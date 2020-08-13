#수를 입력받아 그의 배수를 출력 100이하

a = int(input("수를입력하세요.: "))

def cal(a):

    content = []

    for i in range(1,10):
        b = a * i
        content.append(b)

    return content

#print(cal(a))

def error(content):

    n = content[1] - content[0]
    p = content[2] - content[1]
    for i in content:

        try:
            if p == n:
                print("{n}의 배수입니다.".format(n=n))
                return n
            else:
                raise Exception ("배수의 배열이 아닙니다.")

        except Exception as e:
            print(e)
            return e

a = cal(a)
print(a)
print(error(a))

