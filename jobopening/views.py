from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import JobOpening
# Create your views here.
from django.views.generic import ListView, DetailView

from django.views.generic import CreateView


class JobOpeningView(ListView):
    model = JobOpening
    template_name = 'sampledjango/jobopening_list.html'
    context_object_name = 'jobopening'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobOpeningView, self).get_context_data()
        return context


class JobOpeningDetailView(DetailView):
    model = JobOpening
    template_name = 'sampledjango/jobopening_detail.html'

