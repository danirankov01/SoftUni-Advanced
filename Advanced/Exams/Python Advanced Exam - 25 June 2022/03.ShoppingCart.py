def shopping_cart(*args):
    cart = {}
    
    for el in args:
        if(el == "Stop"): break

        if(el[0] not in cart):
            cart[el[0]] = []
        
        if(el[0] == "Pizza" and len(cart['Pizza']) < 4):
            if(el[1] not in cart['Pizza']):
                cart['Pizza'].append(el[1])

        elif(el[0] == "Soup" and len(cart['Soup']) < 3):
            if(el[1] not in cart['Soup']):
                cart['Soup'].append(el[1])

        elif(el[0] == "Dessert" and len(cart['Dessert']) < 2):
            if(el[1] not in cart['Dessert']):
                cart['Dessert'].append(el[1])

    sortedMeals = {k: v for k, v in sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))}

    result = ""
    if(len(sortedMeals) != 0):
        for k in sortedMeals.keys():
            result += f"{k}:\n"
            for v in sorted(sortedMeals[k]):
                result += f" - {v}\n"

        if('Dessert' not in sortedMeals):
            result += f"Dessert:\n"
        if('Pizza' not in sortedMeals):
            result += f"Pizza:\n"
        if('Soup' not in sortedMeals):
            result += f"Soup:\n"

    else:
        result += "No products in the cart!"
        

    return result


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

