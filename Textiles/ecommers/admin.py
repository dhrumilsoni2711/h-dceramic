from django.contrib import admin
from .models import  Contact, Feedback, Cart, Category, AdminInfo, CustomerInfo, Product,OrderInfo 

class CustomerInfoAdmin(admin.ModelAdmin):
    # Specify which fields you want to display in the list view
    list_display = ('u_id', 'name', 'email','streetaddress','city','state','pincode','phonenumber')

class CategoryInfo(admin.ModelAdmin):
    # Specify which fields you want to display in the list view
    list_display = ('c_id','name','image')
    
class ProductInfo(admin.ModelAdmin):
    # Specify which fields you want to display in the list view
    list_display = ('p_id','name','price','category','size','image')
    
class Order(admin.ModelAdmin):
    # Specify which fields you want to display in the list view
    list_display = ('o_id','username','product','total_price','address','phone_number','payment_mode','payment_status','date')

class CartInfo(admin.ModelAdmin):
    # Specify which fields you want to display in the list view
    list_display = ('c_id','product_id','quantity','email')

class Admin(admin.ModelAdmin):
    # Specify which fields you want to display in the list view
    list_display = ('a_id','name','email','phonenumber')

class ContactInfo(admin.ModelAdmin):
    # Specify which fields you want to display in the list view
    list_display = ('username','email','phonenumber','message')

class FeedbackInfo(admin.ModelAdmin):
    # Specify which fields you want to display in the list view
    list_display = ('username','email','message')
# Register the model with the custom admin interface
admin.site.register(CustomerInfo, CustomerInfoAdmin)
admin.site.register(AdminInfo,Admin)
admin.site.register(Cart,CartInfo)
admin.site.register(OrderInfo,Order)
admin.site.register(Contact,ContactInfo)
admin.site.register(Feedback,FeedbackInfo)
admin.site.register(Product,ProductInfo)
admin.site.register(Category,CategoryInfo)
