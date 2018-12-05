from django.db import models

# Create your models here.


class Video(models.Model):

    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    view_count = models.IntegerField(default=0, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True, max_length=20)

    class Meta:
        db_table = "v_video"
