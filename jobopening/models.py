from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse

from employer.models import CompanyProfile


class JobOpening(models.Model):
    job_title = models.CharField(max_length=50, verbose_name='Designation', editable=True, null=True)
    slug = models.SlugField(max_length=40, auto_created=True)
    company_name = models.CharField(max_length=50, verbose_name='Company Name', blank=True)
    job_location = models.CharField(max_length=50, verbose_name='Job Location', null=True, blank=True)
    experience = models.DecimalField(decimal_places=1, max_digits=5, null=True, verbose_name='Experience', blank=True)
    skill = models.CharField(max_length=100, verbose_name='Skills', blank=True)
    qualification = models.CharField(max_length=100, verbose_name='Qualification', blank=True)
    min_salary_budget = models.DecimalField(decimal_places=2, max_digits=10, null=True,
                                            verbose_name='Min. Salary Criteria',
                                            help_text='Mention Salary in Annual Packages only', blank=True)
    max_salary_budget = models.DecimalField(decimal_places=2, max_digits=10, null=True,
                                            verbose_name='Max. Salary Criteria',
                                            help_text='Mention Salary in Annual Packages only', blank=True)
    industry = models.CharField(max_length=15, null=True, blank=True)
    role_category = models.CharField(max_length=50, verbose_name='Role Category', blank=True)
    employment_type = models.CharField(max_length=100, verbose_name='Employment Type', blank=True)
    job_description = models.TextField(verbose_name='Job Summary', null=True, blank=True)
    job_objective = models.TextField(verbose_name='Job Objectives', null=True, blank=True)
    must_have_skills = models.TextField(verbose_name='Must Have Skills', null=True, blank=True)
    job_created = models.DateTimeField(auto_created=True, null=True, auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.job_title

    class Meta:
        ordering = ["-job_created"]

    def save(self, *args, **kwargs):
        if not self.slug and self.job_title:
            self.slug = slugify(self.job_title)
        super(JobOpening, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'slug': self.slug})

    def get_tag_url(self):
        return reverse("tagged", kwargs={"slug": self.slug})
