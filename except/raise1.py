def raisetest():

    try:
        integer = int(input('2의 배수를 입력하세요 : '))
        
        if (integer % 2) != 0:
            raise Exception('2의 배수가 아닙니다.')
        print(integer)

    except Exception as e:
        print('raisetest 함수에서 예외가 발생했습니다.', e)
        raise

try:
    raisetest()
except Exception as e:
    print('스크립트 파일에서 예외가 발생했습니다.', e)


