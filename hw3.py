import get_fixed_priced as fPrice

sale_rate = int(input('할인률은?'))
('할인율은?',sale_rate)
A_price = int(input('A 상품의 할인된 가격은?'))
('A 상품의 할인된 가격은?', A_price)
B_price = int(input('B 상품의 할인된 가격은?'))
('B 상품의 할인된 가격은?', B_price)

print('A 상품의 정가는?', fPrice.get_fixed_priced(sale_rate, A_price), '원')
print('B 상품의 정가는?', fPrice.get_fixed_priced(sale_rate, B_price), '원')

    
    
    
    
