from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

########################################################
##################### AdminInfo ########################

class AdminInfo(models.Model):
    a_id = models.CharField(max_length=10, unique=True, editable=False,primary_key=True)  
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True,max_length=50)
    phonenumber = models.CharField(
        max_length=10, 
        unique=True,
        validators=[
            RegexValidator(regex=r'^\d{10}$', message="Phone number must be 10 digits.")
        ]
    )
    password = models.CharField(max_length=8)  
    
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.a_id:  
            last_admin = AdminInfo.objects.all().order_by('a_id').last()
            if last_admin:
                last_id_number = int(last_admin.a_id.split('_')[1])
                self.a_id = f'aid_{last_id_number + 1}'
            else:
                self.a_id = 'aid_1'
        super(AdminInfo, self).save(*args, **kwargs)

########################################################
##################### CustomerInfo #####################

class CustomerInfo(models.Model):
 u_id = models.CharField(max_length=10, primary_key=True, unique=True, editable=False)
 name = models.CharField(max_length=50, editable=False)
 email = models.EmailField(unique=True, max_length=50, editable=False)
 phonenumber = models.CharField(
        max_length=10, 
        unique=True,
        validators=[
            RegexValidator(regex=r'^\d{10}$', message="Phone number must be 10 digits.")
        ],
        editable=False
    )
 streetaddress = models.CharField(max_length=50, editable=False)
 state = models.CharField(max_length=20, editable=False)
 city = models.CharField(max_length=20, editable=False)
 pincode = models.CharField(
        max_length=6,
        validators=[
            RegexValidator(regex=r'^\d{6}$', message="Pin code must be 6 digits.")
        ],
        editable=False
    )
 password = models.CharField(
        max_length=8,
        validators=[
            MinLengthValidator(8, message="Password must be at least 8 characters long.")
        ],
        editable=False
    )

 def __str__(self):
        return self.name

 def save(self, *args, **kwargs):
        if not self.u_id:
            last_user = CustomerInfo.objects.all().order_by('u_id').last()
            if last_user:
                count = CustomerInfo.objects.count()
                self.u_id = f'uid_{count + 1}'
                
            else:
                self.u_id = 'uid_1'
        super(CustomerInfo, self).save(*args, **kwargs)

########################################################
##################### Category #########################

class Category(models.Model):
    c_id = models.CharField(max_length=10, unique=True, primary_key=True, editable=False)
    image = models.ImageField(upload_to='category_images/',null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True) 

    def save(self, *args, **kwargs):
        if not self.c_id:  
            last_category = Category.objects.all().order_by('c_id').last()
            if last_category:
                count = Category.objects.count()
                self.c_id = f'cid_{count + 1}'
                
            else:
                self.c_id = 'cid_1'
        super(Category, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

########################################################
##################### Product ##########################     
        
class Product(models.Model):
    p_id = models.CharField(max_length=10, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=60)
    size = models.CharField(max_length=20)  
    image = models.ImageField(upload_to='products/images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.p_id:
            last_product = Product.objects.all().order_by('p_id').last()
            if last_product:
                count = Product.objects.count()
                self.p_id = f'pid_{count + 1}'
            else:
                self.p_id = 'pid_1'
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name       

########################################################
##################### Cart #############################

class Cart(models.Model):  
   c_id=  models.CharField(max_length=10, primary_key=True, editable=False, unique=True)
   product_id = models.CharField(max_length=10, editable=False)  
   quantity = models.IntegerField(default=1)  
   email = models.EmailField(max_length=50)
  
   def save(self, *args, **kwargs):
        if not self.c_id: 
            last_product = Cart.objects.all().order_by('c_id').last()
            if last_product:
                count = Cart.objects.count()
                self.c_id = f'cid_{count + 1}'
            else:
                self.c_id = 'cid_1'
        super(Cart, self).save(*args, **kwargs)
    
   def __str__(self):  
      return self.c_id
    
########################################################
##################### OrderInfo ########################

class OrderInfo(models.Model):
    o_id = models.CharField(max_length=10, primary_key=True, unique=True)  
    username = models.CharField(max_length=20) 
    product = models.JSONField() 
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()  
    phone_number = models.CharField(max_length=10) 
    payment_mode = models.CharField(max_length=50)  
    payment_status = models.CharField(max_length=20)  
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.o_id} by {self.username}"

    def save(self, *args, **kwargs):
        if not self.o_id: 
            last_order = OrderInfo.objects.all().order_by('o_id').last()
            if last_order:
                count = OrderInfo.objects.count()
                self.o_id = f'oid_{count + 1}'
                
            else:
                self.o_id = 'oid_1'
        super(OrderInfo, self).save(*args, **kwargs)  

########################################################
##################### Contact ##########################

class Contact(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.username} ({self.email})"

########################################################
##################### Feedback #########################
    
class Feedback(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Feedback from {self.username} ({self.email})"

