from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Post(models.Model):
    title = models.CharField(
        max_length=24,
        verbose_name='title'
    )
    subtitle = models.CharField(
        max_length=24,
        verbose_name='subtitle'
    )
    image = models.ImageField(
        upload_to='posts/',
        verbose_name='image'
    )
    text = models.TextField(
        verbose_name='text'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='is published'
    )
    date_published = models.DateTimeField(
        default=now(),
        verbose_name='date published'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='author'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='URL'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail-post', kwargs={'post_slug': self.slug})

    class Meta:
        db_table = 'blog_posts'
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('date_published',)


class Contact(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='name'
    )
    email = models.CharField(
        max_length=24,
        verbose_name='email'
    )
    subject = models.CharField(
        max_length=512,
        verbose_name='subject'
    )
    message = models.CharField(
        max_length=512,
        verbose_name='message'
    )
    date_created = models.DateTimeField(
        default=now(),
        verbose_name='date created'
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'blog_contacts'
        verbose_name = 'subject'
        verbose_name_plural = 'subjects'
        ordering = ('date_created',)


class Email(models.Model):
    email = models.CharField(
        max_length=24,
        verbose_name='email'
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'blog_email'
        verbose_name = 'email'
        verbose_name_plural = 'emails'


class Comment(models.Model):
    email = models.CharField(
        max_length=24,
        null=True,
        blank=True,
        verbose_name='email'
    )
    post = models.ForeignKey(
        'Post',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='post'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='author'
    )
    # date_published = models.DateTimeField(
    #     default=now(),
    #     verbose_name='date published'
    # )
    message = models.CharField(
        max_length=512,
        verbose_name='message'
    )

    def __str__(self):
        return str(self.email)

    class Meta:
        db_table = 'blog_comments'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
