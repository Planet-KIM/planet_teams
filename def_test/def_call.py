class testclass:

    def __init__(self, a):
        self.a = a

    def __call__(self):

        print("a :", self.a.__name__)
        self.a()
        print("a : ", self.a.__name__)

@testclass
def printer():
    print("출력")
    #call이랑 관계없음
    #return "hi"

print("_____")
printer()