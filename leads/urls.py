from django.urls import path
from .views import lead_list, detail_view, lead_create

app_name = 'leads'

urlpatterns = [
    path('', lead_list),
    path('<int:pk>/', detail_view),
    path('create/', lead_create),
]