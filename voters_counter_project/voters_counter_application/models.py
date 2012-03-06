from django.db import models

class Video(models.Model):
  # TODO Migrate to models.URLField()
  url = models.CharField(max_length=2048) # Reasonable limitation
  
  def get_embed_url(self):
    video_url_id = self.url.split('/')
    return 'http://www.youtube.com/embed/%s' % video_url_id[-1]
  
class Vote(models.Model):
  video = models.ForeignKey(Video)
  time_period_start = models.IntegerField()
  time_period_stop = models.IntegerField()