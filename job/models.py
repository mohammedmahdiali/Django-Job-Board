from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

def image_upload(object, filename):
    image_name, ext = filename.split(".")
    return f"jobs/{object.id}.{ext}"

def cv_upload(object, filename):
    cv_name, ext = filename.split(".")
    return f"apply/{cv_name}.{ext}"

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ("FT", "Full-Time"),
        ("PT", "Part-Time")
    ]

    owner = models.ForeignKey(User, related_name="job_owner", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES)
    description = models.TextField(max_length=500)
    published_at = models.DateField()
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Apply(models.Model):
    job_id = models.ForeignKey(Job, related_name="apply_job", on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    cv = models.FileField(upload_to=cv_upload)
    website = models.URLField()
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.email
