from django.db import models

# Create your models here.
# title
# publication date
# body
# image
class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

#Add blog app to settings

#create migration

#migrate 

#add to the admin