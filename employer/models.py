from django.db import models


# Create your models here.
from django.urls import reverse
from django.template.defaultfilters import slugify


class CompanyProfile(models.Model):
    company = models.CharField(max_length=50)
    slug = models.SlugField(max_length=40)
    company_profile = models.TextField()
    company_location = models.CharField(max_length=50)
    company_website = models.URLField(verbose_name='Website', default=None)
    founded_year = models.PositiveIntegerField(null=True, blank=True)
    total_employees = models.PositiveIntegerField(null=True, blank=True)
    company_review = models.DecimalField(decimal_places=1, max_digits=2, null=True, blank=True,
                                         help_text="Rate Company Out Of Five")
    company_date_created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.company

    def save(self, *args, **kwargs):
        self.slug_field = slugify(self.company)
        super(CompanyProfile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'slug': self.slug})
