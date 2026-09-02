#DE-DUPLICTING SHOPPING CART
Cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
print([Cart[i] for i in range(len(Cart)) if Cart.index(Cart[i]) == i])