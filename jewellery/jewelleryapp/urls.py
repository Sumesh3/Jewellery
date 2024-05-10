from django.urls import path
from .import views

urlpatterns = [
    path("single_jewellery_items_api/<int:id>", views.single_jewellery_items_api.as_view(), name="single_jewellery_items_api"),
    path("all_jewellery_items_api", views.all_jewellery_items_api.as_view(), name="all_jewellery_items_api"),
]
