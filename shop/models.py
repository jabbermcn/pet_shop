from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='название',
        help_text='Макс. 24 символа'
    )
    descr = models.CharField(
        max_length=140,
        blank=True,
        null=True,
        verbose_name='описание',
        help_text='Макс. 140 символов'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    title = models.CharField(
        max_length=36,
        verbose_name='название',
        help_text='Макс. 36 символов'
    )
    descr = models.CharField(
        max_length=140,
        null=True,
        blank=True,
        verbose_name='описание',
        help_text='Макс. 140 символов'
    )
    article = models.CharField(
        max_length=16,
        unique=True,
        verbose_name='Артикль',
        help_text='Макс. 16 символов'
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        default=0,
        verbose_name='цена',
        help_text='Макс. 999999.99'
    )
    count = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='количество'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name='категория'
    )
    image = models.ImageField(
        upload_to='products/',
        verbose_name='картинка',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'shop_products'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('price', 'title', 'article')
