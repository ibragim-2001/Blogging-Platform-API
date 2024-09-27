from django.db import models


class Post(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255)
    content = models.TextField(verbose_name='Content')
    create_at = models.DateTimeField(verbose_name='Date create', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='Date update', auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField('Tags', related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category's"

    def __str__(self):
        return self.title


class Tags(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title