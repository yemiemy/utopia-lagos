from django.db import models

# Create your models here.

# News model for collecting News links 
class New(models.Model):
    title = models.CharField(max_length=550)
    link = models.CharField(max_length=1500)
    news_from = models.CharField(max_length=500)
    news_about_utopia = models.BooleanField(default=False)
    news_by_utopia = models.BooleanField(default=False)


# Contact model for collecting contact messages from visitors
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    date_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} contacted on {}".format(self.name, self.date_stamp.date()) 
