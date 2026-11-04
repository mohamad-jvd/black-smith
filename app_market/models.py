from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse

User = get_user_model()

class Product(models.Model):
    name_fa = models.CharField(max_length=255, null=True)
    name_en = models.CharField(max_length=255, null=True)
    price = models.PositiveIntegerField()
    discount = models.IntegerField(default=0)
    count = models.PositiveIntegerField()
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    is_suggested = models.BooleanField(default=False)
    is_amazing = models.BooleanField(default=False)
    footer_right = models.BooleanField(default=False)
    footer_left = models.BooleanField(default=False)
    footer_Middle = models.BooleanField(default=False)
    Category = models.ManyToManyField('Category')
    color = models.ManyToManyField('color')
    features = models.ManyToManyField('features')

    @property
    def images(self):
        return Image.objects.filter(
            object_id=self.id,
            content_type=ContentType.objects.get_for_model(self.__class__).id
        )

    def get_absolute_url(self):
        return reverse('app_market:product_detail', args=(self.id, ))

    def discounted_price(self):
        if self.discount > 0:
            return self.price - (self.price * self.discount // 100)
        return self.price
    
    def __str__(self):
        return self.name_fa or ''

class Color(models.Model):
    color = models.CharField(max_length=255)
    hex_code = models.CharField(max_length=35,null=True)

    def __str__(self):
        return self.color

class Brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='brands/',
        null=True,
        blank=True,
        help_text='ابعاد پیشنهادی لوگو: 205 × 205 پیکسل'
    )
    website_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name='آدرس سایت برند'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='نمایش در سایت'
    )
    display_order = models.PositiveIntegerField(
        default=0,
        verbose_name='ترتیب نمایش'
    )

    class Meta:
        ordering = ['display_order', 'id']
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'

    def __str__(self):
        return self.name
    
class Banner(models.Model):
    title = models.CharField(max_length=255)


    @property
    def images(self):
        return Image.objects.filter(
            object_id=self.id,
            content_type=ContentType.objects.get_for_model(self.__class__).id
        )

    def __str__(self):
        return self.title

