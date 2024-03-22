def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(rr):
    rrr = 3.14 * rr * rr
    return rrr


rr = get_radius('넓이를 구하고자 하는 원의 반지름은?')
result = get_circle_area(rr)
print('반지름', rr, '인 원의 넓이 = 3.14 x ',rr, 'x ',rr, '=' , result)

