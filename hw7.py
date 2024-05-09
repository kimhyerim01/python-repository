shopping_bag = {}
print('[구입]')
while True :
    item = input('상품명?')
    if not item:
        break
    quantity = input('수량은?')
    shopping_bag[item] = quantity
    print(f'장바구니에 {item} {shopping_bag[item]}개가 담겼습니다.')
    print('')
    
print(f'>>> 장바구니보기:{shopping_bag}')
print('')
print('[검색]')
item = input(f'장바구니에서 확인하고자 하는 상품은?')
print(f'{item}은(는) {shopping_bag[item]}개 담겨 있습니다.')


    
