from django.db import models


class SamplePost(models.Model):
    post_image = models.ImageField()
