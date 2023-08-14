from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Product, ProductCategory
from site_module.models import SiteBanner
from django.views import View
from django.views.generic.list import ListView
from comment_module.forms import CommentForm
from comment_module.models import Comment
from product_module.models import Product
from account_module.models import User
from order_module.models import Order, OrderDetail, OrderCheckOut
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def add_order(request: HttpRequest):
    product_id = request.GET

    if request.user.is_authenticated == True:
        if Product.objects.get(id=int(product_id.get('product_id'))).count == 0:
            return JsonResponse({
                'status': 'error',
                'icon': 'error',
                'text': 'محصول موجود نمی باشد',
            })
        else:
            
            new_order_or_get, created = Order.objects.get_or_create(user_id=request.user.id, is_paid=False)
            new_order_or_get.is_paid = False
            new_order_or_get.transportation = True
            if new_order_or_get.transportation == True: 
                new_order_or_get.shipping_price = 0
            else: 
                new_order_or_get.shipping_price == 30000
            new_order_or_get.save()

            new_check_out_or_get, created = OrderCheckOut.objects.get_or_create(user_id=request.user.id, order_id=new_order_or_get.id)
            new_check_out_or_get.save()

            new_order_detail_or_get, created = OrderDetail.objects.get_or_create(order_id=new_order_or_get.id, product_id=product_id.get('product_id'))
            current_product = Product.objects.get(id=new_order_detail_or_get.product.id)
            if new_order_detail_or_get.count > current_product.count and current_product == 0:
                return JsonResponse({
                    'status': 'warning',
                    'icon': 'warning',
                    'text': 'عدد سفارش بیشتر از حد مجاز است!'
                })
            elif current_product.count < 1:
                return JsonResponse({
                    'status': 'error_number',
                    'icon': 'error',
                    'text': 'محصول مورد نظر موجود نمیباشد'
                })
            else:
                new_order_detail_or_get.count += 1
                new_order_detail_or_get.final_price = new_order_detail_or_get.totale_price()
                current_product.count -= 1 
                current_product.save()
                new_order_detail_or_get.save()

                return JsonResponse({
                    'status': 'success',
                    'icon': 'success',
                    'text': 'محصول با موفقیت در سبد خرید ذخیره شد.',
                })
    else:
        return JsonResponse({
            'status': 'error',
            'icon': 'error',
            'text': 'ابتدا در سایت لاگین کنید.',
        })


class ProductView(ListView):
    template_name = r'product_module/products.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.filter(is_active=True).all()
        context['sitebanner'] = SiteBanner.objects.filter(is_active=True, position=SiteBanner.SiteBannerPosition.product_list).first()
        return context
    
    def get_queryset(self):
        if self.kwargs == {}:
            query = super().get_queryset()
            return query
        elif 'category' in self.kwargs:
            query = super().get_queryset()
            query = query.filter(is_active=True, category__url_title=self.kwargs['category'])
            return query
        elif 'type' in self.kwargs:
            query = super().get_queryset()
            query = query.filter(is_active=True, type__url_title=self.kwargs['type'])
            return query

    

class ProductDetailView(View):
    def get(self, request: HttpRequest, slug):
        comment_form: CommentForm = CommentForm()
        product: Product = Product.objects.filter(is_active=True, slug=slug).first()
        products: Product = list(Product.objects.filter(is_active=True, category__title=product.category.title).exclude(slug=slug).all())[-1:-4:-1]

        return render(request, r'product_module/product_detail.html', context={
                'product': product,
                'products': products,
                'comment_form': comment_form
            })

    def post(self, request: HttpRequest, slug):
        comment_form: CommentForm = CommentForm(request.POST)
        if comment_form.is_valid() == True:
            email_user: User = User.objects.filter(email=comment_form.cleaned_data.get('email')).first()
            if email_user is not None:
                if request.user.email == email_user:
                    new_comment: Comment = Comment()
                    new_comment.email = comment_form.cleaned_data.get('email')
                    new_comment.full_name = comment_form.cleaned_data.get('full_name')
                    new_comment.text = comment_form.cleaned_data.get('text')
                    new_comment.commentposition = Comment.CommentPosition.product_detail
                    new_comment.read_by_admin = False
                    new_comment.is_accepted = False
                    new_comment.is_subcomment = False
                    new_comment.save()
                    return redirect(reverse('home-page'))
                else:
                    comment_form.add_error('email', 'ایمیل وارد شده با ایمیل کاربری شما مطابقت دارد')
            else:
                comment_form.add_error('email', 'همچین کاربری با این ایمیل یافت نشد')
        else:
            comment_form.add_error('email', 'خطایی در تکمیل فرم رخ داده')

        product: Product = Product.objects.filter(is_active=True, slug=slug).order_by('-price')
        products: Product = Product.objects.filter(is_active=True).all()
        
        return render(request, r'product_module/product_detail.html', context={
            'product': product,
            'products': products,
            'comment_form': comment_form
        })
