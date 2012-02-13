from django.db import models

class Candidate(models.Model):
	name = models.CharField(max_length=200)
	party = models.CharField(max_length=200)
	bio = models.TextField()

class Tweet(models.Model):
	id = models.IntegerField(primary_key=True)
        created_at = models.DateTimeField()
        text = models.TextField()
        user = models.CharField(max_length=200)
	raw_json = models.TextField()
        urls = models.ManyToManyField('URL') 
        candidates = models.ManyToManyField('Candidate')       

class URL(models.Model):
	url = models.TextField()
