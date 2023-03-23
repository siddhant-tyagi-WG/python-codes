def hello(func):
    def wrapper_hello(*args,**kwargs):
        print("Hello!")
        print(f'{kwargs}')
        val = func(*args,**kwargs)

        print("Bye!")
        return val
    return wrapper_hello

@hello
def inc(n):
    return n+1

if __name__ == "__main__":
    n = inc(n=3)
    print(n)
