def rep_char(s, d) :
    print(s * d)
    

def draw_line_string(name) :
    msg1 = 'Hello ' + str(name)+ ','
    msg2 = 'Welcome to Seoul.'
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-', nstr)
    print(f'{msg1}\n{msg2}')
    rep_char('-', nstr)


name = input('input his/her name: ')
draw_line_string(name)
