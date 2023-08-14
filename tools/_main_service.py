def newest_blogs(queryset: list, N_of_newest: int=3) -> list:
    to_list: list = list(queryset)
    return to_list[-1:-N_of_newest:-1]


def div_products(product_list: list, size: int=4) -> list:
    products: list = []
    
    if len(product_list) >= 4:
        for index in range(0, len(product_list), size):
            products.append(product_list[index:index + size])
        else:
            return products
    else:
        return None


def final_price(user_order_detail: list) -> int:
    price: int = 0
    for item in user_order_detail:
            price += item.product.price * item.count
    else:
        return price


def discount(user_order_detail: list, discount: int=2) -> int:
    totale = final_price(user_order_detail)
    return int(totale / discount)


def totale_price(final_price: int, discount: int=0, shipping_price: int=0) -> int:
    try:
        return final_price - discount - shipping_price
    except:
        return 'error'