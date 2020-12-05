from django.urls import path
from .views import (
    ChildListView, ChildDetailView, ChildCreateView, ChildUpdateView, ChildDeleteView,
    AuthorityCreateView, AuthorityListView, AuthorityDetailView, AuthorityUpdateView,
    CareHomeCreateView, CareHomeUpdateView, CareHomeDetailView, CareHomeListView,
    Contact_SocialDetailsView, Contact_SocialUpdateView,

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

    # Placement home
    # Care Home House
    path ('home/new/', CareHomeCreateView.as_view (), name='home-create'),
    path ('home/<int:pk>/detail/', CareHomeDetailView.as_view (), name='home-detail'),
    path ('home/list/', CareHomeListView.as_view (), name='home-list'),
    path ('home/<int:pk>update/', CareHomeUpdateView.as_view (), name='home-update'),

    # Young Person Contacts
    path ('contact/<int:pk>/view/', Contact_SocialDetailsView.as_view (), name='contact-detail'),
    path ('contact/<int:pk>/update/', Contact_SocialUpdateView.as_view (), name='contact-update'),


]