class SiteSettings(models.Model):

    top_banner_1 = models.ImageField(
        upload_to='site/',
        null=True,
        blank=True,
        verbose_name='بنر بالایی سمت چپ',
        help_text='ابعاد پیشنهادی: 856 × 428 پیکسل'
    )
    top_banner_1_category_num = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='شماره دسته‌بندی بنر بالایی سمت چپ'
    )

    top_banner_2 = models.ImageField(
        upload_to='site/',
        null=True,
        blank=True,
        verbose_name='بنر پایینی سمت چپ',
        help_text='ابعاد پیشنهادی: 856 × 428 پیکسل'
    )
    top_banner_2_category_num = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='شماره دسته‌بندی بنر پایینی سمت چپ'
    )

    instant_suggestion = models.ImageField(
        upload_to='site/',
        null=True,
        blank=True,
        verbose_name='پیشنهاد لحظه‌ای',
        help_text='ابعاد پیشنهادی: 1920 × 229 پیکسل'
    )

    bestseller_banner_1 = models.ImageField(
        upload_to='site/',
        null=True,
        blank=True,
        verbose_name='بنر سمت راست پرفروش‌ترین‌ها',
        help_text='ابعاد پیشنهادی: 820 × 300 پیکسل'
    )
    bestseller_banner_1_category_num = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='شماره دسته‌بندی بنر سمت راست پرفروش‌ترین‌ها'
    )

    bestseller_banner_2 = models.ImageField(
        upload_to='site/',
        null=True,
        blank=True,
        verbose_name='بنر سمت چپ پرفروش‌ترین‌ها',
        help_text='ابعاد پیشنهادی: 820 × 300 پیکسل'
    )
    bestseller_banner_2_category_num = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='شماره دسته‌بندی بنر سمت چپ پرفروش‌ترین‌ها'
    )

    special_offer = models.ImageField(
        upload_to='site/',
        null=True,
        blank=True,
        verbose_name='پیشنهاد شگفت‌انگیز',
        help_text='ابعاد پیشنهادی: 495 × 864 پیکسل'
    )

    category_banner_1 = models.ImageField(
        upload_to='site/',
        null=True,
        blank=True,
        verbose_name='تصویر اول زیر پیشنهاد شگفت‌انگیز',
        help_text='ابعاد پیشنهادی: 400 × 300 پیکسل'
    )
    category_banner_1_category_num = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='شماره دسته‌بندی تصویر اول'
    )

    category_banner_2 = models.ImageField(
        upload_to='site/',
        null=True,
        blank=True,
        verbose_name='تصویر دوم زیر پیشنهاد شگفت‌انگیز',
        help_text='ابعاد پیشنهادی: 400 × 300 پیکسل'
    )
    category_banner_2_category_num = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='شماره دسته‌بندی تصویر دوم'
    )

    category_banner_3 = models.ImageField(
        upload_to='site/',
        null=True,
        blank=True,
        verbose_name='تصویر سوم زیر پیشنهاد شگفت‌انگیز',
        help_text='ابعاد پیشنهادی: 400 × 300 پیکسل'
    )
    category_banner_3_category_num = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='شماره دسته‌بندی تصویر سوم'
    )

    category_banner_4 = models.ImageField(
        upload_to='site/',
        null=True,
        blank=True,
        verbose_name='تصویر چهارم زیر پیشنهاد شگفت‌انگیز',
        help_text='ابعاد پیشنهادی: 400 × 300 پیکسل'
    )
    category_banner_4_category_num = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='شماره دسته‌بندی تصویر چهارم'
    )

    bottom_banner = models.ImageField(
        upload_to='site/',
        null=True,
        blank=True,
        verbose_name='بنر پایینی سایت',
        help_text='ابعاد پیشنهادی: 1920 × 244 پیکسل'
    )
    bottom_banner_category_num = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='شماره دسته‌بندی بنر پایینی سایت'
    )

    logo = models.ImageField(
        upload_to='site/',
        null=True,
        blank=True,
        verbose_name='لوگوی سایت',
        help_text='ابعاد پیشنهادی: 128 × 36 پیکسل'
    )

    favicon = models.ImageField(
        upload_to='site/',
        null=True,
        blank=True,
        verbose_name='فاوآیکون سایت',
        help_text='ابعاد پیشنهادی: 32 × 32 پیکسل، فرمت PNG یا ICO'
    )

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return 'تنظیمات Black Smith'

class Category(models.Model):
    parent = models.ForeignKey( 'self', related_name='sub_categories', on_delete=models.SET_NULL, null=True, blank=True )
    name = models.CharField(max_length=50 , null=True)
    slug = models.SlugField(max_length=50 , null=True , blank=True)
    is_available = models.BooleanField(default= True)

    def __str__(self):
        return self.name
    
class features(models.Model):
    text = models.CharField(max_length=255)
    answer = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.text
    
class review(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review' , null=True)
    description = models.TextField(blank=True , null=True)

class special_feature(models.Model):
    text = models.CharField(max_length=255,null=True)
    main_text = models.TextField(null=True)
    review = models.ForeignKey("review", on_delete=models.CASCADE , related_name='feature' , null=True)

    def __str__(self):
        return self.text

class ProductDescription(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='descriptions')
    title = models.CharField(max_length=100 , blank=True , null=True)
    description = models.TextField( blank=True , null=True )

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=255)

    @property
    def images(self):
        return Image.objects.filter(
            object_id=self.id,
            content_type=ContentType.objects.get_for_model(self.__class__).id
        )

    def __str__(self):
        return self.title
    
class Blog_detail(models.Model):
    title = models.CharField( max_length=150 , blank=True , null=True)
    description= models.TextField()

    @property
    def images(self):
        return Image.objects.filter(
            object_id=self.id,
            content_type=ContentType.objects.get_for_model(self.__class__).id
        )

    def __str__(self):
        return self.title
    
class Image(models.Model):
    url = models.CharField(max_length=150, null=True, blank=True)
    Category_num = models.IntegerField(null=True , blank=True)
    image = models.ImageField(upload_to='store/images/', null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, related_name='app_market_images')
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.image.url
    
