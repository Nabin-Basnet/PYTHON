def greet(fxgit):
    def mfx():
        print("good morning")
        fx()
        print("thanks")
    return mfx

@greet
def hello():
    print("hello world")

hello()


def add(a,b):
    print(a+b)

add(12,15)