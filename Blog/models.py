import uuid
from datetime import datetime

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

from Blog.fields import WEBPField
from accounts.models import CustomUser


def image_folder():
    return f'posts/title_images/{datetime.now().strftime("%Y/%m/%d")}/{uuid.uuid4().hex}.webp'


def validate_image(image):
    filesize = image.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))


class Post(models.Model):
    class PostStatus(models.TextChoices):
        PUBLIC = 'PUB', _('Published')
        PRIVATE = 'PRI', _('Private')

    title = models.CharField(max_length=200, unique=True, null=False)
    title_image = WEBPField(upload_to=image_folder, validators=[validate_image], default='posts/home-bg.webp',
                            null=False, verbose_name="Image")
    slug = models.SlugField(max_length=200, unique=True, null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    description = models.TextField(max_length=1000)
    content = HTMLField()

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
