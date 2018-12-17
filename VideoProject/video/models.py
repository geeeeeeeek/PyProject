from django.db import models
from django.conf import settings

# Create your models here.


class Video(models.Model):

    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    view_count = models.IntegerField(default=0, blank=True)
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   blank=True, related_name="liked_videos")
    collected = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   blank=True, related_name="collected_videos")
    create_time = models.DateTimeField(auto_now_add=True, blank=True, max_length=20)

    class Meta:
        db_table = "v_video"

    def switch_like(self, user):
        if user in self.liked.all():
            self.liked.remove(user)

        else:
            self.liked.add(user)

    def count_likers(self):
        return self.liked.count()

    def get_likers(self):
        return self.liked.all()

    def user_liked(self, user):
        if user in self.liked.all():
            return 0
        else:
            return 1

    def switch_collect(self, user):
        if user in self.collected.all():
            self.collected.remove(user)

        else:
            self.collected.add(user)

    def count_collecters(self):
        return self.collected.count()

    def get_collecters(self):
        return self.collected.all()

    def user_collected(self, user):
        if user in self.collected.all():
            return 0
        else:
            return 1