from django.urls import path
from .views import (
    NotesListView, NotesDetailView, NotesCreateView, NotesUpdateView, NotesDeleteView, UserPostListView
)
from . import views

urlpatterns = [
    path('/notes/<int:pk>/new/', NotesCreateView.as_view(), name='notes-create'),
    path('/notes/<int:pk>/details/', NotesDetailView.as_view(), name='notes-detail'),
    path('notes/<int:pk>/update/', NotesUpdateView.as_view(), name='notes-update'),
    path('/notes/<int:pk>/delete/', NotesDeleteView.as_view(), name='notes-delete'),
    path('/notes/<int:pk>/list/', NotesListView.as_view(), name='notes-list'),
    path('notes/reports/', views.show_all_yp_page, name='notes-report'),
    path('notes/reports/<int:pk>/child/', views.show_all_child_page, name='notes-child'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name='notes-about'),




]