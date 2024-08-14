# list는 모든 시퀀스의 시퀀스
# 시퀀스의 모든 연산 작업을 수행
def define_list():
    """
    리스트 생성 관련 샘플 코드
    """
    lst1 = list()  # 타입 함수를 이용한 생성
    print(lst1, type(lst1))
    lst2 = []  # [] -> 리스트 표기법 -> 추천하는 생성법
    lst3 = [1, 2, "Python"]  # 객체 타입을 가리지 않음
    print(lst2, lst3)

    lst4 = list("Python")
    print(lst4)  # 다른 시퀀스 자료형을 리스트로 변환

def list_oper():
    """
    리스트는 len, 인덱싱, 슬라이싱, in, not in, 내부데이터 치환 가능
    리스트 연산 연습
    """
    lst = [1, 2, "Python"]

    print(lst, "Length:", len(lst))  # 길이의 확인
    print(lst[0], lst[1], lst[2])    # 정방향 인덱싱
    print(lst[-1], lst[-2], lst[-3]) # 역방향 인덱싱

    # 슬라이스 : [시작경계:끝경계[:간격값]]
    print(lst[1:3])  # == [2, "Python"]
    print(lst[1:])   # 끝경계가 생략되면 끝까지
    print(lst[0:2])  # == [1, 2]
    print(lst[:2])   # 시작경계가 생략되면 처음부터

    cp = lst[:]      # 원본 전체의 copy -> 슬라이스를 활용한 전체의 복제
    print(cp)
    print(cp is lst, cp == lst)

    # 연결 +
    print(lst + ["Java", True, 3.14159])

    # 반복 *
    print(lst * 3)

    # append vs extend
    print(cp)
    cp.append(["Java", True, 3.14159])  # 맨 뒤에 요소 추가
    print(cp)
    cp.extend(["Java", True, 3.14159])  # 맨 뒤에 새 리스트를 확장
    print(cp)
    cp.insert(2, [1, 2, 3])
    print(cp)

    # 포함 여부 확인
    print("Python" in cp)

    # cp 내부에서 Python의 인덱스 확인
    print("INDEX:", cp.index("Python"))

    if "HTML" in cp:
        print("INDEX HTML:", cp.index("HTML"))
    else:
        print("HTML not found")

    # 항목 개수 확인
    print("COUNT:", cp.count('Python'))

    # 요소의 삭제
    del cp[0]
    print(cp)
    # 요소의 삭제: remove
    cp.remove("Python")
    print(cp)

    # list는 immutable이다

    # slicing 활용
    lst2 = ["apple", "banana", 10, 20]
    print("lst2:", lst2)
    # slicing을 이용한 치환
    lst2[0:2] = [10, 20]
    print(lst2)
    lst2[:2] = [10]
    print(lst2)
    lst2[1:2] = [20]
    print(lst2)
    lst2[2:] = [30]
    print(lst2)

    # 슬라이싱을 이용한 삽입(insert)
    lst3 = [1, 12, 123, 1234]
    print("lst3:", lst3)
    lst3[1:1] = ['a']  # 중간에 삽입
    print(lst3)
    lst3[5:] = [12345] # 맨 뒤에 삽입
    print(lst3)
    lst3[:0] = [0]  # 맨 앞에 삽입
    print(lst3)

    # 슬라이싱을 이용한 삭제
    lst3 = [1, 12, 123, 1234]
    print("lst3:", lst3)
    lst3[1:3] = []
    print(lst3)

    # 기초 산술 함수를 지원
    lst4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("lst4:", lst4)
    print("sum:", sum(lst4))
    print("min, max:", min(lst4), max(lst4))
    print("average:", sum(lst4) / len(lst4))

def list_methods():
    """
    리스트의 메서드들: reverse, sort
    """
    print("===== reversed vs reverse")
    lst = [10, 2, 22, 9, 8, 33, 4, 12]
    print("원본:", lst)
    lst_copy = lst.copy()  # 복제본 생성, 원본데이터 유지

    # 반전(reverse)
    print("REVERSED:", list(reversed(lst_copy)))   # reversed : 원본 유지 데이터 순서 반전 -> 새 리스트
    print("lst_copy:", lst_copy)
    print("REVERSE:", lst_copy.reverse())  # reverse : 내부 데이터를 뒤집는 역할 -> 내부 데이터 변경
    print("lst_copy:", lst_copy)

    print("===== sorted vs sort")
    lst_copy = lst.copy()  # 복제본 생성
    print("lst_copy:", lst_copy)

    print("lst_copy sorted:", sorted(lst_copy))  # 오름차순 정렬
    print("lst_copy:", lst_copy)  # 내부 데이터 변경되지 않음
    print("lst_copy sorted desc:", sorted(lst_copy, reverse=True))  # 내름차순 정렬
    print("lst_copy:", lst_copy)  # 내부 데이터 변경되지 않음

    # key 함수: 정렬 기준을 정의한 로직
    print("lst_copy sorted key int:", sorted(lst_copy, key=int))
    print("lst_copy sorted key str:", sorted(lst_copy, key=str))

    # 키 함수 -> 10으로 나눈 나머지의 역순 정렬
    def key_func(val):
        return val % 10

    print("lst_copy sorted key=key_func desc",
          sorted(lst_copy, key=key_func, reverse=True))
    print("lst_copy:", lst_copy)  # 내부 데이터 변경되지 않음

    # sorted 함수: 원본 유지, 데이터 정렬한 새 리스트 반환
    # sort 메서드: 내부 데이터를 실제로 정렬함
    lst_copy.sort(key=key_func, reverse=True)
    print("lst_copy:", lst_copy)

def stack_ex():
    """
    리스트를 활용 stack 자료형 흉내내기
    stack : last Input First Output (LIFO: 후입 선출)
    - append : 맨 뒤에 요소 추가
    - pop : 맨 뒤의 요소 추출
    """

    stack = []
    stack.append(10)
    print("Stack:", stack)
    stack.append(20)
    print("Stack:", stack)
    stack.append(30)
    print("Stack:", stack)

    print(stack.pop())
    print(stack.pop())

    print("Stack:", stack)

def queue_ex():
    """
    리스트를 활용한 queue 자료형 흉내내기
    QUEUE : First Input First Output (FIFO : 선입선출)
    - append : 입력
    - pop(0) : 인출
    """
    queue = []
    # 입력
    queue.append(10)
    queue.append(20)
    queue.append(30)

    print("QUEUE:", queue)

    print(queue.pop(0))  # 가장 앞 요소를 인출
    print(queue.pop(0))

    print("QUEUE:", queue)

def loop():
    """
    순차 자료형의 순회
    for 변수 in 순차형: 별도 인덱스 변수는 없음
    """
    words = "Life is too short, You need Python.".replace(",", "")\
             .replace(".","").split()
    print("목록:", words)

    for word in words:
        print(word)


if __name__ == "__main__":
    # define_list()
    # list_oper()
    # list_methods()
    # stack_ex()
    # queue_ex()
    loop()