import os
import shutil
A = input("찾고싶은 파일을 검색하세요: ")

def array(A):

    #파일경로
    pth = os.path.dirname(os.path.realpath(__file__))

    #pth의 주소 안에 있는 파일을 목록화 시켜 리스트로 담아주기
    listfiles = os.listdir(pth)
    content = []

    #listfile의 요소를 하나씩 출력
    for i in listfiles:
        #print(i)=목록보여주기
        #요소를 .을 기준으로 나누고 args의 변수로 담기
        args = i.split(".")
        content.append(args[1])

        #args의 1번째가 py일 조건
        if args[1] == A:
            print(i)


    new = []
    for i in content:

        if i not in new:
            new.append(i)

    print(new)

    for i in new:
        folder = os.path.join(pth, i)
        os.mkdir(folder)
        for j in listfiles:
            s = i.split(".")
            if s[1] in folder:
                shutil.move(os.path.join(pth, j),folder)
array(A=A)