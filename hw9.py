class Rectangle :
    def show(ltx, lty, rbx, rby) :
        return ltx, lty, rbx, rby

    def getWidth(ltx, rbx) :
        return (rbx-ltx)

    def getHeight(lty, rby) :
        return (rbx-ltx)

    def getArea() :
        m = (rbx-ltx) * (lty-rby)
        return m

    def getPoint() :
        r = (rbx-ltx)+(rbx-ltx)
        result = 2*r
        return result

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'좌측 상단 꼭지점이 ({show})이고 우측 하단 꼭지점이 ({show})인 사각형입니다.')
print(f'\n넓이는 {a}, 둘레는 {p}')
        
        
        
    
