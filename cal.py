#for 문을 통해서 arrayval이라는 배열에 랜덤수를 10개등록 다만 이 랜덤수의 범위는 1에서 15까지 그리고 배열에 넣을 값의 범위는 7이상만 이상이면 7이상입니다, 아니면 7이하입니다.
#지금 만든 배열을 넣은 class로 만들어 ->값의 총합과 평균을 구하시오
class cal():

    def __init__(self, arrayval):
        self.arrayval = arrayval

    def custom_sum(self) :
        sumvalue = 0

        for i in self.arrayval:
            sumvalue = sumvalue + i

        return sumvalue

    def custom_avg(self) :
        """
        avgvalue = 0

        for i in self.arrayval:
            avgvalue = avgvalue + i
        """

        return self.custom_sum() / len(self.arrayval)

