def do_stuff(num=0):
    try:
        if num != "" and num is not None:  # Check if num is not an empty string or None
            return int(num) + 5
        else:
            return "please enter number"
    except ValueError as err:
        return err


#import utility
#import shopping.shopping_cart

#print(shopping.shopping_cart.buy("apple"))