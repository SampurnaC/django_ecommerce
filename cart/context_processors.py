
def cart_total_quantity(request):
    total_quantity = 0
    if 'cart' in request.session:
        cart = request.session['cart']
        # total_quantity = sum(item['quantity'] for item in cart.values())
        total_quantity=0
        for item in cart.values():
            quantity=item['quantity']
            total_quantity=total_quantity+quantity
            
    
    return {
        'total_quantity': total_quantity
    }
