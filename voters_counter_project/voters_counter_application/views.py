# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from voters_counter_application.models import Video, Vote
from voters_counter_application.forms import AddVideoForm, VoteForm

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
                               
def edit_video(request, video_id):
  # TODO handle video not found properly
  video = Video.objects.get(pk=video_id)
  votes = Vote.objects.filter(video=video).order_by('time_period_start')
  return render_to_response('edit_video.html',
                            {'video': video,
                             'votes': votes},
                            context_instance=RequestContext(request)
                           )

# TODO Handle GETs properly
# TODO Provide CSRF verification
# TODO Handle errors properly
@csrf_exempt
def vote(request):
  if request.method == 'POST':
    vote_form = VoteForm(data=request.POST)
    if vote_form.is_valid():
      timestamp = vote_form.cleaned_data['timestamp']
      vote_type = vote_form.cleaned_data['vote_type']
      box = vote_form.cleaned_data['box']
      video_id = vote_form.cleaned_data['video_id']
      vote_type = vote_form.cleaned_data['vote_type']
      
      if vote_type == 'vote':
        Vote.objects.create(video_id=video_id, 
                            time_period_start=int(timestamp), 
                            time_period_stop=int(timestamp) + 2, # TODO This should be change when buckets are implemented
                            box=box)
        return HttpResponse('OK')
      elif vote_type == 'violation':
        Vote.objects.create(video_id=video_id, 
                            time_period_start=int(timestamp), 
                            time_period_stop=int(timestamp) + 2, # TODO This should be change when buckets are implemented
                            violation=True)
        return HttpResponse('OK')
      else:
        return HttpResponse('UNKNOWN VOTE TYPE: %s' % vote_type, status='400')