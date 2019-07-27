from django.db import models
from django.urls import reverse


class Post(models.Model):
  """Model definition for Post."""

  title = models.CharField(max_length=200)
  author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
  )
  body = models.TextField()

  class Meta:
    """Meta definition for Post."""

    verbose_name = 'Post'
    verbose_name_plural = 'Posts'

  def __str__(self):
    """Unicode representation of Post."""
    return self.title
  
  def get_absolute_url(self):
    return reverse('post_detail', kwargs={'pk': self.pk})