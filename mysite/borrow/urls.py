from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('add_cart', views.add_cart, name='add_cart'),
    path('cart', views.cart, name='cart'),
    path('admin_dashboard/<status>', views.admin_dashboard, name='admin_dashboard'),
    path('reserve_date/<borrow_id>', views.reserve_date, name='reserve_date'),
    path('reserve', views.reserve, name='reserve'),
    path('edit_reservedate', views.edit_reservedate, name='edit_reservedate'),
    path('history/<status>', views.history, name='history'),
    path('delete_cart/<id>', views.delete_cart, name='delete_cart'),
    path('delete_itemcart/<id>/<item_id>/<slug>', views.delete_itemcart, name='delete_itemcart'),
    path('reserve_check/', views.reserve_check, name='reserve_check'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
