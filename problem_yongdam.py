# Q. 주어진 window size W와 input sequence S에 대해서, S에 포함된 숫자들을 살펴보려 합니다.
# 스캔하는 동안엔 한 번에 연속된 W의 크기의 숫자들만 볼 수 있습니다.
# W와 S가 주어지면, 스캔해서 얻을 수 있는 숫자들의 최대합을 출력하는 함수를 작성하세요.
# 합을 계산하는 대상은 W개의 숫자들입니다.

######### INPUT ##########
# input은 순서대로 W, N, S1, S2, ... , SN이 들어옵니다.
# W는 window size, N은 들어오는 input sequence S의 개수, S1, S2, ..., Si, ... , SN은 N개의 input sequence입니다.
# W는 0 ~ 10,000 의 범위를 가집니다.
# N은 0 ~ 100의 범위를 가집니다.
# 각 input sequence Si는 빈 칸을 기준으로 숫자들이 나열되어 있습니다.
# Si는 최소 W개 이상, 100개 이하의 숫자들을 가집니다.
# Si의 각 숫자들은 -1000 ~ 1000의 범위를 가집니다.


######## OUTPUT ########
# 각 S1, S2, ..., SN에서 숫자들을 순서대로 W만큼씩 스캔했을 때, 합의 최대값을 출력합니다.

##### TESTCASE #####
# 함께 제공되는 예제의 정답입니다.
"""
input :
3
3
1 2 3 4 5 6 7 8 9
-1 1 0 1 2 3 4 5 6
0 1 2 49 19 -2 3 45
output :
24
15
70
"""


def solution(testcase):

    ### TO-DO:
    ###  문제 풀이에 해당하는 코드를 작성하세요.
    # 주어진 입력 데이터가 solution 함수의 입력으로 들어온다고 가정합니다.
    # testcase는 숫자 하나가 들어온다고 가정합니다.
    # 데이터를 불러와서 정답을 print하는 solution 함수를 완성하세요.

    ### testcase가 구구단의 단 이라고 생각하고, 해당 단을 print문을 사용하여 출력하는 코드를 작성하세요.
    # e.g. testcase = 2, 2단을 출력하세요.

    for number in range(1, 10):
        print("%d X %d = %d" % (testcase, number, testcase*number))

    return


solution(2)
solution(5)
solution(9)