# -*- coding: utf-8 -*-

from django.db import models

class Video(models.Model):
  # TODO Migrate to models.URLField()
  url = models.CharField(max_length=2048) # Reasonable limitation
  
  def get_embed_url(self):
    video_url_id = self.url.split('/')
    return 'http://www.youtube.com/embed/%s' % video_url_id[-1]
    
  def get_embed_url_with_api(self):
    video_url_id = self.url.split('/')
    return 'http://www.youtube.com/v/%s?version=3&enablejsapi=1' % video_url_id[-1]

class Vote(models.Model):
  video = models.ForeignKey(Video)
  time_period_start = models.IntegerField()
  time_period_stop = models.IntegerField()
  box = models.CharField(max_length=1)
  violation = models.BooleanField(default=False)
  
  def __unicode__(self):
    if self.violation:
      return u'%s:%s:нарушение' % (self.time_period_start, self.time_period_stop)
    else:
      return u'%s:%s:урна %s' % (self.time_period_start, self.time_period_stop, self.box)