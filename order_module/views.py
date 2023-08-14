from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, JsonResponse
from product_module.models import Product
from .models import Order, OrderDetail, OrderCheckOut
from .forms import CheckOutForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from tools._main_service import final_price, discount, totale_price
# from django.db.models import Count

# Create your views here.

@login_required
def cart(request: HttpRequest):
    current_order: Order = Order.objects.filter(is_paid=False, user_id=request.user.id).prefetch_related('orderdetail_set').first()
    if current_order is not None:
        user_order_detail: OrderDetail = current_order.orderdetail_set.filter(order_id=current_order.id).all()
        product_count = user_order_detail.count()
        f_price: int = final_price(user_order_detail)
        d_count: int = discount(user_order_detail, 4)
        t_price = totale_price(f_price, d_count, current_order.shipping_price)
        if t_price > 0:
            current_order.final_price = t_price
            current_order.save()
            return render(request, r'order_module/cart.html', context={
                'there_was': True,
                'current_order': current_order,
                'user_order_detail': user_order_detail,
                'product_count': product_count,
                'final_price': f_price,
                'discount': d_count,
                'totale_price': t_price
            })  
        else:
            return render(request, r'order_module/cart.html', context={
                'there_was': False
            })
    else:
        return render(request, r'order_module/cart.html', context={
            'there_was': False
        })

@login_required
def make_less(request: HttpRequest):
    product_id = request.GET.get('product_id')

    if product_id is None:
        return redirect(reverse('home-page'))
    else:
        current_product: OrderDetail = OrderDetail.objects.get(product_id=product_id)
        if current_product is not None:
            current_p = Product.objects.get(id=current_product.product.id)
            if current_product.count > 0:
                current_product.count -= 1
                if current_product.count == 0: 
                    current_product.delete()
                    current_p.count += 1
                    current_p.save()
                    return JsonResponse({
                        'status': 'deleted'
                    })
                current_p.count += 1
                current_p.save()
                current_product.save()
                return JsonResponse({
                    'status': 'success',
                    'count': current_product.count
                })
            elif current_product.count == 0:
                current_product.delete()
                return render(request, r'order_module/includes/empty_cart.html')
            else:
                return JsonResponse({
                    'status': 'error',
                    'icon': 'error',
                    'text': 'عدد تعداد محصول اشتباه میباشد'
                })
        else:
            return redirect(reverse('cart-page'))

@login_required
def make_more(request: HttpRequest):
    product_id = request.GET.get('product_id')
    
    if product_id is not None:
        current_product: OrderDetail = OrderDetail.objects.get(product_id=product_id)
        current_p: Product = Product.objects.get(id=current_product.product.id)
        if current_product is not None:
            current_product.count += 1
            current_p.count -= 1
            current_product.save()
            current_p.save()
            if current_product.count >= current_product.product.count and current_product.product.count == 0:
                current_product.count -= 1
                current_p.count += 1
                current_product.save()
                current_p.save()
                return JsonResponse({
                    'status': 'error',
                    'text': 'تعداد وارد شده بیش تر از تعداد موجودی محصول میباشد!',
                    'icon': 'error'
                })
            else:
                return JsonResponse({
                    'status': 'success'
                })
        else:
            return redirect(reverse('cart-page'))
    else:
        return redirect(reverse('home-page'))
                 

@method_decorator(login_required, name='dispatch')
class CheckOutView(View):
    def get(self, request: HttpRequest, order_id):
        current_order: Order = Order.objects.filter(is_paid=False, user_id=request.user.id).prefetch_related('orderdetail_set').first()
        if current_order is not None:
            user_order_detail: OrderDetail = current_order.orderdetail_set.filter(order_id=current_order.id).all()
            product_count = user_order_detail.count()
            f_price: int = final_price(user_order_detail)
            d_count: int = discount(user_order_detail, 4)
            t_price: int = totale_price(f_price, d_count, current_order.shipping_price)
            check_out_form: CheckOutForm = CheckOutForm()
            try:
                current_check_out: OrderCheckOut = OrderCheckOut.objects.get(user_id=request.user.id, order_id=order_id)
                if current_check_out is not None:
                    return render(request, r'order_module/checkout.html', context={
                        'there_was': True,
                        'transportation': current_order.transportation,
                        'check_out_form': check_out_form,
                        'current_order': current_order,
                        'user_order_detail': user_order_detail,
                        'product_count': product_count,
                        'final_price': f_price,
                        'discount': d_count,
                        'totale_price': t_price
                    })
            except OrderCheckOut.DoesNotExist:
                return render(request, r'order_module/checkout.html', context={
                    'there_was': False
                })
        else:
            return render(request, r'order_module/checkout.html', context={
                'there_was': False
            })

    def post(self, request: HttpRequest, order_id):
        check_out_form: CheckOutForm = CheckOutForm(request.POST)
        if check_out_form.is_valid() == True:
            try:
                current_check_out: OrderCheckOut = OrderCheckOut.objects.get(user_id=request.user.id, order_id=order_id)
                if current_check_out is not None:
                    current_check_out.first_name = check_out_form.cleaned_data.get('first_name')
                    current_check_out.last_name_name = check_out_form.cleaned_data.get('last_name')
                    current_check_out.company = check_out_form.cleaned_data.get('company')
                    current_check_out.country = check_out_form.cleaned_data.get('country')
                    current_check_out.state = check_out_form.cleaned_data.get('state')
                    current_check_out.city = check_out_form.cleaned_data.get('city')
                    current_check_out.street_address = check_out_form.cleaned_data.get('street_address')
                    current_check_out.more_complete_address = check_out_form.cleaned_data.get('more_complete_address')
                    current_check_out.postal_code = check_out_form.cleaned_data.get('postal_code')
                    current_check_out.phone = check_out_form.cleaned_data.get('phone')
                    current_check_out.email = check_out_form.cleaned_data.get('email')
                    current_check_out.save()
                    return redirect(reverse('home-page'))
            except OrderCheckOut.DoesNotExist:
                return render(request, r'order_module/checkout.html', context={
                    'there_was': False
                })
        else:
            check_out_form.add_error('email', 'خطایی در تکمیل فرم رخ داده')

        return render(request, r'order_module/checkout.html', context={
            'there_was': True,
            'check_out_form': check_out_form
        })