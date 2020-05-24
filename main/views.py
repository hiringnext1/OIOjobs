from django.views.generic import ListView, DetailView
from django_filters.views import FilterView
from .filters import JobFilter
from .models import IndeedJobs
from jobopening.models import JobOpening
from django.core.paginator import Paginator
from django.core.paginator import Paginator


# Create your views here.

class HomeListView(FilterView):
    model = IndeedJobs
    template_name = 'new_theme/../templates/employer/panel/index.html'
    filterset_class = JobFilter
    context_object_name = 'indeed'
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeListView, self).get_context_data()
        context.update({
            'total_jobs': IndeedJobs.objects.all(),
            'total_companies': IndeedJobs.objects.values('company').distinct().count(),
            'feature_jobs': IndeedJobs.objects.all().distinct()[:10],
            'by_location': IndeedJobs.objects.filter(city__icontains=IndeedJobs.city),
            'filter': JobFilter(self.request.GET, queryset=self.get_queryset()),
            'jobs_ahm': IndeedJobs.job_objects.get_queryset_ahm().all(),
            'jobs_vadodara': IndeedJobs.job_objects.get_queryset_vadodara().all(),
            'jobs_bharuch': IndeedJobs.job_objects.get_queryset_bharuch().all(),
            'jobs_surat': IndeedJobs.job_objects.get_queryset_surat().all(),
            'jobs_by_sales': IndeedJobs.categories_objects.get_queryset_sales().all(),
            'jobs_by_backoffice': IndeedJobs.categories_objects.get_queryset_back_office().all(),
            'jobs_by_purchase_store': IndeedJobs.categories_objects.get_queryset_purchase_store().all(),
            'jobs_by_account_finance': IndeedJobs.categories_objects.get_queryset_account_finance().all(),
            'jobs_by_software_hardware': IndeedJobs.categories_objects.get_queryset_software_hardware().all(),
            'jobs_by_graphic_digital': IndeedJobs.categories_objects.get_queryset_graphic_digital().all(),
            'jobs_by_bpo_ites': IndeedJobs.categories_objects.get_queryset_bpo_ites().all(),
            'jobs_by_engg': IndeedJobs.categories_objects.get_queryset_engineering_manufacturing().all(),

        }
        )
        return context


class IndexView(FilterView):
    model = IndeedJobs
    template_name = 'sampledjango/indeedjobs_list.html'
    filterset_class = JobFilter
    context_object_name = 'indeed'
    paginate_by = 20
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context.update({
            'total_jobs': IndeedJobs.objects.all(),
            'jobopening': JobOpening.objects.all(),
            'filter': JobFilter(self.request.GET, queryset=self.get_queryset()),
        }
        )
        return context


class IndexDetailView(DetailView):
    model = IndeedJobs
    template_name = 'sampledjango/indeedjobs_detail.html'

    def get_context_data(self, **kwargs):
        context = super(IndexDetailView, self).get_context_data()
        context.update({

        })

        return context


class TestListView(FilterView):
    model = IndeedJobs
    template_name = 'test_page.html'
    filterset_class = JobFilter
    context_object_name = 'indeed_test'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TestListView, self).get_context_data()
        context.update({
            'total_jobs': IndeedJobs.objects.all(),
            'by_location': IndeedJobs.objects.filter(city__icontains=IndeedJobs.city),
            'filter': JobFilter(self.request.GET, queryset=self.get_queryset()),
        }
        )
        return context


class JobsByCategories(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_categories/jobs-by-categories.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsByCategories, self).get_context_data()
        context.update({
            'jobs_by_sales': IndeedJobs.categories_objects.get_queryset_sales().all(),
            'jobs_by_purchase_store': IndeedJobs.categories_objects.get_queryset_purchase_store().all(),
            'jobs_by_backoffice': IndeedJobs.categories_objects.get_queryset_back_office().all(),
            'jobs_by_account_finance': IndeedJobs.categories_objects.get_queryset_account_finance().all(),
            'jobs_by_software_hardware': IndeedJobs.categories_objects.get_queryset_software_hardware().all(),
            'jobs_by_graphic_digital': IndeedJobs.categories_objects.get_queryset_graphic_digital().all(),
            'jobs_by_bpo_ites': IndeedJobs.categories_objects.get_queryset_bpo_ites().all(),
            'jobs_by_engg': IndeedJobs.categories_objects.get_queryset_engineering_manufacturing().all(),
        })
        return context


