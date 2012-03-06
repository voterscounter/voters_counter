from django import forms
from voters_counter_application.models import Video

# UNITTEST: Too low complexity to have unittests
class AddVideoForm(forms.ModelForm):
  class Meta:
    model = Video