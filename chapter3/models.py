import re
from django.core.exceptions import ValidationError
from django.db import models


def number_only(value):
    if re.match(r'^[0~9]*$', value) == None:
        raise ValidationError(
            '%(value)s is not Number!',
            params={'value': value}
        )


# Create your models here.
class Friend(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[number_only]
    )
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField()
    birthday = models.DateField()

    def __str__(self):
        return (
            "<Friend:id="
            + str(self.id)
            + ","
            + self.name
            + "("
            + str(self.age)
            + ")>"
        )