class JobsByLocation(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_location/jobs-by-location.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsByLocation, self).get_context_data()
        context.update({
            'jobs_ahm': IndeedJobs.job_objects.get_queryset_ahm().all(),
            'jobs_vadodara': IndeedJobs.job_objects.get_queryset_vadodara().all(),
            'jobs_bharuch': IndeedJobs.job_objects.get_queryset_bharuch().all(),
            'jobs_surat': IndeedJobs.job_objects.get_queryset_surat().all(),
        })

        return context


class JobsByAhm(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_location/jobs-by-location-ahm.html'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsByAhm, self).get_context_data()
        context.update({
            'jobs_ahm': IndeedJobs.job_objects.get_queryset_ahm().all(),
        })

        return context


class JobsByVadodara(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_location/jobs-by-location-vadodara.html'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsByVadodara, self).get_context_data()
        context.update({
            'jobs_vadodara': IndeedJobs.job_objects.get_queryset_vadodara().all(),
        })

        return context


class JobsByBharuch(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_location/jobs-by-location-bharuch.html'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsByBharuch, self).get_context_data()
        context.update({
            'jobs_bharuch': IndeedJobs.job_objects.get_queryset_bharuch().all(),
        })

        return context


class JobsBySurat(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_location/jobs-by-location-surat.html'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsBySurat, self).get_context_data()
        context.update({
            'jobs_surat': IndeedJobs.job_objects.get_queryset_surat().all(),
        })

        return context


class JobsBySales(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_categories/jobs-by-categories-sales.html'
    context_object_name = 'jobs_by_sales'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsBySales, self).get_context_data(**kwargs)
        context.update({
            'jobs_by_sales': IndeedJobs.categories_objects.get_queryset_sales().all(),
        })

        return context


class JobsByBackOffice(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_categories/jobs-by-categories-back-office.html'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsByBackOffice, self).get_context_data(**kwargs)
        context.update({
            'jobs_by_backoffice': IndeedJobs.categories_objects.get_queryset_back_office().all(),
        })

        return context


class JobsByPurchaseStore(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_categories/jobs-by-categories-purchase-store.html'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsByPurchaseStore, self).get_context_data(**kwargs)
        context.update({
            'jobs_by_purchase_store': IndeedJobs.categories_objects.get_queryset_purchase_store().all(),
        })

        return context


class JobsByAccountFinance(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_categories/jobs-by-categories-account-finance.html'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsByAccountFinance, self).get_context_data(**kwargs)
        context.update({
            'jobs_by_account_finance': IndeedJobs.categories_objects.get_queryset_account_finance().all(),
        })

        return context


class JobsBySoftwareHardware(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_categories/jobs-by-categories-software-hardware.html'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsBySoftwareHardware, self).get_context_data(**kwargs)
        context.update({
            'jobs_by_software_hardware': IndeedJobs.categories_objects.get_queryset_software_hardware().all(),
        })
        return context


class JobsByGraphicDigital(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_categories/jobs-by-categories-graphic-digital.html'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsByGraphicDigital, self).get_context_data(**kwargs)
        context.update({
            'jobs_by_graphic_digital': IndeedJobs.categories_objects.get_queryset_graphic_digital().all(),
        })
        return context


class JobsByBPOITES(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_categories/jobs-by-categories-bpo-ites.html'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsByBPOITES, self).get_context_data(**kwargs)
        context.update({
            'jobs_by_bpo_ites': IndeedJobs.categories_objects.get_queryset_bpo_ites().all(),
        })
        return context


class JobsByEngineering(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_categories/jobs-by-categories-engineering.html'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsByEngineering, self).get_context_data(**kwargs)
        context.update({
            'jobs_by_engg': IndeedJobs.categories_objects.get_queryset_engineering_manufacturing().all(),
        })
        return context