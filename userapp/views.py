from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.conf import settings
from django.shortcuts import render, redirect
from bookapp.models import Book
from .models import CartItem , Cart
from guestapp.models import userTable
import stripe
# Create your views here.

def listitem(request):
    books = Book.objects.all()
    return render(request, 'user/home.html', {'books': books})

def search(request):
    query = None
    books = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
    else:
        books = []

    context = {'books': books, 'query': query}
    return render(request, 'user/home.html', context)

def add_to_cart(request, book_id):
    if 'username' in request.session:
        user = userTable.objects.get(username=request.session['username'])
        book = Book.objects.get(id=book_id)
        if book.quantity > 0:
            cart, created = Cart.objects.get_or_create(user=user)
            cart_item, item_created = CartItem.objects.get_or_create(cart=cart, book=book)
            if not item_created:
                cart_item.quantity += 1
                cart_item.save()
        return redirect('viewcart')
    else:
        return redirect('login')  # Redirect to login if user not in session

def view_cart(request):
    if 'username' in request.session:
        user = userTable.objects.get(username=request.session['username'])
        cart, created = Cart.objects.get_or_create(user=user)
        cart_items = cart.cartitem_set.all()
        total_price = sum(item.book.price * item.quantity for item in cart_items)
        total_items = cart_items.count()
        context = {'cart_items': cart_items, 'total_price': total_price, 'total_items': total_items}
        return render(request, 'user/cart.html', context)
    else:
        return redirect('login')

def increase_quantity(request,item_id):
    cart_item=CartItem.objects.get(id=item_id)
    if cart_item.quantity < cart_item.book.quantity:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('viewcart')

def decrease_quantity(request,item_id):
    cart_item=CartItem.objects.get(id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('viewcart')

def remove_from_cart(request,item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.delete()
    except cart_item.DoesNotExist:
        pass
    return redirect('viewcart')

def create_checkout_session(request):
    if 'username' in request.session:
        user = userTable.objects.get(username=request.session['username'])
        cart_items = CartItem.objects.filter(cart__user=user)
        if cart_items:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            if request.method == 'POST':
                line_items = []
                for cart_item in cart_items:
                    if cart_item.book:
                        line_item = {
                            'price_data': {
                                'currency': 'INR',
                                'unit_amount': int(cart_item.book.price * 100),
                                'product_data': {
                                    'name': cart_item.book.title,
                                },
                            },
                            'quantity': cart_item.quantity,  # Use actual quantity
                        }
                        line_items.append(line_item)
                if line_items:
                    checkout_session = stripe.checkout.Session.create(
                        payment_method_types=['card'],
                        line_items=line_items,
                        mode='payment',
                        success_url=request.build_absolute_uri(reverse('success')),
                        cancel_url=request.build_absolute_uri(reverse('cancel')),
                    )
                    return redirect(checkout_session.url, code=303)
        return redirect('viewcart')  # Redirect to cart page if no cart items or GET request
    else:
        return redirect('login')


def success(request):
    cart_items=CartItem.objects.all()
    for cart_item in cart_items:
        product=cart_item.book
        if product.quantity >= cart_item.quantity:
            product.quantity -= cart_item.quantity
            product.save()
    cart_item.delete()
    return render(request,'user/success.html')

def cancel(request):
    return render(request,'user/cancel.html')