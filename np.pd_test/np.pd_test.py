#하난ㄴ 4곱하기 4 랜덤 행렬 생성, 데이터플에ㅣ으로 변환한거 하나 원형값아 하나 , 데이터 함수를 받아 정리하는 함수, 범위 이상은 exception
import numpy as np
import random
import pandas as pd
content = []
def random(content):

    content = np.random.randn(4,4)
    #df = pd.DataFrame(content)
    #print(df)
    print(content)
    return content

content1 = random(content = content)

def array(content):
    count = 0
    for i in content:

        if (-0.5<= i < -0.25):
            content[count] = -0.5

        elif -0.25 <= i < -0.1:
            content[count] = -0.25

        elif -0.1 <= i < -0.01:
            content[count] = 0


        elif 0.1 <= i < 0.25:
            content[count] = 0.25

        elif 0.25 <= i <0.5:
            content[count] = 0.5

        else:
            print("값의 범위가 초과하였습니다.")

        count = count + 1

    return content

print(array(content = content1))