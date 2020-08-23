#배열을 만드는데 1, a, b, 4 하고 문자열인지 정수형인지 구분해주는 함수

content = [1, 'a', 'b', 4]

def flower(content):

    while(1):
        counta = 0
        countb = 0
        for i in content:
            #print(i)

            if type(i) == str:
                #print(type(i))
                #print("문자열 입니다.")
                counta = counta + 1

            else:

                #print(type(i))
                #print("정수형 입니다.")
                countb = countb + 1

        return counta, countb


a,b = flower(content = content)
print(a, ":", b)

def light(content):

    counta, countb = flower(content)


    while(1):

        A = int(input("문자열의 갯수를 입력해주세요: "))
        B = int(input("정수형의 갯수를 입력해주세요: "))

        try:

            if ((counta==A) and (countb==B)):
                print("정답입니다.")
                break

            elif ((counta==A)or (countb==B)):

                raise Exception("정답이 아닙니다.")


        except Exception as e:
            print(e)

light(content = content)

