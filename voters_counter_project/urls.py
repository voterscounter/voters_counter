from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView


from voters_counter_application.models import Video

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # TODO Following URL pattern should be overriden by some HTTP Server alias for 
    #   performance and security reasons
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
    url(r'^$', 'voters_counter_application.views.home', name='home'),
    url(r'^add_video/$', 'voters_counter_application.views.add_video', name='add_video'),
    url(r'^list_videos/$', ListView.as_view(model=Video, template_name='video_list.html'), name='list_videos'),
    # url(r'^voters_counter_project/', include('voters_counter_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
