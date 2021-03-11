from django.urls import path
from .views import lead_list, detail_view, lead_create, lead_update, lead_delete

app_name = 'leads'

urlpatterns = [
    path('', lead_list),
    path('<int:pk>/', detail_view),
    path('<int:pk>/update/', lead_update),
    path('<int:pk>/delete/', lead_delete),
    path('create/', lead_create),
]