from django.db import models


class User(models.Model):
    # Пользователь
    name = models.CharField('Имя', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Category(models.Model):
    # Категории
    name = models.CharField('Название', max_length=70)
    url = models.SlugField(max_length=120, unique=True)
    img = models.ImageField('Картинка', upload_to='photo_category/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    # Разные товары
    title = models.CharField('Название', max_length=70)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    poster = models.ImageField('Постер', upload_to='user_product/')
    draft = models.BooleanField('В наличии', default=False)
    url = models.SlugField(max_length=150, unique=True)
    category = models.ForeignKey(
        Category, verbose_name='Категории', on_delete=models.SET_NULL, null=True)
    users = models.ManyToManyField(User, verbose_name='Пользователи', related_name='product_user')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Comments(models.Model):
    # Коментарий
    name = models.CharField('Имя', max_length=150)
    text = models.TextField('Коментарий', max_length=5000)
    email = models.EmailField()
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Родитель')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукты')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'