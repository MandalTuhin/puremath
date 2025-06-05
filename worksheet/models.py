from django.db import models

# Create your models here.


class Worksheet(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='worksheets/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.date}"
