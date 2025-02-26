from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListExercises.as_view(),name="home"),
    path("exercises/<int:pk>", views.SingleDetailExercise.as_view(),name="detail"),
    path("add_exercise",views.AddExercise.as_view(),name="add_exercise"),
    path('update-exercise/<int:pk>/', views.UpdateExercise.as_view(), name='update-exercise'),
    path('delete-exercise/<int:pk>/', views.DeleteExercise.as_view(), name='delete-exercise'),
    path("favorites",views.Favorites.as_view(),name="favorites"),
    path("add_favorite/<int:pk>/", views.add_favorite, name="add_favorite"),  
]

