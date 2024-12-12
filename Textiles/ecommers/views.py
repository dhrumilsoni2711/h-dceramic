from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from .models import Product, Cart, AdminInfo, Category, CustomerInfo,Contact,Feedback, OrderInfo
from .forms import AdminLoginForm
import random
from twilio.rest import Client

##########################################################
########################  Admin-login  ###################

def admin_login(request):
    form = AdminLoginForm()

    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('a_name')
            password = form.cleaned_data.get('a_password')

            try:
                admin = AdminInfo.objects.get(name=name)
                if password == admin.password:  
                    return redirect('/admin/')
                else:
                    return render(request, 'adminlogin.html', {'form': form, 'error': 'Invalid password'})
            except AdminInfo.DoesNotExist:
                return render(request, 'adminlogin.html', {'form': form, 'error': 'Invalid username or password'})

    return render(request, 'adminlogin.html', {'form': form})

##########################################################
########################  Register  ######################

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        streetaddress = request.POST.get('streetaddress')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        password = request.POST.get('password')

        # Manual validations
        errors = []

        if not name:
            errors.append("Name is required.")
        if not email or '@' not in email:
            errors.append("A valid email is required.")
        if not phonenumber or not phonenumber.isdigit() or len(phonenumber) != 10:
            errors.append("Phone number must be 10 digits.")
        if not streetaddress:
            errors.append("Street address is required.")
        if not state:
            errors.append("State is required.")
        if not city:
            errors.append("City is required.")
        if not pincode or not pincode.isdigit() or len(pincode) != 6:
            errors.append("Pin code must be 6 digits.")
        if not password or len(password) < 8:
            errors.append("Password must be at least 8 characters long.")

        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'register.html')

        customer = CustomerInfo(
            name=name,
            email=email,
            phonenumber=phonenumber,
            streetaddress=streetaddress,
            state=state,
            city=city,
            pincode=pincode,
            password=password
        )

        try:
            customer.save()
            user = CustomerInfo.objects.get(email=email)
            request.session['user_id'] = user.u_id 
            request.session['email'] = email
            messages.success(request, 'Registeration successfully.')
            return redirect('index')
        except IntegrityError:
            messages.error(request, "Phone number or email already exists.")

    return render(request, 'register.html')

##########################################################
########################  User Login  ####################

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = CustomerInfo.objects.get(email=username) 
            if user.password == password:
                # Set session data
                request.session['user_id'] = user.u_id  
                request.session['email'] = user.email
                messages.success(request, 'Login successfully.')
                return redirect('index')
            else:
                return render(request, 'login.html', {'error': 'Invalid password'})
        except CustomerInfo.DoesNotExist:
            return render(request, 'login.html', {'error': 'User does not exist'})

    return render(request, 'login.html')

##########################################################
###################  Forget Password #####################

TWILIO_ACCOUNT_SID = 'AC764295d7e0bc13b5b0e9f8c758512811'
TWILIO_AUTH_TOKEN = 'ea6f47191de767569ea58b9018d77d2d'
TWILIO_PHONE_NUMBER = '+12096387601' 

from twilio.rest import Client

def send_otp_via_sms(phone_number, otp, country_code):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f'Your OTP is: {otp}',
        from_=TWILIO_PHONE_NUMBER,
        to=f'+91{phone_number}'  # Format the phone number with country code
    )
    print(message.sid)  # For debugging purposes
    return True  # Indicating the message was sent successfully


def forget(request):
    if request.method == 'POST':
        # Step 1: Send OTP
        if 'phone_number' in request.POST:
            username = request.POST.get('phone_number')
            otp = random.randint(100000, 999999)  # Generate a random 6-digit OTP
            
            try:
                user = CustomerInfo.objects.get(phonenumber=username)  
                phone_number = user.phonenumber 

                # Send OTP via SMS
                if send_otp_via_sms(phone_number, otp, '91'):  # Replace '91' with the appropriate country code
                    request.session['otp'] = otp  # Store OTP in session for verification
                    request.session['user_id'] = user.u_id  # Store user ID for later use
                    request.session['phone_number'] = phone_number  # Store phone number for later use
                    return render(request, 'forget.html', {'otp_sent': True})  # Redirect to OTP verification page
                else:
                    return render(request, 'forget.html', {'error': 'Failed to send OTP.'})
            
            except CustomerInfo.DoesNotExist:
                return render(request, 'forget.html', {'error': 'User not found.'})

        # Step 2: Verify OTP
        if 'otp' in request.POST:
            otp_entered = request.POST.get('otp')
            if str(otp_entered) == str(request.session.get('otp')):
                return render(request, 'forget.html', {'otp_verified': True})
            else:
                messages.success(request, 'Invalid OTP')
                return render(request, 'forget.html', {'otp_sent': True})

        # Step 3: Update Password
        if 'password' in request.POST and 'conformpassword' in request.POST:
            password = request.POST.get('password')
            confirm_password = request.POST.get('conformpassword')

            if password == confirm_password:
                user = CustomerInfo.objects.get(phonenumber=request.session.get('phone_number'))
                user.password = password  
                user.save()
                messages.success(request, 'Password updated successfully.')
                return redirect('login')
            else:
                messages.success(request, 'Passwords do not match.')
                return render(request, 'forget.html', {'otp_verified': True})

    return render(request, 'forget.html')

