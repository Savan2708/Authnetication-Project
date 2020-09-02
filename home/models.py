from django.db import models


class Profile(models.Model):
    img = models.ImageField(upload_to='imgs/')
    about = models.TextField(max_length=255, null=False)
    phnum = models.IntegerField()

    def __str__(self):
        return self.about
