def is_trangle():
    a = float(raw_input('Put the first stick length:'))
    b = float(raw_input('Put the second stick length:'))
    c = float(raw_input('Put the third stick length:'))

    if a+b > c and b+c > a and a+c > b:
        print 'This is a triangle'   
    else:
        
        print 'This is not a triangle'

is_trangle()
                
