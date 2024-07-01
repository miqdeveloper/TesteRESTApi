from django.urls import path
from . import views

# Sale;
# • Seller;
# • Purchase;
# • Buyer;

# • Stock;

urlpatterns = [
  path('stock/', views.stock.as_view()),
  path('stock/<int:num>/', views.stockIntem.as_view()),
  path('sale/', views.sale.as_view()),
  path('seller/<int:cpf>/', views.seller.as_view()),
  path('purchase/<int:idI>/', views.purchase.as_view()),
  path('buyer/', views.buyer.as_view())
  
]