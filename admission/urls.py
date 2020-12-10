from django.urls import path
from .views import (
    ChildListView, ChildDetailView, ChildCreateView, ChildUpdateView, ChildDeleteView,ChildListAllView,
    AuthorityCreateView, AuthorityListView, AuthorityDetailView, AuthorityUpdateView,
    CareHomeCreateView, CareHomeUpdateView, CareHomeDetailView, CareHomeListView,
    Contact_SocialDetailsView, Contact_SocialUpdateView,
    PhysicalDetailView, PhysicalUpdateView,
    HealthDetailView, HealthUpdateView,
    YP_Pen_PicDetailsView, YP_Pen_PicUpdateView,
    YP_Profile_ChildDetailsView, YP_Profile_ChildUpdateView,
    YP_Relationships_AssociatesDetailsView, YP_Relationships_AssociatesUpdateView,
    BankDetailView, BankUpdateView,
    IPADetailView, IPAUpdateView, IPAListView,

)
from . import views


urlpatterns = [
    path('', views.dashboard, name='admission-home'),
    path('child/list/', ChildListView.as_view(), name='admission-list'),
    path('child/all/', ChildListAllView.as_view(), name='admission-all'),
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
    path('home/new/', CareHomeCreateView.as_view(), name='home-create'),
    path('home/<int:pk>/detail/', CareHomeDetailView.as_view(), name='home-detail'),
    path('home/list/', CareHomeListView.as_view(), name='home-list'),
    path('home/<int:pk>update/', CareHomeUpdateView.as_view(), name='home-update'),

    # Young Person Contacts
    path ('contact/<int:pk>/view/', Contact_SocialDetailsView.as_view(), name='contact-detail'),
    path ('contact/<int:pk>/update/', Contact_SocialUpdateView.as_view(), name='contact-update'),

    # Young Person Physical Details
    path('physical/<int:pk>/', PhysicalDetailView.as_view(), name='physical-detail'),
    path('physical/<int:pk>/update/', PhysicalUpdateView.as_view(), name='physical-update'),

    # Health Information
    path('health/<int:pk>/', HealthDetailView.as_view(), name='health-detail'),
    path('health/<int:pk>/update/', HealthUpdateView.as_view(), name='health-update'),

    # Young Person Pen Picture
    path('pen/<int:pk>/view/', YP_Pen_PicDetailsView.as_view(), name='pen-detail'),
    path('pen/<int:pk>/update/', YP_Pen_PicUpdateView.as_view(), name='pen-update'),

    # Young Person Placement Profile
    path('young/<int:pk>/profile/', YP_Profile_ChildDetailsView.as_view(), name='profile-detail'),
    path('young/<int:pk>/profile_update/', YP_Profile_ChildUpdateView.as_view(), name='profile-update'),

    # Young Person Relations and Associates
    path('young/<int:pk>/relations/', YP_Relationships_AssociatesDetailsView.as_view(), name='relations-detail'),
    path('young/<int:pk>/relations_update/', YP_Relationships_AssociatesUpdateView.as_view(), name='relations-update'),

    # Banking Information
    path('bankinfo/<int:pk>/', BankDetailView.as_view(), name='bank-detail'),
    path('bankinfo/<int:pk>/update/', BankUpdateView.as_view(), name='bank-update'),

    path('ipa/<int:pk>/', IPADetailView.as_view(), name='ipa-detail'),
    path('ipa/<int:pk>/list/', IPAListView.as_view(), name='ipa-list'),
    path('ipa/<int:pk>/update/', IPAUpdateView.as_view(), name='ipa-update'),


]