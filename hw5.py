def read_single_digit(num1) :
    korea_num = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    return korea_num[num1]


def read_number(num2) :
    hundred_num = num2 // 100
    ten_num = (num2 % 100) // 10
    one_num = num2 % 10

    result = [ ]

    if hundred_num > 0 :
        result += korea_num(hundred_digit)

    elif ten_num > 0 :
        result += korea_num(ten_digit)

    elif one_num > 0 :
        result += korea_num(one_digit)

    return result
        

num = int(input("세 자리 정수 입력: "))
digit = read_number(num)
print(digit)


          
