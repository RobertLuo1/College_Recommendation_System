from django.urls import path
from .import views
from django.conf.urls import url

urlpatterns = [
    path('query',views.query,name='query'),
    path('queryCollege',views.queryCollege,name='queryCollege'),
    path('find',views.find,name='find'),
    path('result',views.result,name='result'),
    path('collegeRank',views.collegeRank,name='collegeRank'),
    path('Jobs',views.Jobs,name='Jobs')
]




