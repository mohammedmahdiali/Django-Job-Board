from django.db import models

# Create your models here.

def image_upload(object, filename):
    image_name, ext = filename.split(".")
    return f"jobs/{object.id}.{ext}"

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ("FT", "Full-Time"),
        ("PT", "Part-Time")
    ]

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

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name