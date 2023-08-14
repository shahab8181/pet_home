from django.urls import path
from .views import cart, CheckOutView, make_less, make_more


urlpatterns = [
    path('cart/', view=cart, name='cart-page'),
    path('cart/make-less', view=make_less, name='make-less-ajax'),
    path('cart/make-more', view=make_more, name='make-more-ajax'),
    path('cart/check-out/<int:order_id>', view=CheckOutView.as_view(), name='check-out-page'),
]
