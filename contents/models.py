from django.db import models

from user.models import User

class Content(models.Model):
    Item_ID = models.IntegerField()
    title = models.CharField(max_length=50)
    Netflix = models.IntegerField()
    Tving = models.IntegerField()
    Wavve = models.IntegerField()
    Watcha = models.IntegerField()

    def set_title(self, new_title):
        self.title = new_title
        self.save()

    def __str__(self):
        return self.title

class Rating(models.Model):
    content = models.ForeignKey('contents.Content', on_delete=models.CASCADE, related_name='rating')
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment_text = models.CharField(max_length=1000)
    comment_date = models.DateField(auto_now_add=True)
    comment_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['comment_updated']

#마이그레이션 필요
