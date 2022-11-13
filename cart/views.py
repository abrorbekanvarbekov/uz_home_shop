from django.shortcuts import render, redirect
from cart.models import Cart, CartItem
from product.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from user.models import User
# Create your views here.
@csrf_exempt
def _cart_id_(request):
    cart  = request.session.session_key
    if not cart :
        cart = request.session.create()
    return cart

@csrf_exempt
def add_cart(request, product_id):
    if request.method =='POST':
        quantity = request.POST.get('quantity',None)
        product = Product.objects.get(id=product_id)
        user_id = request.session.get('user_id',None)
        try:
            cart = Cart.objects.get(cart_id = user_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id = user_id)
            cart.save()
            # print(cart)
        
        try:
            cart_item = CartItem.objects.get(product=product, cart=cart)
            cart_item.quantity +=int(quantity)
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                product=product,
                quantity = quantity,
                cart=cart,
                )
            cart_item.save()
    return redirect('cart:cart_detail')


@csrf_exempt
def quantity_plus(request):
    if request.method == "POST":
        feed_id = request.POST.get('feed_id',None)
        product = Product.objects.get(id=feed_id)
        user_id = request.session.get('user_id',None)
    # try:
        cart = Cart.objects.get(cart_id = user_id)
    # except Cart.DoesNotExist:
        # cart = Cart.objects.create(cart_id = _cart_id_(request))
        # cart.save()  
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity +=1
        cart_item.save()
        print(cart_item.quantity) 
    return redirect('cart:cart_detail')


@csrf_exempt
def quantity_minus(request):
    if request.method == "POST":
        feed_id = request.POST.get('feed_id',None)
        product = Product.objects.get(id=feed_id)
        user_id = request.session.get('user_id',None)
    # try:
        cart = Cart.objects.get(cart_id = user_id)
    # except Cart.DoesNotExist:
    #     cart = Cart.objects.create(cart_id = _cart_id_(request))
    #     cart.save()  

        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity >0:
            cart_item.quantity -=1
            cart_item.save()
        print(cart_item.quantity)  
    return redirect('cart:cart_detail')


@csrf_exempt
def cart_detail(request, total=0, counter=0, cart_items=None,delivery_fee=0):
    try:
        user_id = request.session.get('user_id',None)
        cart = Cart.objects.get(cart_id=user_id)
        cart_items = CartItem.objects.filter(cart=cart,active=True).order_by('-id')
        for cart_item in cart_items:
            total += (cart_item.product.sell_price * cart_item.quantity)
            if total >= 30000:
                delivery_fee= 0 
            else:
                delivery_fee = 3000
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    email = request.session.get('email',None)
    user = User.objects.filter(email=email).first()
    return render(request, "cart/cart.html", context=dict(
                                            cart_items=cart_items,
                                            total=total,
                                            counter=counter,
                                            pay_price=total + delivery_fee,
                                            user=user,
                                            delivery_fee = delivery_fee
                                            ))


@csrf_exempt
def cart_delite(request,id):
    product = Product(id=id)
    user_id = request.session.get('user_id',None)
    cart = Cart.objects.get(cart_id = user_id)
    cart.save()

    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
        
    return redirect('cart:cart_detail')
