from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # User_id = models.ForeignKey('User')
    pub_date = models.DateTimeField(auto_now_add=True)
    pro = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    Board_id = models.ForeignKey('Board', on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    # User_id = models.ForeignKey('User')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]