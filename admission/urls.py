from django.urls import path
from .views import (
    ChildListView, ChildDetailView, ChildCreateView, ChildUpdateView, ChildDeleteView,
    AuthorityCreateView, AuthorityListView, AuthorityDetailView, AuthorityUpdateView,

)
from . import views


urlpatterns = [
    path('', views.home, name='admission-home'),
    path('child/lisit/', ChildListView.as_view(), name='admission-list'),
    path('admissions/', views.admissions, name='admission-admissions'),

    # General Information
    path('/child/new/', ChildCreateView.as_view(), name='child-create'),
    path('/child/<int:pk>/', ChildDetailView.as_view(), name='child-detail'),
    path('/child/<int:pk>/update/', ChildUpdateView.as_view(), name='child-update'),
    path('/child/<int:pk>/delete/', ChildDeleteView.as_view(), name='child-delete'),

    # Placement Authority
    path('authority/new/', AuthorityCreateView.as_view(), name='authority-create'),
    path('authority/list/', AuthorityListView.as_view(), name='authority-list'),
    path('authority/<int:pk>/update/', AuthorityUpdateView.as_view(), name='authority-update'),
    path('authority/<int:pk>/detail/', AuthorityDetailView.as_view(), name='authority-detail'),


]