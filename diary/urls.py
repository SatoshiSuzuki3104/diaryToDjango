from django.urls import path
from . import views

app_name = "diary"

urlpatterns = [
    # path("", views.index, name='index'),
    # 汎用Viewを使用するときはas_viewを定義しないといけない
    path('', views.IndexView.as_view(), name="index"),

    # path('add/', views.add, name='add'),
    path('add/', views.AddView.as_view(), name='add'),

    # path("update/<int:pk>", views.update, name="update"),
    path("update/<int:pk>", views.UpdateView.as_view(), name="update"),

    # path("delete/<int:pk>", views.delete, name="delete"),
    path("delete/<int:pk>", views.DeleteView.as_view(), name="delete"),

    # path("detail/<int:pk>", views.detail, name="detail")
    path("detail/<int:pk>", views.DetailView.as_view(), name="detail")
]