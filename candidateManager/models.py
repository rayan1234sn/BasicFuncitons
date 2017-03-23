from django.db import models
from django.utils import timezone 
import datetime
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length = 40)
    state = models.CharField(max_length = 40)
    
    #def __unicode__(self):
    def __str__(self):
        return self.city +" "+ self.state

    def get_absolute_url(self):
        return reverse('location_list', kwargs={'pk': self.pk})
       

class JobRequesition(models.Model):
    position = models.CharField(max_length = 40)
    offerRate = models.CharField(max_length = 40)
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.position +", "+ self.location.city

    def get_absolute_url(self):
        return reverse('candidate_list', kwargs={'pk': self.pk})    
 

class Candidate(models.Model):
    firstName = models.CharField(max_length = 20)
    lastName = models.CharField(max_length = 20)
    phoneNumber = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 40)
    jobRequesition = models.ForeignKey(JobRequesition, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstName +" "+ self.lastName 

    def get_absolute_url(self):
        return reverse('candidate_list', kwargs={'pk': self.pk})


class Notes(models.Model):
    note = models.CharField(max_length = 400)
    created = models.DateTimeField(editable=False)
    createdby = models.ForeignKey(User, null = True)
    candidate = models.ForeignKey(Candidate, null=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        return super(Notes, self).save(*args, **kwargs)    
