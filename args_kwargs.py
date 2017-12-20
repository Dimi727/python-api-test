def m_method(arg1,arg2):
    return arg1+arg2


def ultra_method(*args): ## args Anna
    return sum(args)



def kwargs(*args,**kwargs): #keyword args location="UK"
    print(args)
    print(kwargs)


kwargs(name="Test", location="UK")