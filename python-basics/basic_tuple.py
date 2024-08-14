def define_tuple():
    """
    튜플의 정의
    tuple: 리스트와 거의 동일, 변경 불가 자료(immutable)
        len, 인덱싱, 슬라이싱, 연결, 반복, 포함 여부
        내부 요소 변경 불가
    """
    tp1 = ()  # 공튜플
    tp2 = tuple()  # 공튜플
    print(tp1, type(tp1))
    print(tp2, type(tp2))
    tp3 = (1,)  # 요소가 1개일 경우, 요소 뒤에,
    print(tp3, type(tp3))


def tuple_oper():
    """
    튜플 연산
    """
    tp = (1, 2, 3, 4, 5)
    # 길이를 구할 수 있다
    print(tp, "LENGTH:", len(tp))
    # 인덱싱
    print(tp[-3], tp[-2], tp[-1],  # 역방향 인덱싱
          tp[0], tp[1], tp[2], tp[3])  # 정방향 인덱싱

    # 슬라이싱 : [시작경계:끝경계[:간격]]
    slice = tp[1:4]
    print(slice, type(slice))
    slice = tp[:]  # 처음부터 -> 생략 가능, 끝까지 -> 생략 가능, [:] -> 튜플 전체
    print(slice)

    # 반복 *
    print(tp * 3)

    # 연결 +
    print(tp + (6, 7, 8, 9, 10))

    # 포함 여부 : in, not in
    print(5 in tp)  # 5가 포함?
    print(1 not in tp)  # 1이 포함 안됨?


def tuple_assign():
    """
    튜플의 할당
    """
    # 튜플을 이용, 좌우변의 여러 값을 동시 할당
    x, y, z = 10, 20, 30  # 튜플
    print(x, y, z)

    # 튜플을 이용한 swap(값 교환)
    x, y = 10, 20
    print(x, y)
    x, y = y, x  # 튜플을 이용한 교환
    print(x, y)


def tuple_method():
    """
    튜플의 메서드들
    """
    tp = (20, 30, 10, 20)
    print("count:", tp.count(20))  # 요소 갯수
    print("index:", tp.index(20))  # 요소의 인덱스
    print("index:", tp.index(20, 1))  # 요소의 인덱스, 범위 제한


def packing_unpacking():
    """
    튜플 패킹과 언패킹
    """
    # 튜플의 Packing
    tp = (10, 20, 30, "Python")  # 기본적으로 튜플 생성법
    print(tp, type(tp))
    tp = 10, 20, 30, "Python"    # 값만 나열해도 자동으로 튜플로 인식
    print(tp, type(tp))

    # 기본 unpacking
    a, b, c, d = tp
    print(a, b, c, d)

    # a, b, c = tp  # 좌변의 변수 개수 적음 -> ValueError
    # a, b, c, d, e = tp  #좌변의 변수 개수 많음 -> ValueError

    # 확장 언패킹
    a, *b = tp  # 확장 언패킹 기호 *
    print(a, type(a))
    print(b, type(b))

    *a, b = tp
    print(a, type(a))
    print(b, type(b))

    a, *b, c = tp
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))




if __name__ == "__main__":
    # define_tuple()
    # tuple_oper()
    # tuple_assign()
    # tuple_method()
    packing_unpacking()