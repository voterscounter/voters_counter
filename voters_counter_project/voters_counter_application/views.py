# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext


from voters_counter_application.forms import AddVideoForm

def home(request):
  return render_to_response('home.html')

def add_video(request):
  if request.method == 'GET':
    add_video_form = AddVideoForm()
    return render_to_response('add_video.html',
                              { 
                                'add_video_form': add_video_form,
                              }, context_instance=RequestContext(request))
  if request.method == 'POST':
    add_video_form = AddVideoForm(data=request.POST)
    if add_video_form.is_valid():
      video = add_video_form.save()
      return render_to_response('add_video.html',
                          {'add_video_form': add_video_form,
                           'video': video},
                          context_instance=RequestContext(request)
                         )
    else:
      return render_to_response('add_video.html',
                                {'add_video_form': add_video_form},
                                context_instance=RequestContext(request)
                               )