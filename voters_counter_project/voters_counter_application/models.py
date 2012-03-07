# -*- coding: utf-8 -*-

from django.db import models

class Video(models.Model):
  # TODO Migrate to models.URLField() ?
  url = models.CharField(max_length=2048) # Reasonable limitation
  
  def get_embed_url(self):
    video_url_id = self.url.split('/')
    return 'http://www.youtube.com/embed/%s' % video_url_id[-1]
    
  def get_embed_url_with_api(self):
    video_url_id = self.url.split('/')
    return 'http://www.youtube.com/v/%s?version=3&enablejsapi=1' % video_url_id[-1]

# TODO Support more than 24 hour durations properly
def humanize_seconds(seconds):
  """Return humanized duration in HH:mm:ss format.
  
  HH may be greater than 24. For less than minute return ss seconds, for less than hour return mm:ss
  
  >>> humanize_seconds(0)
  u'0 \u0441'
  >>> humanize_seconds(1)
  u'1 \u0441'
  >>> humanize_seconds(12)
  u'12 \u0441'
  >>> humanize_seconds(59)
  u'59 \u0441'
  >>> humanize_seconds(60)
  u'1:00'
  >>> humanize_seconds(68)
  u'1:08'
  >>> humanize_seconds(81)
  u'1:21'
  >>> humanize_seconds(681)
  u'11:21'
  >>> humanize_seconds(3681)
  u'1:01:21'
  >>> humanize_seconds(36081)
  u'10:01:21'
  >>> humanize_seconds(40281)
  u'11:11:21'
  >>> humanize_seconds(90000)
  u'25:00:00'
  """
  seconds_int = int(seconds)
  hours = seconds_int / 60 / 60
  minutes = seconds_int / 60 % 60
  seconds = seconds_int % 60 % 60
  if hours:
    return u'%d:%02d:%02d' % (hours, minutes, seconds)
  elif minutes:
    return u'%d:%02d' % (minutes, seconds)
  else:
    return u'%d с' % seconds

class Vote(models.Model):
  video = models.ForeignKey(Video)
  time_period_start = models.IntegerField()
  time_period_stop = models.IntegerField()
  box = models.CharField(max_length=1)
  violation = models.BooleanField(default=False)
  
  def get_humanized_time_period_start(self):
    return humanize_seconds(self.time_period_start)
    
  def get_humanized_time_period_stop(self):
    return humanize_seconds(self.time_period_stop)
  
  def __unicode__(self):
    if self.violation:
      return u'%s:%s:нарушение' % (self.time_period_start, self.time_period_stop)
    else:
      return u'%s:%s:урна %s' % (self.time_period_start, self.time_period_stop, self.box)