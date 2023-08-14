from django.shortcuts import render
from django.http import HttpRequest
from site_module.models import Slider, SiteSetting
from blog_module.models import Blog, BlogCategory
from product_module.models import ProductType, ProductCategory, Product
from comment_module.models import Comment
from django.contrib.auth import get_user_model
from account_module.models import User
from tools._main_service import div_products
from tools.comment_star import to_star

# Create your views here.

def main_page(request: HttpRequest):
    sliders: Slider = Slider.objects.filter(is_active=True).all()
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    blogs: Blog = list(Blog.objects.filter(is_active=True).all())[-1:-5:-1]
    product_type: ProductType = ProductType.objects.filter(is_active=True).all()
    comments: Comment = Comment.objects.filter(is_star=True, is_accepted=True, commentposition=Comment.CommentPosition.main_page).all()
    admin: User = get_user_model().objects.get(user_group=get_user_model().UserGroup.admin)
    best_products: Product = list(Product.objects.order_by('price').filter(count__gt=0).all())[-1:-6:-1]
    best_products = div_products(best_products, size=4)
    return render(request, r'home_module/index.html', context={
        'sliders': sliders,
        'setting': setting,
        'blogs': blogs,
        'admin': admin,
        'product_type': product_type,
        'comments': comments,
        'best_products': best_products
    })


def header(request: HttpRequest):
    return render(request, r'shared/header.html', context={})

    
def footer(request: HttpRequest):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    return render(request, r'shared/footer.html', context={
        'setting': setting
    })

