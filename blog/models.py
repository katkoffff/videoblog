from django.db import models
from django.contrib.auth.models import User

class VideoContent(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author_video')
    title = models.CharField('Название', max_length=30)
    description = models.TextField('Описание')
    createddate = models.DateTimeField(auto_now_add=True)
    content = models.ImageField('Картинка', upload_to='media/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Commentary(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author_commentary')
    video = models.ForeignKey(VideoContent, on_delete=models.CASCADE, verbose_name='video_commentary')
    content = models.TextField('Комментарий')
    parent = models.ForeignKey('self', verbose_name='parent', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.author} - {self.video}"

class Subscription(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author_subscription')
    video = models.ForeignKey(VideoContent, on_delete=models.CASCADE, verbose_name='video_subscription')
    subscription = models.BooleanField('Подписка', default=False)

    def __str__(self):
        return f"{self.author} : {self.video} - {self.subscription}"

class Disregard(models.Model):
    author = models.ForeignKey(User, related_name='author_disregard', on_delete=models.CASCADE, verbose_name='disregard_author')
    to_author = models.ForeignKey(User, related_name='to_author_disregard', on_delete=models.CASCADE, verbose_name='disregard_to_author')
    ban = models.BooleanField('Игнор', default=False)

    def __str__(self):
        return f"{self.author} : {self.to_author} - {self.ban}"

class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author_like')
    video = models.ForeignKey(VideoContent, on_delete=models.CASCADE, verbose_name='video_like', blank=True, null=True)
    commentary = models.ForeignKey(Commentary, on_delete=models.CASCADE, verbose_name='commentary_like', blank=True, null=True)
    like = models.IntegerField('Лайк', default=0)
    dislike = models.IntegerField('Дизлайк', default=0)

    def __str__(self):
        return f"{self.author} : {self.video} : {self.commentary} - {self.like} - {self.dislike}"
