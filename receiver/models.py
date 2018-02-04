from django.db import models

# Create your models here.
class Province(models.Model):
    name = models.TextField(default='')
    ruler = models.TextField(default='')
    race = models.ForeignKey('Race', on_delete=models.CASCADE, null=True)
    personality = models.ForeignKey('Personality', on_delete=models.CASCADE, null=True)
    kingdom = models.ForeignKey('Kingdom', on_delete=models.CASCADE, null=True)

class Race(models.Model):
    name = models.CharField(max_length=20, help_text="Utopian Race")

    def __str__(self):
        """ String to represent the model object, for instance in Admin site """

        return self.name



class Personality(models.Model):
    name = models.CharField(max_length=20, help_text="Ruler's personality")

    def __str__(self):
        """ String to represent the model object, for instance in Admin site """

        return self.name


class Kingdom(models.Model):
    name = models.CharField(max_length=20, help_text="Kingdom name")

    def __str__(self):
        """ String to represent the model object, for instance in Admin site """

        return self.name






