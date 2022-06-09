print(list(filter(lambda num:num %2==0,range(1,30))))

print(tuple(filter(lambda a:a%2!=0,range(1,20))))

product_prices=[54,39,400,50,100]
print(list(filter(lambda prices:prices>=100,product_prices)))

new_prices=list(filter(lambda prices:prices>=100,product_prices))
