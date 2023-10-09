#variable number of keyword arguments
"""
def keyword_args (**kwargs):
    print(kwargs)
    return kwargs
"""
def keywordargs(**kwargs):
    print(kwargs)
    return kwargs

keywordargs(a=1,b=2,c=2,d=4,e=5,f=6)


def keywordargs(*x,**kwargs):
    print(kwargs)
    print(x)
    return kwargs

keywordargs(1,23,4,a=1,b=2,c=2,d=4,e=5,f=6)
#-------

def keywordargs(i,j,k,l=20,*x,**kwargs):
    print(kwargs)
    print(x)
    print(l)
    return kwargs

keywordargs(1,23,4,2,3,43,5,6,7,a=1,b=2,c=2,d=4,e=5,f=6)