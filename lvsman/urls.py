from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lvsman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^status/$', 'status.views.status'),
    url(r'^play/$', 'del_server.views.play'),
    url(r'^play_add_vip/$', 'add_server.views.add_vip'),
    url(r'^play_add_node/$', 'add_server.views.add_node'),
    url(r'^add_vip/$', 'add_server.views.add_vip_data'),
    url(r'^add_node/$', 'add_server.views.add_node_data'),
    url(r'^delete_vip/$', 'del_server.views.del_vip'),
    url(r'^delete_node/$', 'del_server.views.del_node'),
)
urlpatterns += staticfiles_urlpatterns()
