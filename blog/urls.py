from django.urls import path

from . import views

urlpatterns = [
    path('', views.VideocontentView.as_view()),
    path("<int:pk>/", views.VideocontentDetailView.as_view(), name="videocontent_detail"),
    path("commentary/<int:pk>/", views.AddCommentary.as_view(), name="add_commentary")
]