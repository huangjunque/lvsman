from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lvsman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^status/$', 'status.views.status'),
    url(r'^play/$', 'del_server.views.play'),
    url(r'^delete_vip/$', 'del_server.views.del_vip'),
    url(r'^delete_node/$', 'del_server.views.del_node'),
)
urlpatterns += staticfiles_urlpatterns()
