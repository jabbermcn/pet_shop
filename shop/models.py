from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='name',
        help_text='max. 24 symbols'
    )
    descr = models.CharField(
        max_length=140,
        blank=True,
        null=True,
        verbose_name='description',
        help_text='max. 140 symbols'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('name',)


class Product(models.Model):
    title = models.CharField(
        max_length=36,
        verbose_name='title',
        help_text='max. 36 symbols'
    )
    descr = models.CharField(
        max_length=140,
        null=True,
        blank=True,
        verbose_name='description',
        help_text='max. 140 symbols'
    )
    article = models.CharField(
        max_length=16,
        unique=True,
        verbose_name='article',
        help_text='max. 16 symbols'
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        default=0,
        verbose_name='price',
        help_text='max. 999999.99'
    )
    currency = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name='currency',
        help_text='max. 4 symbols'
    )
    weight = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        default=0,
        verbose_name='weight',
        help_text='min. 0.1'
    )
    count = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='count'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name='category'
    )
    image = models.ImageField(
        upload_to='products/',
        verbose_name='image',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'shop_products'
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('price', 'title', 'article')


class Professional(models.Model):
    first_name = models.CharField(
        max_length=24,
        verbose_name='first_name',
        help_text='max. 24 symbols'
    )
    last_name = models.CharField(
        max_length=24,
        verbose_name='last_name',
        help_text='max. 24 symbols'
    )
    image = models.ImageField(
        upload_to='professionals/',
        verbose_name='image',
        null=True,
        blank=True
    )
    linkedin = models.URLField(
        blank=True
    )
    facebook = models.URLField(
        blank=True
    )
    twitter = models.URLField(
        blank=True
    )
    descr = models.CharField(
        max_length=140,
        blank=True,
        null=True,
        verbose_name='description',
        help_text='max. 140 symbols'
    )

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'shop_professional'
        verbose_name = 'professional'
        verbose_name_plural = 'professionals'
        ordering = ('first_name', 'last_name')


class Client(models.Model):
    first_name = models.CharField(
        max_length=24,
        verbose_name='first_name',
        help_text='max. 24 symbols'
    )
    last_name = models.CharField(
        max_length=24,
        verbose_name='last_name',
        help_text='max. 24 symbols'
    )
    image = models.ImageField(
        upload_to='clients/',
        verbose_name='image',
        null=True,
        blank=True
    )
    descr = models.CharField(
        max_length=140,
        blank=True,
        null=True,
        verbose_name='description',
        help_text='max. 140 symbols'
    )

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'shop_client'
        verbose_name = 'client'
        verbose_name_plural = 'clients'
        ordering = ('first_name', 'last_name')
