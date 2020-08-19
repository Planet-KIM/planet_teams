content= [1, 2, 3, 4, "hi", 5]
def assertion():

    data = int(input("입력하세요. : "))
    if type(data) is int:
        print(type(data))

def assertion2(A):
    assert type(A) is int, "정수 값이 아닙니다."

for i in content:
    assertion2(A=i)
    print(i)