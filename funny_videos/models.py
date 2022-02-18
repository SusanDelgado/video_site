from django.db import models

class Video(models.Model):
    video_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.video_name