from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import F
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Notes, Parent_Notes
from .forms import NotesForm, Parent_NotesForm
from admission.views import YP_General_Information
from .filters import YP_Notes_Month_Filter, Child_Notes_Month_Filter
from django.template.loader import render_to_string
from django.http import HttpResponse, Http404, HttpResponseRedirect
from weasyprint import HTML
import tempfile
import datetime


def home(request):
    context = {
        'notes': Notes.objects.all ()
    }
    return render (request, 'notes/home.html', context)


class NotesListView (LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'notes/notes_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'notes'
    ordering = ['-date_added']

    def get_queryset(self):
        filtered_results = Notes.objects.filter (yp=self.request.resolver_match.kwargs['pk']).order_by ('-date_added')
        return filtered_results

    def user_count(self):
        get_yp_name = YP_General_Information.objects.get (id=self.request.resolver_match.kwargs['pk'])
        return get_yp_name


class UserPostListView (LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'notes/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'notes'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404 (User, username=self.kwargs.get ('username'))
        return Notes.objects.filter (author=user).order_by ('-date_posted')


class NotesDetailView (LoginRequiredMixin, DetailView):
    model = Notes
    template_name = 'notes/notes_detail.html'


class NotesCreateView (LoginRequiredMixin, CreateView):
    model = Notes
    form_class = NotesForm
    template_name = 'notes/notes_create.html'
    Notes.objects.update(duration=F('time_end') - F('time_start'))

    def form_valid(self, form):
        form.instance.staff = self.request.user
        form.instance.yp_id = self.kwargs['pk']
        return super ().form_valid (form)


class NotesUpdateView (LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notes
    form_class = NotesForm
    template_name = 'notes/notes_update.html'

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super ().form_valid (form)

    def test_func(self):
        notes = self.get_object ()
        if self.request.user == notes.staff:
            return True
        return False


class NotesDeleteView (LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notes
    template_name = 'notes/notes_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        notes = self.get_object ()
        if self.request.user == notes.staff:
            return True
        return False


def about(request):
    return render (request, 'notes/about.html', {'title': 'About'})


def show_all_yp_page(request):
    if 'pdf_download' in request.GET:
        context = {}
        filtered_yp = YP_Notes_Month_Filter (request.GET, queryset=Notes.objects.all ())
        context['filtered_yp'] = filtered_yp

        response = HttpResponse (content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=filter' + \
                                          str (datetime.datetime.now ()) + '.pdf'
        response['Content-Transfer-Encoding'] = 'binary'

        html_string = render_to_string ('admission/pdf_notes_report.html', context, request)
        html = HTML (string=html_string)
        result = html.write_pdf ()

        with tempfile.NamedTemporaryFile (delete=True) as output:
            output.write (result)
            output.flush ()
            output.seek (0)
            # output = open(output.name, 'rb') they using this on a live server
            response.write (output.read ())

        return response

    else:
        context = {}

        filtered_yp = YP_Notes_Month_Filter (
            request.GET,
            queryset=Notes.objects.all ()
        )

        context['filtered_yp'] = filtered_yp

        return render (request, 'notes/notes_report.html', context=context)


def show_all_child_page(request, pk):
    if 'pdf_download' in request.GET:
        context = {}
        filtered_yp = Child_Notes_Month_Filter (request.GET, queryset=Notes.objects.filter (yp=pk))
        context['filtered_yp'] = filtered_yp

        response = HttpResponse (content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=filter' + \
                                          str (datetime.datetime.now ()) + '.pdf'
        response['Content-Transfer-Encoding'] = 'binary'

        html_string = render_to_string ('admission/pdf_notes_report.html', context, request)
        html = HTML (string=html_string)
        result = html.write_pdf ()

        with tempfile.NamedTemporaryFile (delete=True) as output:
            output.write (result)
            output.flush ()
            output.seek (0)
            # output = open(output.name, 'rb') they using this on a live server
            response.write (output.read ())

        return response

    else:
        context = {}

        filtered_yp = Child_Notes_Month_Filter (request.GET,
                                                queryset=Notes.objects.filter (yp=request.resolver_match.kwargs['pk']))

        context['filtered_yp'] = filtered_yp

        return render (request, 'notes/notes_report.html', context=context)

    # Parent Notes


class ParentNotesListView (LoginRequiredMixin, ListView):
    model = Parent_Notes
    template_name = 'notes/parent_notes_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'parent_notes'
    ordering = ['-date_added']

    def get_queryset(self):
        filtered_results = Parent_Notes.objects.filter(yp=self.request.resolver_match.kwargs['pk']).order_by('-date_added')
        return filtered_results

    def user_count(self):
        get_yp_name = YP_General_Information.objects.get(id=self.request.resolver_match.kwargs['pk'])
        return get_yp_name


class ParentNotesDetailView (LoginRequiredMixin, DetailView):
    model = Parent_Notes
    template_name = 'notes/parent_notes_detail.html'


class ParentNotesCreateView (LoginRequiredMixin, CreateView):
    model = Parent_Notes
    form_class = Parent_NotesForm
    template_name = 'notes/parent_notes_create.html'

    def form_valid(self, form):
        form.instance.staff = self.request.user
        form.instance.yp_id = self.kwargs['pk']
        return super().form_valid(form)


class ParentNotesUpdateView (LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Parent_Notes
    form_class = Parent_NotesForm
    template_name = 'notes/parent_notes_update.html'

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super().form_valid(form)

    def test_func(self):
        parent_notes = self.get_object()
        if self.request.user == parent_notes.staff:
            return True
        return False


class ParentNotesDeleteView (LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Parent_Notes
    template_name = 'notes/parent_notes_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        parent_notes = self.get_object()
        if self.request.user == parent_notes.staff:
            return True
        return False


