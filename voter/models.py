from django.db import models

# Create your models here.


class Admin(models.Model):

    hub_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.hub_name

class Voter(models.Model):

    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    is_voted = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username


class Candidates(models.Model):

    name = models.CharField(max_length=20)
    votes = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Candidates'

    def __str__(self) -> str:
        return self.name

