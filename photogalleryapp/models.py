from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null = False, blank = False) #cannot be blank

    def __str__(self):
        return self.name
    

class Photo(models.Model):
    category = models.ForeignKey(Category, null = True, blank = True, on_delete=models.SET_NULL) #delete a category wont delete the photo
    image = models.ImageField(null = False, blank = False)
    description = models.TextField() #cannot be blank

    def __str__(self):
        return self.description
    
