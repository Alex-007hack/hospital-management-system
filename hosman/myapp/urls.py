from django.urls import path,include
from . import views

urlpatterns = [
   
    path('', views.index,name='home'),
    path('about/', views.about,name='about'),
    path('booking/', views.booking,name='booking'),
    path('doctors/', views.doctors,name='doctors'),
    path('contact/', views.contact,name='contact'),
    path('department/', views.department,name='department'),
    path('about1/', views.about1,name='about1'),
     path('lab/', views.lab,name='lab'),
       path('confirm/', views.confirm,name='confirm'),
         path('main/', views.main,name='main'),
          path('d1/', views.d1,name='d1'),
          path('call/', views.call,name='call'),
          path('test/', views.testi,name='test'),
             path('dep/', views.dep,name='dep'),
              path('login/', views.login,name='login'),
               path('admin1/', views.admin1,name='admin1'),
                path('createdr/', views.createdr,name='createdr'),
                 path('docmain/', views.docmain,name='docmain'),
                  path('drlogin/', views.drlogin,name='drlogin'),
                  path('sendleave/', views.sendleave,name='sendleave'),
                   path('leavecof/', views.leavecof,name='leavecof'),
                    path('viewleave/', views.viewleave,name='viewleave'),
                     path('sendatt/', views.sendatt,name='sendatt'),
                      path('markatt/', views.markatt,name='markatt'),
                       path('attcof/', views.attcof,name='attcof'),
                         path('viewdrat/', views.viewdrat,name='viewdrat'),
                         path('createnu/', views.createnu,name='createnu'),
                             path('nusmain/', views.nusmain,name='nusmain'),
                                 path('nuslogin/', views.nuslogin,name='nuslogin'),
                                  path('sendnusleave/', views.sendnusleave,name='sendnusleave'),
                                      path('viewnusleave/', views.viewnusleave,name='viewnusleave'),
                                       path('mainlogin/', views.mainlogin,name='mainlogin'),
                                       path('nusattview/', views.nusattview,name='nusattview'),
                                       path('accrej/', views.accrej,name='accrej'),
                                          path('myleave/', views.myleave,name='myleave'),
                                           path('userregister',views.userregister,name="userregister"),
                                            path('userlogin',views.userlogin,name="userlogin"),
                                             path('usercomp',views.usercomp,name="usercomp"),
                                                                                          path('usercomp1',views.usercomp1,name="usercomp1"),

                                              path('mycomplaint',views.mycomplaint,name="mycomplaint"),
                                                                                            path('mycomplaint1',views.mycomplaint1,name="mycomplaint1"),

                                              
    path('viewcomplaint',views.viewcomplaint,name="viewcomplaint"),
        path('viewcomplaint1',views.viewcomplaint1,name="viewcomplaint1"),

     path('viewcomplaint2/<int:id>',views.viewcomplaint2,name="viewcomplaint2"),
          path('viewcomplaint3/<int:id>',views.viewcomplaint3,name="viewcomplaint3"),

                                                path('userregister1',views.userregister1,name="userregister1"),
                                                                                            path('userlogin1',views.userlogin1,name="userlogin1"),


                                              
                                       




]
