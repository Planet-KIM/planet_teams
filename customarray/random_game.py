#랜덤수를 1에서 10까지 발생시키고 1숫자만 뽑아내서 그수가 무슨수인지 맞추면 탈출 맞추지 않으면 예외처리
import random


while (1):

    a = random.randint(1, 10)

    b = int(input('예상되는 값을 입력하세요 :'))

    try:
        if  a != b :

            raise Exception("정답이 아닙니다.")

        else:
            print("정답입니다.")
            break


    except Exception as e:
        print(e)