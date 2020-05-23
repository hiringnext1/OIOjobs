"""scrapydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main.views import IndexView, IndexDetailView, HomeListView, TestListView, JobsByLocation, JobsByAhm, \
    JobsByVadodara, JobsByBharuch, JobsBySurat, JobsByCategories, JobsBySales, JobsByBackOffice, JobsByPurchaseStore
from jobopening.views import JobOpeningView, JobOpeningDetailView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', HomeListView.as_view(), name='homepage'),
                  path('test/', TestListView.as_view(), name='test_page'),
                  path('job/', IndexView.as_view(), name='joblist'),
                  path('job/<slug>/', IndexDetailView.as_view(), name='detail'),

                  path('jobs-by-location/', JobsByLocation.as_view(), name='jobs-by-location'),
                  path('jobs-by-categories/', JobsByCategories.as_view(), name='jobs-by-categories'),
                  path('jobs-in-ahmedabad', JobsByAhm.as_view(), name='jobs-in-ahmedabad'),
                  path('jobs-in-vadodara', JobsByVadodara.as_view(), name='jobs-in-vadodara'),
                  path('jobs-in-bharuch', JobsByBharuch.as_view(), name='jobs-in-bharuch'),
                  path('jobs-in-surat', JobsBySurat.as_view(), name='jobs-in-surat'),

                  # Categories

                  path('jobs-by-sales', JobsBySales.as_view(), name='jobs-by-sales'),
                  path('jobs-by-back-office', JobsByBackOffice.as_view(), name='jobs-by-back-office'),
                  path('jobs-by-purchase-store', JobsByPurchaseStore.as_view(), name='jobs-by-purchase-store'),

                  path(r'employer/', include('employer.urls')),

                  # not used
                  path('jobopening/', JobOpeningView.as_view(), name='job-list'),
                  path('jobopening/<slug>/', JobOpeningDetailView.as_view(), name='job-detail'),
                  # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')

                  path(r'tinymce/', include('tinymce.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
