#입력받은 값의 구구단을 출력해주고 값이 50초과 이면 예외발생 아니면 구구단 출력
A = int(input("수를 입력해주세요. : "))

def cal(A):
    count = 0
    content = []

    while (1):
        count = count + 1
        B = A * count
        print(B)

        if B > 50:
            return content
        content.append(B)

C = cal(A=A)
print(C)