##########################################################
########################  Logout  ########################

def logout(request):
    # Clear the session
    request.session.flush()
    messages.success(request, 'Logout successfully.')
    return redirect('index')



##########################################################
########################  Index  #########################

def index(request):
    user_id = request.session.get('user_id')
    categories = Category.objects.all()
    products = list(Product.objects.all())  # Fetch all products
    random.shuffle(products)  # Shuffle to display random products
    products = products[:8]  # Select 8 random products

    if user_id:
        return render(request, 'index.html', {'is_logged_in': True, 'categories': categories, 'products': products})
    else:
        return render(request, 'index.html', {'is_logged_in': False, 'categories': categories, 'products': products})

##########################################################
########################  Shop  ##########################

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    user_email = request.session.get('email')  # Use `email` from session
    user_id = request.session.get('user_id')
   
   

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        
        if 'cart' in request.POST:
            if user_email :
            # Check if the product is already in the cart
                 cart_item = Cart.objects.filter(email=user_email, product_id=product_id).first()

                 if cart_item:
                # If the product is already in the cart, increase the quantity
                     cart_item.quantity += 1
                     cart_item.save()
                     messages.success(request, 'Cart Update successfully.')
                
                 else:
                # If the product is not in the cart, add it
                     Cart.objects.create(email=user_email, product_id=product_id, quantity=1)
                     messages.success(request, 'Cart Update successfully.')
            else:
                return redirect('login')

            

    if user_id:
        return render(request, 'shop.html', {'is_logged_in': True, 'categories': categories, 'products': products})
    else:
        return render(request, 'shop.html', {'is_logged_in': False, 'categories': categories, 'products': products})

##########################################################
########################  Cart  ##########################

def cart(request):
    user_id = request.session.get('user_id')
    
    if user_id:
        email = request.session.get('email')
        cart_items = Cart.objects.filter(email=email)
        products = []
        total_price = 0
        
        for item in cart_items:
            product = Product.objects.get(p_id=item.product_id)
            
            size = product.size
            quantity = item.quantity

            # Initialize sq ft based on size
            if size == "600 x 600":
              square_footage_per_box = 38.74
            elif size == "300 x 300":
                 square_footage_per_box = 9.68
            elif size == "600 x 1200":
                 square_footage_per_box = 77.50
            else:
                 square_footage_per_box = None

            # Calculate total square footage based on quantity
            total_square_footage = square_footage_per_box * quantity if square_footage_per_box else None
     
            
            products.append({
                'name': product.name,
                'id': product.p_id,
                'category': product.category,
                'size': product.size,
                'price': product.price,
                'image': product.image,
                'total_square_footage': total_square_footage,
                'quantity': item.quantity
            })
            total_price += product.price * item.quantity
        if request.method == 'POST':
            product_id = request.POST.get('product_id')
            quantity_change = int(request.POST.get('quantity_change', 0))  # Default to 0 if not provided
            
      
            if 'remove' in request.POST:
                try:
                    cart_item = Cart.objects.get(email=email, product_id=product_id)
                    cart_item.delete()
                     # Remove the item from the cart
                except Cart.DoesNotExist:
                    pass
            else:  
                try:
                    cart_item = Cart.objects.get(email=email, product_id=product_id)
                    cart_item.quantity += quantity_change
                    if cart_item.quantity <= 0:
                        cart_item.delete()
                    else:
                        cart_item.save()
                except Cart.DoesNotExist:
                    pass
            
            return redirect('cart')

        return render(request, 'cart.html', {'is_logged_in': True, 'products': products, 'total_price': total_price})
    else:
        return redirect('login')
    
##########################################################
########################  Checkout  ######################

