list_ = []  # 빈 리스트 선언

for i in range(1, 10001):  # 1부터 ~ 10000까지 돌기
    a = i  # a라는 변수에 i 값 대입
    for j in str(i):  # i를 문자열로 바꾸어 각각의 자리수에 접근
        a += int(j)  # 문자열로 바꾼 i를 다시 int형으로 바꾸어 a에 더해준다.
    list_.append(a)  # 그 값을 list에 추가
    if i not in list_:  # 만약 리스트에 i 값이 없다면
        print(i)  # 그 값은 셀프넘버이므로 출력
