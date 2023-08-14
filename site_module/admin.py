from django.contrib import admin
from .models import Slider, SiteBanner, SiteSetting, QuestionAnswer, Visit

# Register your models here.

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']



@admin.register(SiteBanner)
class SiteBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_on_banner', 'position', 'is_active']



@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_main_setting']



@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ['question']



@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['user', 'ip', 'product_or_blog']


