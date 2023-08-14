from django.urls import path
from .views import DashBoardView, ChangeInformationView, ChangePasswordView, RecentInvoicesView, InvoiceDetailView

urlpatterns = [
    path('user/dashboard', view=DashBoardView.as_view(), name='dashboard-page'),
    path('user/change-information', view=ChangeInformationView.as_view(), name='changeinformation-page'),
    path('user/recent-invoices/', view=RecentInvoicesView.as_view(), name='recentinvoices-page'),
    path('user/invoice_detail/<int:pk>', view=InvoiceDetailView.as_view(), name='invoicedetail-page'),
    path('user/change-password', view=ChangePasswordView.as_view(), name='changepassword-page'),
]
