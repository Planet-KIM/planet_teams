#그 함수에 입력하는 것을 쓰면 그게 켁스트로 저장 입력한 결과의 갯수가 str만, 몇개인지 세어주기. 글자수를 10개 제한하는 것 일정 글자수를 초과하면 에러발생 에러를 발생하면 에러문구 리턴
#성공하면 성공리턴
#초과흘 한 개ㅏ쑤까지만 자르고 에러는 로그 txt까지

data = str(input("문장을 입력하세요: "))

def error(e):
    error = open("C:/temp/python/planet_teams/fileread/log.txt","a")
    error.write(str(e))

def txt(data):
    count = len(list(data))
    f = open("C:/temp/python/planet_teams/fileread/fileread1.txt","a")
    f.write(data+"\n")

    try:

        if count <= 10:
            C = print("{count}개 입니다.".format(count = count))

        else:
            raise Exception("입력 갯수 10개를 초과하였습니다.\n")

    except Exception as e:
        print(e)
        error(e=e)
        return e

txt(data=data)

