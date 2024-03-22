def get_integer(prompt) :
    return int(input(prompt))

def exchange(money) :
    h5 = money // 500
    money %= 500

    h1 = money // 100
    money %= 100

    t5 = money // 50
    money %= 50

    t1 = money // 10

    print('500원 동전이 개수: ', h5, '\n100원 동전의 개수: ', h1, '\n50원 동전의 개수: ', t5, '\n10원 동전의 개수: ', t1)

result = get_integer('동전으로  교환하고자 하는 금액은? ')
exchange(result)