def cartcheckout(request):
    user_id = request.session.get('user_id')

    if user_id:
        email = request.session.get('email')
        info = get_object_or_404(CustomerInfo, email=email)
        cart_items = Cart.objects.filter(email=email)
        products = []
        table = []
        total_price = 0

        # Calculating total price and preparing product data
        for item in cart_items:
            product = get_object_or_404(Product, p_id=item.product_id)
            products.append({
                'name': product.name,
                'id': product.p_id,
                'category': product.category,
                'size': product.size,
                'price': float(product.price),
                'image': product.image,
                'qut': item.quantity
            })
            table.append({
                'name': product.name,
                'quantity': item.quantity
            })
            total_price += product.price * item.quantity

        tax = (total_price * 10) / 100
        total = total_price + 500 + tax

        if request.method == 'POST':
            phone_number = request.POST.get('checkout-phone')
            address = f"{request.POST.get('checkout-address')}, {request.POST.get('checkout-city')}, {request.POST.get('checkout-country')}, {request.POST.get('checkout-postal')}"
            payment_mode = request.POST.get('payment_mode')

            # Determine payment status based on payment mode
            if payment_mode == 'cash_on_delivery':
                payment_status = 'pending'
            elif payment_mode == 'online_payment':
                payment_status = 'received'
            else:
                payment_status = 'pending'  
           
            # Create and save order
            order = OrderInfo(
                username=info.name,
                product=[(item['name'], item['quantity']) for item in table],
                total_price=total,
                address=address,
                phone_number=phone_number,
                payment_mode=payment_mode,
                payment_status=payment_status
            )

            order.save()  
            # Clear cart items after order is placed
            cart_items.delete()

            messages.success(request, 'Order placed successfully.')
            return redirect('feedback')

        return render(request, 'checkout.html', {
            'product': products,
            'is_logged_in': True,
            'info': info,
            'total_price': float(total_price),
            'tax': float(tax),
            'total': float(total)
        })

    else:
        return redirect('login')

##########################################################
########################  About  #######################
 
def about(request):
    user_id = request.session.get('user_id')
   
    if user_id:
        return render(request, 'about.html', {'is_logged_in': True})
    else:
        return render(request, 'about.html', {'is_logged_in': False})
    
##########################################################
########################  Contact  #######################

def contact(request):
    user_id = request.session.get('email')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Store form data in the Contact model
        contact = Contact(username=name, email=email, phonenumber=phone, message=message)
        contact.save()
        messages.success(request, 'Contect information submitted successfully.')
        return redirect('index')
    if user_id:
        return render(request, 'contact.html', {'is_logged_in': True})
    else:
        return render(request, 'contact.html', {'is_logged_in': False})

##########################################################
########################  Feedback  ######################

def feedback(request):
    user_id = request.session.get('email')
    if request.method == 'POST':
     if 'feedback' in request.POST:
        name = request.POST.get('name')
        email = request.session.get('email')
        message = request.POST.get('message')

        # Store form data in the Contact model
        feedback = Feedback(username=name, email=email, message=message)
        feedback.save()
        messages.success(request, 'Feedback submitted successfully.')
        return redirect('index')
    if user_id:
        return render(request, 'feedback.html', {'is_logged_in': True})
    else:
        return render(request, 'feedback.html', {'is_logged_in': False})


##########################################################
########################  Profile  #######################

def profile(request):
    user_id = request.session.get('email')

    if not user_id:
        return redirect('login')

    Customer_Info = get_object_or_404(CustomerInfo, email=user_id)

    if request.method == 'POST':
    # Get form data
     name = request.POST.get('name')
     streetaddress = request.POST.get('streetaddress')
     city = request.POST.get('city')
     state = request.POST.get('state')
     pincode = request.POST.get('pincode')
    
    # Validate pincode
     if not (pincode.isdigit() and len(pincode) == 6):
        messages.success(request, 'Pincode must be a 6-digit number.')
        return redirect('profile')
    
    # Update profile information
     Customer_Info.name = name
     Customer_Info.streetaddress = streetaddress
     Customer_Info.city = city
     Customer_Info.state = state
     Customer_Info.pincode = pincode
     Customer_Info.save()
    
     messages.success(request, 'Profile updated successfully')
     return redirect('profile')
    
    orders = OrderInfo.objects.filter(username=Customer_Info.name)
    feedbacks = Feedback.objects.filter(email=user_id)

    context = {
        'is_logged_in': True,
        'Customer_Info': Customer_Info,
        'orders': orders,
        'feedbacks': feedbacks,
    }
    
    return render(request, 'profile.html', context)

##########################################################
#####################  DeleteAccount  ####################

def delete_account(request):
    user_id = request.session.get('email')
    customer_info = get_object_or_404(CustomerInfo, email=user_id)

    if request.method == 'POST':
        customer_info.delete()
        request.session.flush()
        messages.success(request, 'Account deleted successfully')
        return redirect('index')  # Redirect to home page or login page

    return render(request, 'profile.html')

##########################################################
########################  Bill  ##########################

def bill(request, order_id):
    user_id = request.session.get('email')
    order = get_object_or_404(OrderInfo, o_id=order_id) 
    user = get_object_or_404(CustomerInfo, email=user_id)
    pro = Product.objects.all() 
     
    context = {
        'order': order,
        'user': user,
        'pro': pro,
        
    }
    return render(request, 'bill.html', context)