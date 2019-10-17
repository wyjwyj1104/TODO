from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from TODOS import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("todos/", views.TODOList.as_view(), name="todos_list"),
    path("todos/<int:pk>/", views.TODODetail.as_view(), name="todos_detail"),
    path("todos/create/", views.TODOCreate.as_view(), name="todos_create"),
    path("todos/<int:pk>/update/", views.TODOUpdate.as_view(), name="todos_update"),
    path("todos/<int:pk>/delete/", views.TODODelete.as_view(), name="todos_delete"),
]
