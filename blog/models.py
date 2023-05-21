from djongo import models

# Create your models here.

class User(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, null = False)
    email = models.EmailField(null = False)
    password = models.CharField(max_length = 50, null=False)


class Blog(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length = 500, null = False)
    description = models.CharField(max_length = 100000, null = False)
    publish_date = models.DateField()
    image = models.ImageField()
