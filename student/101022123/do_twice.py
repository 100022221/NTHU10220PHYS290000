def do_twice(f):
    f()
    f()
def print_spam():
    print 'spam'

do_twice(print_spam)
print'\n\n'

#########################    

def print_twice(a):
    print a
    print a
print_twice('spam')
print'\n\n'
    
#########################

def do_four(f):
    f()
    f()
    f()
    f()
    
def print_spam():
    print 'spam'
do_four(print_spam)
    
