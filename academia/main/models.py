from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    TYPE_OF_USER = (
        ('a', 'Alumno'),
        ('d', 'Discipulo'),
        ('i', 'Instructor'),
        ('p', 'Profesor'),
        ('m', 'Maestro'),
        ('g', 'Gran Maestro'),
    )
    user_type = models.CharField(
    	max_length=2,
        choices=TYPE_OF_USER,
        default='a')

    birthday = models.DateField(
    	blank=False, 
    	null=False,
    	)
    pic = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username



