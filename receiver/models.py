from django.db import models

# Create your models here.
class Province(models.Model):
    name = models.Textfield(default='')
    ruler = models.TextField(default='')
    race = models.ForeignKey('Race', on_delete=models.SET_NULL, null=True)
    personality = models.ForeignKey('Personality', on_delete=models.SET_NULL, null=True)
    kingdom = models.ForeignKey('Kingdom', on_delete=models.SET_NULL, null=True)

class Race(models.Model):
    name = models.Charfield(max_length=20, help_text="Utopian Race")

    def __str__(self):
        """ String to represent the model object, for instance in Admin site """

        return self.name
