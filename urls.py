from django.conf.urls import url, include
from .views import ProjectListAndFormView

urlpatterns = [
    url(r'^$', ProjectListAndFormView.as_view(), name='main')
]
