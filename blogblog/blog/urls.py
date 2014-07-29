__author__ = 'wikibootup'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^', 'index')

    # Examples:
    # url(r'^$', 'blogblog.views.home', name='home'),
  #  url(r'^blog/', include('blog.urls')),

   # url(r'^admin/', include(admin.site.urls)),
)
