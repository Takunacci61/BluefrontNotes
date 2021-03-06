import os

from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .forms import YP_General_InformationForm, Local_AuthorityForm, Care_House_InfomationForm, \
    Contact_Social_DetailsForm, YP_Physical_DescriptionForm, YP_Health_And_WellnessForm, YP_Banking_InformationForm, \
    YP_Pen_PicForm, YP_Profile_ChildForm, \
    YP_Relationships_AssociatesForm, YP_IPAForm, Profile_PicUpdateForm

from .models import YP_General_Information, Local_Authority, Care_House_Information, YP_Contact_Info, \
    YP_Physical_Description, \
    YP_Health_And_Wellness, YP_Banking_Information, YP_Pen_Pic, YP_Profile_Child, YP_Relationships_Associates, YP_IPA, \
    Profile_Pic


def dashboard(request):
    dashboard_placement_count = YP_General_Information.objects.count ()
    dashboard_house_count = Care_House_Information.objects.count ()
    dashboard_local_authority_count = Local_Authority.objects.count ()
    dashboard_recent_placement = YP_General_Information.objects.all ().order_by ('-yp_date_added')[:3]

    return render (request, 'admission/dashboard.html', {'dashboard_placement_count': dashboard_placement_count,
                                                         'dashboard_local_authority_count': dashboard_local_authority_count,
                                                         'dashboard_house_count': dashboard_house_count,
                                                         'dashboard_recent_placement': dashboard_recent_placement})


def admissions(request):
    context = {
        'young_person_info': YP_General_Information.objects.select_related ('profile_pic')

    }

    return render (request, 'admission/home.html', context)


def young_person_local_authority_view(request, pk):
    yp_local_authority_details = YP_General_Information.objects.select_related ('local_authority')
    return render (request, 'admission/yp_local_authority_details.html',
                   {'yp_local_authority_details': yp_local_authority_details})


class ChildListView (ListView):
    queryset = YP_General_Information.objects.select_related ('profile_pic')
    template_name = 'admission/my_placements.html'
    context_object_name = 'young_person_info'
    ordering = ['-yp_date_added']


class ChildListAllView (ListView):
    queryset = YP_General_Information.objects.select_related ('profile_pic')
    template_name = 'admission/all_placements.html'
    context_object_name = 'young_person_all'
    ordering = ['-yp_date_added']


class ChildDetailView (DetailView):
    model = YP_General_Information
    template_name = 'admission/yp_general_information_detail.html'


class ChildCreateView (LoginRequiredMixin, CreateView):
    model = YP_General_Information
    form_class = YP_General_InformationForm
    template_name = 'admission/new_admission.html'

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super ().form_valid (form)


class ChildUpdateView (LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = YP_General_Information
    form_class = YP_General_InformationForm
    template_name = 'admission/yp_general_information_update.html'

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super ().form_valid (form)

    def test_func(self):
        YP_General_Information = self.get_object ()
        if self.request.user == YP_General_Information.staff:
            return True
        return False


class ChildDeleteView (LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = YP_General_Information
    success_url = '/'
    template_name = 'admission/admission_confirm_delete.html'

    def test_func(self):
        YP_General_Information = self.get_object ()
        if self.request.user == YP_General_Information.staff:
            return True
        return False


# Placement Authority

class AuthorityCreateView (LoginRequiredMixin, CreateView):
    model = Local_Authority
    form_class = Local_AuthorityForm
    template_name = 'admission/new_authority.html'


class AuthorityUpdateView (LoginRequiredMixin, UpdateView):
    model = Local_Authority
    form_class = Local_AuthorityForm
    template_name = 'admission/new_authority.html'


class AuthorityDetailView (LoginRequiredMixin, DetailView):
    model = Local_Authority
    template_name = 'admission/local_authority_detail.html'


class AuthorityListView (LoginRequiredMixin, ListView):
    model = Local_Authority
    context_object_name = 'local_authority_list'
    template_name = 'admission/local_authority_list.html'


# Placement Home


class CareHomeCreateView (LoginRequiredMixin, CreateView):
    model = Care_House_Information
    form_class = Care_House_InfomationForm
    template_name = 'admission/new_care_home.html'


class CareHomeUpdateView (LoginRequiredMixin, UpdateView):
    model = Care_House_Information
    form_class = Care_House_InfomationForm
    template_name = 'admission/new_care_home.html'


class CareHomeDetailView (LoginRequiredMixin, DetailView):
    model = Care_House_Information
    template_name = 'admission/home_details.html'


class CareHomeListView (LoginRequiredMixin, ListView):
    model = Care_House_Information
    context_object_name = 'home_list_info'
    template_name = 'admission/home_list.html'


# Contact and Social

class Contact_SocialDetailsView (DetailView):
    model = YP_Contact_Info


class Contact_SocialUpdateView (LoginRequiredMixin, UpdateView):
    model = YP_Contact_Info
    form_class = Contact_Social_DetailsForm


# Physical Description


class PhysicalDetailView (DetailView):
    model = YP_Physical_Description


class PhysicalUpdateView (LoginRequiredMixin, UpdateView):
    model = YP_Physical_Description
    form_class = YP_Physical_DescriptionForm


class HealthDetailView (DetailView):
    model = YP_Health_And_Wellness

    def test_func(self):
        obj = self.get_object ()
        return obj.yp_id == self.request.pk


class HealthUpdateView (LoginRequiredMixin, UpdateView):
    model = YP_Health_And_Wellness
    form_class = YP_Health_And_WellnessForm


# The code below is going to handle the banking details

class BankDetailView (DetailView):
    model = YP_Banking_Information


class BankUpdateView (LoginRequiredMixin, UpdateView):
    model = YP_Banking_Information
    form_class = YP_Banking_InformationForm


class YP_Pen_PicDetailsView (DetailView):
    model = YP_Pen_Pic


class YP_Pen_PicUpdateView (LoginRequiredMixin, UpdateView):
    model = YP_Pen_Pic
    form_class = YP_Pen_PicForm


class YP_Profile_ChildDetailsView (DetailView):
    model = YP_Profile_Child


class YP_Profile_ChildUpdateView (LoginRequiredMixin, UpdateView):
    model = YP_Profile_Child
    form_class = YP_Profile_ChildForm


class YP_Relationships_AssociatesDetailsView (DetailView):
    model = YP_Relationships_Associates


class YP_Relationships_AssociatesUpdateView (LoginRequiredMixin, UpdateView):
    model = YP_Relationships_Associates
    form_class = YP_Relationships_AssociatesForm


# The code below is going to handle the IPA table for the view


class IPADetailView (DetailView):
    model = YP_IPA
    template_name = 'admission/yp_initial_ipa.html'


class IPAListView (ListView, ):
    model = YP_IPA
    template_name = 'admission/yp_ipa_list.html'
    context_object_name = 'ipa_posts'
    ordering = ['-yp_date_added']

    def get_queryset(self):
        return YP_IPA.objects.filter (yp=self.request.resolver_match.kwargs['pk'])


class IPAUpdateView (LoginRequiredMixin, UpdateView):
    model = YP_IPA
    form_class = YP_IPAForm


class IPACreateView (LoginRequiredMixin, CreateView):
    model = YP_IPA
    form_class = YP_IPAForm

    # In the function below we are passing two kwargs , for both the user and the young person


class PicUpdateView (LoginRequiredMixin, UpdateView):
    model = Profile_Pic
    form_class = Profile_PicUpdateForm
    template_name = 'admission/pic_update.html'
