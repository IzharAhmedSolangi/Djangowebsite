from django.db import models

# Create your models here.
class polls(models.Model):
    title= models.TextField(null=True , blank=True)
    op1 = models.CharField(max_length=100)
    op2 = models.CharField(max_length=100)
    op3 = models.CharField(max_length=100)
    op4 = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
    