from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('',views.index,  name='index'),
    path('contact/',views.contact,name='contact'),
    path('feedback/',views.feedback,name='feedback'),
    path('shop/',views.shop,name='shop'),
    path('about/',views.about,name='about'),
    path('admin-login/',views.admin_login, name='adminlogin'),
    path('register/', views.register, name='register'),
    path('login/',views.login,name='login'),
    path('cart/',views.cart,name='cart'),
    path('cart/checkout/',views.cartcheckout,name='cartcheckout'),
    path('logout/',views.logout,name='logout'),
    path('delete_account/',views.delete_account,name='delete_account'),
    path('profile/',views.profile,name='profile'),
    path('bill/<str:order_id>/', views.bill, name='bill'),
    path('forget/',views.forget,name='forget')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

