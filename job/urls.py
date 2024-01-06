from django.urls import path, include
from . import views

app_name = "job"

urlpatterns = [
    path('', views.job_list, name="job_list"),
    path('<str:slug>', views.job_detail, name="job_detail"),
    path('job/apply', views.add_job, name="add_job")
]
