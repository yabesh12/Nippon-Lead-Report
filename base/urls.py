from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name="home"),
    path('lead-sales/<str:pk>',views.lead_sales, name="lead_sales"),
    path('download/<str:pk>',views.download, name="download"),
    path('download-all/',views.download_all, name="download_all"),
]