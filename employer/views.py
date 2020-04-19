from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render, redirect

from .models import CompanyProfile
from jobopening.models import JobOpening


# Create your views here.

class EmployerPanelView(ListView):
    model = CompanyProfile
    template_name = 'employer/panel/used/dashboard.html'
    context_object_name = 'panel'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EmployerPanelView, self).get_context_data()
        context.update({
            'jobopening': JobOpening.objects.all(),
        })
        return context


class EmployerJobListView(ListView):
    model = JobOpening
    template_name = 'employer/panel/used/manage-jobs.html'
    context_object_name = 'joblist'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EmployerJobListView, self).get_context_data()
        context.update({
            'company': CompanyProfile.objects.all(),
        })
        return context


def post_jobs(request):
    if request.method == 'POST':
        jobtitle = request.POST.get('jobtitle')
        jobslug = request.POST.get('jobslug')
        jobcat = request.POST.get('jobcat')
        companyname = request.POST.get('companyname')
        joblocation = request.POST.get('joblocation')

        b = JobOpening(job_title=jobtitle, slug=jobslug, industry=jobcat,
                       company_name=companyname, job_location=joblocation)
        b.save()
        return redirect('manage-jobs')

    return render(request, 'employer/panel/used/post-job.html')
