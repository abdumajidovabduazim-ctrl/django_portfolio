from django.db import models

class Category(models.Model):
    # Blog kategoriyasi (Python, Django, Linux...)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)  # URL uchun: /blog/python/

    def __str__(self):
        return self.name

class Post(models.Model):
    # Sarlavha
    title = models.CharField(max_length=300)

    # URL uchun: /blog/mening-postim/
    slug = models.SlugField(unique=True)

    # Kategoriya (o'chirilsa post qoladi)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # Qisqa tavsif (ro'yxatda ko'rinadi)
    excerpt = models.TextField()

    # To'liq matn
    content = models.TextField()

    # Muqova rasmi
    image = models.ImageField(upload_to='blog/', blank=True, null=True)

    # Nashr etilganmi?
    is_published = models.BooleanField(default=False)

    # Sana (avtomatik)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # Yangilari birinchi

    def __str__(self):
        return self.title