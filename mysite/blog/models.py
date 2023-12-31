from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    """ модель постов блога """
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)     # SlugField по умолчанию подразумевают индекс
    # many-to-one relationship (several posts can be writen by one author/user)
    author = models.ForeignKey(User,               # поля типа ForeignKey по умолчанию подразумевают индекс
                               on_delete=models.CASCADE,    # on delete User - delete all his posts
                               related_name='blog_posts')   # имя обратной связи, от User к Post (user.blog_posts)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)


    class Meta:
        # Отображать посты блога в обратном порядке
        ordering = ['-publish']
        # определить индекс БД по полю publish (можно указать несколько полей)
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title