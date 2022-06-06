
from django.db import models

# Create your models here.


#creating the model for required dataset - naming it as assignments
class assignments(models.Model):

    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    email = models.EmailField()
    createdAt = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
    
    #setting visible name to assignment
    class Meta:
        verbose_name_plural = "assignment"
