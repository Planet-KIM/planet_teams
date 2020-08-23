Dictionary = {'사과':'apple', '오렌지':'orange', '바나나':'banana', '망고':'mango', '수박':'watermelon',
              '레몬':'lemon', '딸기':'strawberry', '메론':'melon', '복숭아':'peach', '체리':'cherry' }

def manu(D):

    print(list(Dictionary.keys()))

manu(D= Dictionary)

def serch(D):

    A = str(input("검색할 단어: "))
    print(Dictionary[A])

serch(D=Dictionary)
