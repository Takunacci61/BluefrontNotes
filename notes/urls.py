from django.urls import path
from .views import (
    NotesListView, NotesDetailView, NotesCreateView, NotesUpdateView, NotesDeleteView, UserPostListView,
    ParentNotesListView, ParentNotesDetailView, ParentNotesCreateView, ParentNotesUpdateView, ParentNotesDeleteView
)
from . import views

urlpatterns = [
    path('notes/<int:pk>/new/', NotesCreateView.as_view(), name='notes-create'),
    path('notes/<int:pk>/details/', NotesDetailView.as_view(), name='notes-detail'),
    path('notes/<int:pk>/update/', NotesUpdateView.as_view(), name='notes-update'),
    path('notes/<int:pk>/delete/', NotesDeleteView.as_view(), name='notes-delete'),
    path('notes/<int:pk>/list/', NotesListView.as_view(), name='notes-list'),
    path('notes/reports/', views.show_all_yp_page, name='notes-report'),
    path('notes/reports/<int:pk>/child/', views.show_all_child_page, name='notes-child'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name='notes-about'),
    # Parent notes
    path('parent/notes/<int:pk>/new/', ParentNotesCreateView.as_view(), name='parent-notes-create'),
    path('parent/notes/<int:pk>/details/', ParentNotesDetailView.as_view(), name='parent-notes-detail'),
    path('parent/notes/<int:pk>/update/', ParentNotesUpdateView.as_view(), name='parent-notes-update'),
    path('parent/notes/<int:pk>/delete/', ParentNotesDeleteView.as_view(), name='parent-notes-delete'),
    path('parent/notes/<int:pk>/list/', ParentNotesListView.as_view(), name='parent-notes-list'),

    # path('notes/reports/', views.show_all_yp_parent_notes, name='parent-notes-report'),
    # path('notes/reports/<int:pk>/child/', views.parent_show_all_child_page, name='parent-notes-child'),





]