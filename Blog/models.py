from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser

class Post(models.Model):

    class PostStatus(models.TextChoices):
        PUBLIC = 'PUB', _('Published')
        PRIVATE = 'PRI', _('Private')

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=3,
        choices=PostStatus.choices,
        default=PostStatus.PUBLIC,
    )

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title


