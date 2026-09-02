#CDAC CAFETERIA DISCOUNT CALCULATOR
def calculate_cafetria_bill(base_price, *items, tax_rate=0.05,discount=0.0,delivery_fee=0.0):
    sub_total = base_price + sum(items)
    discounted_sub_total = sub_total*(1-(discount/100))
    tax_value = discounted_sub_total* tax_rate
    final_total = delivery_fee + discounted_sub_total
    return round(final_total,2)
print(calculate_cafetria_bill(300,5,tax_rate=0.05,discount=20,delivery_fee=10))
