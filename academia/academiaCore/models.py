from django.db import models
from django.contrib.auth.models import User


TYPE_OF_USER = (
    ('a', 'Alumno'),
    ('d', 'Discipulo'),
    ('i', 'Instructor'),
    ('p', 'Profesor'),
    ('m', 'Maestro'),
    ('g', 'Gran Maestro'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    user_type = models.CharField(
    	max_length=2,
        choices=TYPE_OF_USER,
        default='a')

    birthday = models.DateField(
    	blank=False, 
    	null=False,
    	)
    pic = models.ImageField(
    	upload_to='profile_images', 
    	blank=True)
    enable = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username



