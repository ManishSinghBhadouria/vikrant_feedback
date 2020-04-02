from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('course',views.course,name='course'),
    path('element',views.element,name='element'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('validate',views.validate,name='validate'),
    path('stdlogout',views.stdlogout,name='stdlogout'),
    path('faclogout',views.faclogout,name='faclogout'),
    path('alogout',views.alogout,name='alogout'),
    path('recovery',views.recovery,name='recovery'),


    #ADMIN
    path('subfeed', views.subfeed, name='subfeed'),
    path('subwisefeed', views.subwisefeed, name='subwisefeed'),
    path('facwisefeed', views.facwisefeed, name='facwisefeed'),
    path('subreg', views.subreg, name='subreg'),
    path('strtfeed',views.strtfeed,name='strtfeed'),
    path('start_feedback',views.start_feedback,name='start_feedback'),
    path('addsub',views.addsub,name='addsub'),
    path('addfac',views.addfac,name='addfac'),
    path('allotsub',views.allotsub,name='allotsub'),
    path('viewfac',views.viewfac,name='viewfac'),
    path('viewstd',views.viewstd,name='viewstd'),
    path('viewsub',views.viewsub,name='viewsub'),
    path('viewalmt',views.viewalmt,name='viewalmt'),
    path('viewfeedback',views.viewfeedback,name='viewfeedback'),
    path('viewfeed',views.viewfeed,name='viewfeed'),
    path('subwisefeed',views.subwisefeed,name='subwisefeed'),
    path('facwisefeed',views.facwisefeed,name='facwisefeed'),
    path('subalmt', views.subalmt, name='subalmt'),
    



    #STUDENT
    path('preevfeed', views.preevfeed, name='preevfeed'),
    path('feedreg', views.feedreg, name='feedreg'),
    path('validateotp', views.validateotp, name='validateotp'),
    path('checkotp', views.checkotp, name='checkotp'),
    path('downloadnotes', views.downloadnotes, name='downloadnotes'),
    path('stdupdateprofile', views.stdupdateprofile, name='stdupdateprofile'),
    path('stdviewprofile', views.stdviewprofile, name='stdviewprofile'),



    #FACULTY
    path('uploadnotes', views.uploadnotes, name='uploadnotes'),
    path('facupdateprofile', views.facupdateprofile, name='facupdateprofile'),
    path('facviewprofile', views.facviewprofile, name='facviewprofile'),
    path('fshowsub',views.fshowsub,name='fshowsub'),
    path('faclogin', views.faclogin, name='faclogin'),
    path('facsubwise', views.facsubwise, name='facsubwise'),



    
    path('stddelete/<int:id>', views.stddelete, name='stddelete'),
    path('facdelete/<int:id>', views.facdelete, name='facdelete'),
    path('subdelete/<int:id>', views.subdelete, name='subdelete'),
    path('almtdelete/<int:id>', views.almtdelete, name='almtdelete'),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
