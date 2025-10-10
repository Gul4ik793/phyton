from Сategory import drinks, dairy_products
from Product import cheese, juice, icecream
from Сheque import check



print(dairy_products)
print(drinks)
print(drinks.category)


print(cheese.get_price())
print(cheese.change_price(300))

print(cheese)
print(juice)
print(icecream)


check.add_product(icecream)
check.add_product(juice)
check.add_product(cheese)

print(check)
