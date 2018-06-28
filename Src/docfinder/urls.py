from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('results/', views.results, name='results'),
    path('import/', views.import_data, name='import'),
    path('all_doctors/', views.all_doctors, name='all_doctors')
]
