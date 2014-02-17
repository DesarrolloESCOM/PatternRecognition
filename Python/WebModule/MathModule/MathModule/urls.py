from django.conf.urls import patterns, url
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MathModule.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^prueba/$', 'MathModule.views.index'),
    url(r'^render/$', 'MathModule.views.templateRender'),
    url(r'^renderShortCut/$', 'MathModule.views.shortCutRender'),
    #url(r'^admin/', include(admin.site.urls)),
)
