from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.
class Home(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = '/'
    def get(self, request, *args, **kwargs):
        return render(request, "candidateManager/home.html", {})

class Locations_List(ListView):
    template_name = 'candidateManager/Location/location_list.html'
    model = Location

class Locations_FilterList(ListView):
    template_name = 'candidateManager/JobReq/jobrequesition_list.html'
    model = JobRequesition

    def get_queryset(self):
        self.location = get_object_or_404(Location, id=self.kwargs['pk'])
        return JobRequesition.objects.filter(location=self.location)


class Locations_Create(CreateView):
    template_name = 'candidateManager/Location/location_form.html'
    model = Location
    success_url = reverse_lazy('location_list')
    fields = ['city', 'state']

class Locations_Update(UpdateView):
    template_name = 'candidateManager/Location/location_form.html'
    model = Location
    success_url = reverse_lazy('location_list')
    fields = ['city', 'state']

class Locations_Delete(DeleteView):
    template_name = 'candidateManager/Location/location_confirm_delete.html'
    model = Location
    success_url = reverse_lazy('location_list')

class Locations_Detail(DetailView):
    template_name = 'candidateManager/Location/location_detail.html'
    model = Location

class JobRequesition_List(ListView):
    template_name = 'candidateManager/JobReq/jobrequesition_list.html'
    model = JobRequesition

class JobRequesition_Create(CreateView):
    template_name = 'candidateManager/JobReq/jobrequesition_form.html'
    model = JobRequesition
    success_url = reverse_lazy('jobRequesition_list')
    fields = ['position', 'offerRate','location']

    def get_context_data(self, **kwargs):
        context = super(JobRequesition_Create, self).get_context_data(**kwargs)
        context["location_list"] = Location.objects.all()
        return context

class JobRequesition_Update(UpdateView):
    template_name = 'candidateManager/JobReq/jobrequesition_form.html'
    model = JobRequesition
    success_url = reverse_lazy('jobRequesition_list')
    fields = ['position', 'offerRate','location']

class JobRequesition_Detail(DetailView):
    template_name = 'candidateManager/JobReq/jobrequesition_detail.html'
    model = JobRequesition
    context_object_name = 'jobrequesition'

    def get_context_data(self, **kwargs):
        context = super(JobRequesition_Detail, self).get_context_data(**kwargs)
        self.jobRequesition = get_object_or_404(JobRequesition, id=self.kwargs['pk'])
        context["candidate_list"] = Candidate.objects.filter(jobRequesition=self.jobRequesition)
        return context

class JobRequesition_Delete(DeleteView):
    template_name = 'candidateManager/JobReq/jobrequesition_confirm_delete.html'
    model = JobRequesition
    success_url = reverse_lazy('jobRequesition_list')

class JobRequesition_FilterList(ListView):
    template_name = 'candidateManager/Candidate/candidate_list.html'
    model = Candidate

    def get_queryset(self):
        self.jobRequesition = get_object_or_404(JobRequesition, id=self.kwargs['pk'])
        return Candidate.objects.filter(jobRequesition=self.jobRequesition)


class Candidates_List(ListView):
    template_name = 'candidateManager/Candidate/candidate_list.html'
    model = Candidate

class Candidates_Detail(DetailView):
    template_name = 'candidateManager/Candidate/candidate_detail.html'
    model = Candidate
    context_object_name = 'candidate'
    success_url = reverse_lazy('candidate_detail')

    def get_context_data(self, **kwargs):
        context = super(Candidates_Detail, self).get_context_data(**kwargs)
        self.candidate = get_object_or_404(Candidate, id=self.kwargs['pk'])
        context["note_list"] = Notes.objects.filter(candidate=self.candidate)
        return context

class Candidates_Create(CreateView):
    template_name = 'candidateManager/Candidate/candidate_form.html'
    model = Candidate
    success_url = reverse_lazy('candidate_list')
    fields = ['firstName', 'lastName','phoneNumber','email','jobRequesition']

    def get_context_data(self, **kwargs):
        context = super(Candidates_Create, self).get_context_data(**kwargs)
        context["job_list"] = JobRequesition.objects.all()
        return context

class Candidates_Update(UpdateView):
    template_name = 'candidateManager/Candidate/candidate_form.html'
    model = Candidate
    success_url = reverse_lazy('candidate_list')
    fields = ['firstName', 'lastName','phoneNumber','email','jobRequesition']

    def get_context_data(self, **kwargs):
        context = super(Candidates_Update, self).get_context_data(**kwargs)
        self.candidate = get_object_or_404(Candidate, id=self.kwargs['pk'])
        context["job_list"] = JobRequesition.objects.all()
        return context

class Candidates_Delete(DeleteView):
    template_name = 'candidateManager/Candidate/candidate_confirm_delete.html'
    model = Candidate
    success_url = reverse_lazy('candidate_list')

class Note_Create(CreateView):
    template_name = 'candidateManager/Notes/notes_form.html'
    model = Notes
    candidatepk = 5
    success_url = reverse_lazy('candidate_detail', kwargs={'pk': candidatepk})
    fields = ['note']

    def form_valid(self, form):
        object = form.save(commit=False)
        object.createdby = self.request.user
        object.candidate = get_object_or_404(Candidate, pk = self.kwargs['pk'])
        candidatepk = self.kwargs['pk']
        object.save()
        return super(Note_Create, self).form_valid(form) 



class Notes_List(ListView):
    template_name = 'candidateManager/Notes/notes_list.html'
    model = Notes

    def get_queryset(self):
        self.candidate = get_object_or_404(Candidate, id=self.kwargs['pk'])
        return Notes.objects.filter(candidate=self.candidate)
