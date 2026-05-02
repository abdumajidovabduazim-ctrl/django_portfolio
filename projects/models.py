from django.db import models


class Project(models.Model):
    # Loyiha nomi
    title = models.CharField(max_length=200)

    # Qisqa tavsif (kartochkada ko'rinadi)
    short_description = models.TextField()

    # To'liq tavsif
    description = models.TextField()

    # Loyiha rasmi
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    # GitHub linki
    github_url = models.URLField(blank=True)

    # Demo linki (ixtiyoriy)
    live_url = models.URLField(blank=True)

    # Texnologiyalar (Python, Django, PostgreSQL...)
    technologies = models.CharField(max_length=300)

    # Yaratilgan sana (avtomatik)
    created_at = models.DateTimeField(auto_now_add=True)

    # Tartib raqami
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']  # order bo'yicha saralaydi

    def __str__(self):
        return self.title  # Admin'da nomi ko'rinadi