#BeautifulSoup를 파이썬 라이브러리로 인식하게 설정
from bs4 import BeautifulSoup
#-url을 여는 함수
from urllib.request import urlopen

#urlopen 함수를 사용하여 원하는 주소로부터 웹페이지를 가져옴
html = urlopen('https://elwlsek.tistory.com/1586')
#위의 html 문자열에 대해서, html 파싱
bs = BeautifulSoup(html,'html.parser')

#study라는 클래스 생성
class study():
    #생성자__init__으로 self와 a 를 인자로 지정
    def __init__ (self, a):
        self.a = a

    #정확히 잘모르겠습니다
    def aprintf(self):
        #content 라는 list 생성
        content = []
        count = 1

        #속성값을 기준으로 해당 태그를 불러온다
        for i in bs.find_all('p', {'align': 'center'}):

            #문자열 데이터를 보여준다
            content.append(i.get_text())

            #리스트를 4로 나눈 나머지가 2인 길이
            if len(content) % 4 == 2:

                country = i.get_text()
                #문자열의 대괄호 자리에 괄호안에 들어있는 값을 하나씩 대입한다
                print("{count}, 국가:{this}".format(count=count, this=country))
                count = count + 1


            # 리스트를 4로 나눈 나머지가 0인 길이
            if len(content) % 4 == 0:
                dollar = i.get_text()
                # 문자열의 대괄호 자리에 괄호안에 들어있는 값을 하나씩 대입한다
                print("\tUSD:{this}".format(this = dollar))



            # count가 30 초과이면 break
            if len(content) > 120:
                break

#해당 class를 불러온다
study(a='https://elwlsek.tistory.com/1586').aprintf()





