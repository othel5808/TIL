"""
문제
두 정수 A와 B를 입력 받은 다음, A + B를 출력하는 프로그램을 작성하시오

입력
첫째 줄에 A와 B가 주어진다( 0 < A, B < 10 )

출력
첫째줄에 A+B를 출력한다.
"""

if __name__ == "__main__":
    print("공백을 이용하여, 두 숫자를 구분하여 입력해 주세욤")
    A, B = input().split(" ")

    print(int(A) + int(B))

# 백준에서는 input 대신 map을 사용하는 것을 권장함.
"""
Map은 python의 내장 함수로 여러개의 데이터를 한번에 다른 형태로 변환하기 위해 사용됨.
주로, 여러개의 데이터를 담고 있는 list나 tuple을 대상으로 사용.

map의 기본 형태는 `map(function, iterable)` 의 형태로 구성되며, 
`function`에는 함수
`iterable`에는 반복 가능한 자료형(리스트, 튜플 등)이 오게된다. 

map함수의 반환값은 map 객체이므로, 해당 자료형을 list 혹은 tuple로 형 변환 시켜 사용해야한다.

예를 들어, 아래와 같은 데이터가 존재하고, 이 값들 중에 성과 이름을 분리하고 싶을 경우, map을 이용하여 해결이 가능하다.
users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M'},
    {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F'},
    {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M'},
    {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F'},
    {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F'}] 
    
def convert_to_name(user):
    first, last = user["name"].split()
    return {"first", first, "last", last}
    
for name in map(convert_to_name, users):
    print(name)
    
>>>{'last', 'Holland', 'Brett', 'first'}
{'last', 'Madison', 'first', 'Martinez'}
{'last', 'Jenkins', 'Michael', 'first'}
{'Rodriguez', 'last', 'first', 'Karen'}
{'Amber', 'last', 'first', 'Rhodes'}

위의 내용을 통해서, 아래와 같은 형태로 수정이 가능함
"""
if __name__ == "__main__":
    print("공백을 이용하여, 두 숫자를 구분하여 입력해 주세욤")
    A, B = map(int, input().split(" "))
    print(A+B)

# 1001 A - B
A, B = map(int, input().split(" "))
print(A-B)