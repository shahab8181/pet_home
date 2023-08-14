from django.urls import path
from .views import ProductView, ProductDetailView, add_order


urlpatterns = [
    path('products/', view=ProductView.as_view(), name='products-page'),
    path('products/single-product/<slug:slug>', view=ProductDetailView.as_view(), name='product-page'),
    path('products/type/<slug:type>', view=ProductView.as_view(), name='productsfilter-tp-page'),
    path('products/category/<slug:category>', view=ProductView.as_view(), name='productsfilter-cat-page'),
    path('products/add-order', view=add_order, name='add-order-ajax'),
]
