from django.conf import settings
from django.db import models

class Post(models.Model):
    """
    Represents a blog post
    """
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.PROTECT,
        related_name = 'blog_posts',
        null = True
    )
    
    status = models.CharField(
        max_length = 10,
        choices = STATUS_CHOICES,
        help_text = 'Set to "published" to make this post publicly visible',
    )
    
    class Meta:
        """
        sort by the 'created' field. The '-' prefix
        specifies to order in descending/reverse order. Otherwise, it will be in ascending order.
        """
        ordering = ['-created']
    
    def __str__(self):
        return self.title
    

    