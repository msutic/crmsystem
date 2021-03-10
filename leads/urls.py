from django.urls import path
from .views import lead_list, detail_view

app_name = 'leads'

urlpatterns = [
    path('', lead_list),
    path('<pk>/', detail_view)
]