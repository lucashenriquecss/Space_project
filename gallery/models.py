from django.db import models
from datetime import datetime

# Create your models here.
CATEGORY = [
    ('Nebulosa', 'Nebulosa'),
    ('Planeta', 'Planeta'),
    ('Estrela', 'Estrela'),
    ('Galáxia', 'Galáxia'),
   
]
class Gallery(models.Model):
    photo = models.ImageField(upload_to='photos/%d/%m/%Y', blank = True)
    title = models.CharField(max_length=200)
    categories = models.CharField(max_length=20,choices=CATEGORY, default='Planeta')
    description = models.TextField(max_length=1000,blank=True)
    date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
