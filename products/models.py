from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('name',)

    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique_with=['id'], always_update=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='product_images/')
    slug = AutoSlugField(populate_from='name', unique_with=['category', 'id'], always_update=True)
    brand = models.CharField(max_length=100, blank=True)
    material = models.CharField(max_length=100, blank=True)
    size_dimensions = models.CharField(max_length=100, blank=True)
    instrument_type = models.CharField(max_length=100, blank=True, null=True)
    quantity_in_stock = models.IntegerField(default=0, verbose_name="Quantity in Stock")
    is_top_product = models.BooleanField(default=False, verbose_name="Top Product")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        verbose_name=_("Discount Percentage"),
        help_text=_("Enter a number between 0 and 100.")
    )

    def __str__(self):
        return self.name

    @property
    def discounted_price(self):
        """
        Calculates the discounted price if a discount_percentage is set,
        otherwise, returns the original price.
        """
        if self.discount_percentage is not None and self.discount_percentage > 0:
            discount_amount = (Decimal(self.discount_percentage) / Decimal('100')) * self.price
            return (self.price - discount_amount).quantize(Decimal('0.01'))
        return self.price
