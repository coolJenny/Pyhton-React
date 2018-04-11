from django.conf.urls import url
from . import views
urlpatterns = [
    url('api/lead/', views.LeadListCreate.as_view() ),
]