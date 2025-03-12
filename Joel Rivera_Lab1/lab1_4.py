#lab1_4.py – Joel Rivera
#calculating the price of an item after a 25% reduction
price=99.99
discountPercent=25
markdown=discountPercent/price*100
price=price-markdown
print(round(price,2))