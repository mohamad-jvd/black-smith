from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from app_market.models import Product, Color, Brand, Banner, Image, Category, features, review, ProductDescription, special_feature, Blog, Blog_detail, SiteSettings


class ImageInline(GenericStackedInline):
    model = Image
    extra = 1

class special_featureInline(admin.StackedInline):
    model = special_feature
    extra = 1

class reviewInline(admin.StackedInline):
    model = review
    extra = 1

class ProductDescriptionInline(admin.StackedInline):
    model = ProductDescription
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline , reviewInline ,ProductDescriptionInline ]

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order', 'is_active')
    list_editable = ('display_order', 'is_active')
    search_fields = ('name',)
    ordering = ('display_order',)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
 
@admin.register(features)
class featuresAdmin(admin.ModelAdmin):
    pass

@admin.register(review)
class reviewAdmin(admin.ModelAdmin):
    inlines = [special_featureInline]
    pass

@admin.register(special_feature)
class special_featureAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductDescription)
class ProductDescriptionAdmin(admin.ModelAdmin):
    pass

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    pass

@admin.register(Blog_detail)
class Blog_detailAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    pass

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    fieldsets = (
        ('بنرهای بالایی سایت', {
            'fields': (
                ('top_banner_1', 'top_banner_1_category_num'),
                ('top_banner_2', 'top_banner_2_category_num'),
            )
        }),

        ('پیشنهاد لحظه‌ای', {
            'fields': ('instant_suggestion',)
        }),

        ('بنرهای پرفروش‌ترین‌ها', {
            'fields': (
                ('bestseller_banner_1', 'bestseller_banner_1_category_num'),
                ('bestseller_banner_2', 'bestseller_banner_2_category_num'),
            )
        }),

        ('پیشنهاد شگفت‌انگیز', {
            'fields': ('special_offer',)
        }),

        ('بنرهای دسته‌بندی', {
            'fields': (
                ('category_banner_1', 'category_banner_1_category_num'),
                ('category_banner_2', 'category_banner_2_category_num'),
                ('category_banner_3', 'category_banner_3_category_num'),
                ('category_banner_4', 'category_banner_4_category_num'),
            )
        }),

        ('بنر پایینی سایت', {
            'fields': (
                ('bottom_banner', 'bottom_banner_category_num'),
            )
        }),

        ('هویت بصری سایت', {
            'fields': ('logo', 'favicon')
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False