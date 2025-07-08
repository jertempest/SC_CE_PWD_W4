from django.db import models

class Post(models.Model):
    """
    Represents a blog post
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        """
        sort by the 'created' field. The '-' prefix
        specifies to order in descending/reverse order. Otherwise, it will be in ascending order.
        """
        ordering = ['-created']
    def __str__(self):
        return self.title
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.Protect,
        related_name = 'blog_posts',
        null = True
    )
    