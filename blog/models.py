from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title

def get_absolute_url(self):
    return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
    your_name = models.CharField(max_length=20)
    comment_text = models.TextField()
    body = models.ForeignKey('Post', on_delete=models.CASCADE)
     
    def __str__(self):
        return f"Comment by Name: {self.your_name}"
