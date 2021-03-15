from django.db import models

# Create your models here.

class Contact(models.Model):
    SrNo = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    phone = models.CharField( max_length=50)
    email = models.EmailField(max_length=254)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add = True, blank =  True)

    #this is a special funtion to return name of that particular
    #object while we see contact list in the admin section.
    #hence with this function we can display each entry
    #in the contact table by its name - its email id
    def __str__(self):
        return self.name + " - " + self.email 
    