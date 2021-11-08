"""
다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
fibonacci(0)은 0을 출력하고, 0을 리턴한다.
fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

출력
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
입력
3
0
1
3

1 0
0 1
1 2
"""
def fibonacci(n):
    global zero, one
    if ( n == 0 ):
        zero += 1
        # print("0")
        return 0
    elif ( n == 1 ):
        one += 1
        # print("1")
        return 1
    else:
        return fibonacci(n -1) + fibonacci( n -2 )

if __name__ == "__main__":
    global zero, one
    inputs = list(map(int, input().split("\n")))
    CASE: int = inputs[0]
    if len(inputs[1:] == CASE):
        exit(1)
    for index in inputs[1:]:
        # zero = one = 0
        fibonacci(index)
        print( zero, one, sep=" ")

"""
이 문제는 "다이나믹 프로그래밍"을 통하여 피보나치 문제를 해결하는 것으로, 재귀 함수로만 문제를 풀 경우, 시간 제한으로 인해 오답처리가 된다.
해당 문제의 답은 아래와 같다.
https://itstory1592.tistory.com/34

여기서 다이나믹 프로그래밍에서 프로그래밍은 "테이블을 만든다"라는 뜻
이를 풀어 말하자면, 하나의 문제는 단 한번만 풀도록 하는 알고리즘으로, "한번 푼 것을 여러번 다시 푸는 비효율적인 알고리즘을 개선시키는 방법
일반적으로,분할 정복기법은 동일한 문제를 다시푸는 단점.
"""
import time

zero = [1, 0, 1]
one = [0, 1, 1]


def fibonacci_d(num):
    mmemoi_length = len(one)

    if num >= mmemoi_length:
        for index in range(mmemoi_length, num+1):
            one.append(one[index-1] + one[index-2])
            zero.append(zero[index-1] + zero[index-2])
    print('{} {}'.format(zero[num], one[num]))


inputs = list(map(int, input().split("\n")))
now = time.perf_counter()
CASE = inputs[0]

for index in inputs[1:]:
    fibonacci_d(index)
print(time.perf_counter() - now)

"""
  아니 위의 코드는 틀렸고..
  왜 참고 자료로 쓴 프로그램은 괜찮은 거지..? 이해가 안가네..
  
"""
zero = [1, 0, 1]
one = [0, 1, 1]


def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print('{} {}'.format(zero[num], one[num]))


T = int(input())

for _ in range(T):
    fibonacci(int(input()))