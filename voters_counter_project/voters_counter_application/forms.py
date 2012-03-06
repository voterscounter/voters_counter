from django import forms
from voters_counter_application.models import Video

# UNITTEST: Too low complexity to have unittests
class AddVideoForm(forms.ModelForm):
  class Meta:
    model = Video
    
class VoteForm(forms.Form):
  timestamp = forms.FloatField()
  vote_type = forms.CharField()
  box = forms.CharField()
  video_id = forms.IntegerField()
  