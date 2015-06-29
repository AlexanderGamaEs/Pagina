from django.db import models

class SectionMainPage(models.Model):
    name = models.CharField(
		max_length=48,
		blank=False,
		null=False)

    content = models.TextField(
    	blank=False, 
    	null=False,)

    last_edition = models.DateField(
    	blank=False, 
    	null=False,
    	)
    def __str__(self):
        return self.name
