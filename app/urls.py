from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
	path('',views.firstpage,name='firstpage'),
     path('login/',views.edu,name = 'edu'),
     path('login/add/',views.educrev,name='educrev'),
     path('login/next/',views.EducationView.as_view(),name='education'),
     path ('login/next/<int:pk>',views.UpdatepostView.as_view(), name='updateview'),
     path('login/next/job/',views.job345, name='job345'),
     path('check',views.formfunction),
     path ('login/next/<int:pk>/delete/',views.Deletepostview.as_view(), name='deleteview'),






     #path('login/back/',views.backopt,name='backopt'),
     #path('login/next/job/',views.skillsfun,name='skillfun'),
     #path('login/next/add/',views.jobadd,name='jobadd'),
     #path('login/next/job/add/',views.skillsadd,name='skillfun'),
     #path('login/next/job/skill/',views.addons,name='home'),
     #path('login/next/job/skill/',views.addonstest,name='home'),
     #path('login/next/job/skill/addonemorefield/',views.addonemoreaddon,name='home'),
     #path('login/next/job/skill/fieldadd/',views.home,name='home'),
     #path('login/next/job/skill/fieldadd/pdf_view/',views.viewPDF.as_view(),name='pdf_view'),
     


]