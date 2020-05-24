from django.db.models import Q
from django.template.defaultfilters import slugify
from djongo import models
from tinymce.models import HTMLField


# Create your models here.


class IndeedCategoriesManager(models.Manager):

    def get_queryset_sales(self):
        return super().get_queryset().filter(
            Q(title__icontains='Sales') | Q(title__icontains='Marketing') | Q(
                title__icontains='Business Development') | Q(title__icontains='BDE') | Q(title__icontains='BDM'))

    def get_queryset_back_office(self):
        return super().get_queryset().filter(
            Q(title__icontains='Back Office') | Q(title__icontains='Admin') | Q(title__icontains='Front Office'))

    def get_queryset_purchase_store(self):
        return super().get_queryset().filter(
            Q(title__icontains='Purchase') | Q(title__icontains='Store') | Q(title__icontains='Supply Chain') | Q(
                title__icontains='Material Management'))

    def get_queryset_account_finance(self):
        return super().get_queryset().filter(
            Q(title__icontains='account') | Q(title__icontains='finance') | Q(title__icontains='Tally') | Q(
                title__icontains='accountant'))

    def get_queryset_software_hardware(self):
        return super().get_queryset().filter(
            Q(title__icontains='Developer') | Q(title__icontains='Software') | Q(title__icontains='Hardware') | Q(
                title__icontains='Network'))

    def get_queryset_graphic_digital(self):
        return super().get_queryset().filter(
            Q(title__icontains='Web') | Q(title__icontains='Graphic') | Q(title__icontains='SEO') | Q(
                title__icontains='Digital Marketing') | Q(title__icontains='Social Media') | Q(
                title__icontains='PhotoShop') | Q(title__icontains='Coral Draw') | Q(title__icontains='Illustrator'))

    def get_queryset_bpo_ites(self):
        return super().get_queryset().filter(
            Q(title__icontains='bpo') | Q(title__icontains='customer care') | Q(title__icontains='tele caller') | Q(
                title__icontains='Customer care') | Q(title__icontains='call center') | Q(
                title__icontains='International call center') | Q(title__icontains='non voice') | Q(
                title__icontains='voice'))

    def get_queryset_engineering_manufacturing(self):
        return super().get_queryset().filter(
            Q(title__icontains='Production') | Q(title__icontains='Maintenance')  | Q(
                title__icontains='CNC') | Q(title__icontains='Packaging') | Q(
                title__icontains='Shift') | Q(title__icontains='Manufacturing') | Q(
                title__icontains='Engineering'))


class IndeedJobsManager(models.Manager):

    def get_queryset_ahm(self):
        return super().get_queryset().filter(city__icontains='Ahmedabad')

    def get_queryset_vadodara(self):
        return super().get_queryset().filter(city__icontains='Vadodara')

    def get_queryset_surat(self):
        return super().get_queryset().filter(city__icontains='Surat')

    def get_queryset_rajkot(self):
        return super().get_queryset().filter(city__icontains='Rajkot')

    def get_queryset_bharuch(self):
        return super().get_queryset().filter(city__icontains='Bharuch')

    def get_queryset_ankleshwar(self):
        return super().get_queryset().filter(city__icontains='Ankleshwar')

    def get_queryset_vapi(self):
        return super().get_queryset().filter(city__icontains='Vapi')

    def get_queryset_gandhinagar(self):
        return super().get_queryset().filter(city__icontains='Gandhinagar')


class IndeedJobs(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    salary = models.CharField(max_length=200, null=True, blank=True)
    # experience = models.CharField(max_length=100, null=True, blank=True)
    job_description = HTMLField(null=True, blank=True)
    employment_type = models.CharField(max_length=100, null=True, blank=True)
    date_posted = models.CharField(max_length=200, null=True, blank=True)
    job_url = models.URLField(max_length=1000, unique=True, null=True, blank=True)
    pub_date = models.DateTimeField(null=True, auto_created=True, auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_created=True)

    objects = models.Manager()
    job_objects = IndeedJobsManager()
    categories_objects = IndeedCategoriesManager()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return str(self.title)

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while IndeedJobs.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', args=[str(self.slug, )])
