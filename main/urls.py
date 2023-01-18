from django.urls import path
from . import views

urlpatterns = [
    path('about-us/', views.AboutUsAPIView.as_view()),
    path('news/', views.NewsListAPIView.as_view()),
    path('news/<int:pk>/', views.NewsDetailAPIView.as_view()),
    path('scientist/', views.ScientistListAPIView.as_view()),
    path('scientist/<int:pk>/', views.ScientistDetailAPIView.as_view()),
    path('scientist-movie/', views.ScientistMovieAPIView.as_view()),
    path('scientist-audio/', views.ScientistAudioListAPIView.as_view()),
    path('scientist-ebook/', views.ScientistEbookListAPIView.as_view()),
    path('scientist-foto/', views.ScientistFotoAPIView.as_view()),
    path('test/', views.TestListAPIView.as_view())
]
