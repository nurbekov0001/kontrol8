from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxLengthValidator


CATEGORY_CHOICES = [('OTHER', 'other'), ('SAMSUNG', 'samsung'), ('ACER', 'acer'), ('IPHONE', 'iPhone')]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='название')
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, null=False, blank=False, default='other',
                                verbose_name="категория товара")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание товара")
    picture = models.ImageField(null=True, blank=True, verbose_name='Каринка', upload_to='user_pics')
# Create your models here.
    class Meta:
        db_table = 'Products'
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f'{self.name}:{self.category}  '



class Review (models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name="автор",
                              on_delete=models.CASCADE, related_name='author')
    product = models.ForeignKey('webapp.Product', related_name="product", on_delete=models.CASCADE)

    review = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Отзыв')
    appraisal = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(0)],
                                    verbose_name='отценка')
    moderated = models.BooleanField(null=False, blank=False, verbose_name='промоделирован ли')

    class Meta:
        db_table = 'Reviews'
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        return f'{self.id}. {self.author}:{self.product}{self.review} {self.appraisal}, {self.moderated} '

