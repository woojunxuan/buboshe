from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    author = models.CharField(null=True, blank=True, max_length=32)
    introduction = models.CharField(null=True, blank=True, max_length=255)
    content = models.TextField(null=True, blank=True)
    cover = models.FileField(upload_to='cover_image', null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
