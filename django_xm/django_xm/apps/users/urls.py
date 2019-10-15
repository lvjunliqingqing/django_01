from django.conf.urls import url

from django_xm.apps.users import views

urlpatterns = [
    url(r'^test/', views.TestView.as_view()),
]