def define_dict():
    """
    dict 정의
    """
    # 타입 함수를 이용한 생성
    dct = dict()  # 빈 dict
    print(dct, type(dct))
    # 리터럴 생성
    dct = {}      # 빈 dict
    print(dct, type(dct))
    # 키워드 인수로 생성
    dct = dict(one=1, two=2)
    print(dct, type(dct))
    # 키, 값 깡 튜플의 목록으로 생성
    dct = dict([("one", 1), ("two", 2), ("three", 3)])
    print(dct)

    # 키목록과 값목록이 별도로 있을 때 두 목록을 합쳐서 dict 생성
    keys = ('one', 'two', 'three', 'four')
    values = (1, 2, 3)
    dct = dict(zip(keys, values))  # 키목록과 값목록을 합쳐서 dict에 전달
    print(dct)


def dict_oper():
    """
    dict의 연산
    키를 통한 접근, 가변 자료형
        len, in, not in
        기본적 연산 대상은 keySet
    """

    dct = {"baseball": 9, "basketball": 5}
    # 키를 통한 접근
    dct['soccer'] = 11
    print(dct, type(dct))

    # 순서가 없음: 인덱싱, 슬라이싱 불가
    # 길이, 포함 여부 확인 가능
    print(dct, "LENGTH:", len(dct))
    print("baseball" in dct)
    print("soccer" in dct)
    print("volleyball" in dct)

    # 포함 여부를 값 목록에서 확인할 경우 .values()
    print(9 in dct.values())

    # .keys() : key set를 받아올 수 있음
    # .values() : value 목록을 받아올 수 있음
    # .items() :(키, 값) 목록을 받아올 수 있음

    # dic의 키 : 해싱되야 하므로 immutable 자료여야함
    dct[True] = "true"
    dct[10] = 10
    dct["eleven"] = 11
    dct[1, 2, 3] = 6


def dict_methods():
    """
    dict의 메서드를
    """
    dct = {"baseball": 9, "basketball": 5, "soccer":11}
    print(dct, type(dct))

    # set(key)-list(value) 랍쳐진 복합 자료형
    keys = dct.keys()
    print(keys, type(keys))  # dict_key
    # dict_key도 순차 자료형: set, list 타입 함수로 변환 후 순차형으로 사용 가능
    lst_keys = list(keys)
    print(lst_keys, type(lst_keys))

    # 값의 목록 : .values() # dict_values
    values = dct.values()
    print(values, type(values))

    # (키, 값) 튜플의 목록 : .items() #dict_items
    items = dct.items()
    print(items, type(items))
    lst_items = list(items)

    print("key:", lst_items[1][0], ", value:", lst_items[1][1])

    # dict 배우기
    dct.clear()
    print(dct)


def using_dict():
    """
    dict 사용 방법
    """
    phones = {
        "둘리": "010-1234-5678",
        "도우너": "010-9876-5432",
        "또치": "010-2222-3333"
    }
    print(phones)

    # 키 접근 vs get() 메서드
    print("둘리 전화번호:", phones["둘리"])
    # print("고길동 전화번호:", phones["고길동"])  # 없는 키에 접근하면 KeyError
    print("고길동 전화번호:", phones.get("고길동", "몰라요"))

    # 아이템 삭제
    del phones['또치']

    # 아이템을 가져오고 동시에 삭제 : pop
    item = phones.pop("도우너")
    print(item)
    print(phones)


def loop():
    """
    사전의 순회(loop) : 기본적으로 keySet 대상
    """
    phones = {
        "둘리": "010-1234-5678",
        "도우너": "010-9876-5432",
        "또치": "010-2222-3333"
    }

    # 기본적인 루프
    for key in phones:
        print(f"{key}: {phones.get(key)}")

    for key in phones.keys():
        print(f"{key}: {phones.get(key)}")

    print("items:", phones.items())
    for key, value in phones.items():  # (키, 값)
        print(f"{key}: {value}")


if __name__ == "__main__":
    # define_dict()
    # dict_oper()
    # dict_methods()
    # using_dict()
    loop()