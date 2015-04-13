from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'remotelauncher.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('launcher.urls')),
]

admin.site.site_header = "Remote launcher administration"
admin.site.site_title = "Remote launcher site admin"
