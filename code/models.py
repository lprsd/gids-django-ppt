from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    datetime = models.DateTimeField()

    class Meta:
        ordering = ('-datetime',)
    
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    text = models.TextField()
