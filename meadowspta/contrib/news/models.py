from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
from meadowspta.core.models import *
from meadowspta.contrib.system.models import sysvar

class News(ContentModel):
    teaser = models.CharField(max_length=255, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='images/news/posts')
    image_large = ImageSpecField(source='image', processors=[Thumbnail(620)], format='JPEG', options={'quality': 80})
    image_modal = ImageSpecField(source='image', processors=[Thumbnail(550)], format='JPEG', options={'quality': 80})
    image_medium = ImageSpecField(source='image', processors=[Thumbnail(140)], format='JPEG', options={'quality': 80})
    image_thumbnail = ImageSpecField(source='image', processors=[Thumbnail(100)], format='JPEG', options={'quality': 80})

    def __unicode__(self):
        return str(self.title)

    def get_absolute_url(self):
        """
        Get the canonical url.
        """
        return '/news/%s' % self.slug

    def is_featured(self):
        """
        Check if the post is featured.
        """
        if self.id == int(sysvar['news_featured_post']):
            return True
        else:
            return False

    def admin_image(self):
        """
        Image output for the admin list page.
        """
        return '<img src="%s">' % self.image_thumbnail.url

    admin_image.allow_tags = True;