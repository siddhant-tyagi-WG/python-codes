def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(kwargs)
        # d = args[1]
        list1=args[0]
        # k=d["pop"]
        print(list1[0])
        j=func(*args,**kwargs)
        print(j)
    return wrapper







@my_decorator
def check(l,dictionary):
    return l[1]



list1=["help",'a',1,3,45]
dictnary={"oa":23, "pop":456}
check(list1,dictnary="f")