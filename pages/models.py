from django.db import models


class CategoryModel(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class ImagesModel(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="image")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"


class FoodsModel(models.Model):
    photo = models.ImageField(upload_to="food")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.photo

    class Meta:
        verbose_name = "food"
        verbose_name_plural = "foods"


class ProductsModel(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    short_description = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="product")

    categories = models.ManyToManyField(CategoryModel, related_name="product")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"


class BookingModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "booking"
