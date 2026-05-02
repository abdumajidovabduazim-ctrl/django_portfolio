from django.db import models


class About(models.Model):
    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    photo = models.ImageField(upload_to='about/', blank=True, null=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)  # ← qo'shildi
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    telegram = models.URLField(blank=True)

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    LEVEL_CHOICES = [
        (1, 'Boshlang\'ich'),
        (2, 'O\'rta'),
        (3, 'Yaxshi'),
        (4, 'Professional'),
    ]
    name = models.CharField(max_length=100)
    level = models.IntegerField(choices=LEVEL_CHOICES, default=2)
    icon = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email}"