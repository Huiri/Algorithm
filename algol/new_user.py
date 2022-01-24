import re

def solution(new_id):
    new_id = new_id.lower()
    # 특수문자 제거
    new_id = re.compile('[^a-z0-9_|-|-.]+').sub('', new_id)
    # 중복 문자 제거
    new_id = re.sub('\.+', '.', new_id)
    # 처음과 끝 . 제거
    if (new_id[0] == '.'):
        # 아무것도 안 남았을 때 a넣기
        # (.만 남아있는 경우는 제거함 -> 길이가 0인 경우 a 추가함
        if (len(new_id) == 1):
            new_id = 'a'
        else:
            new_id = new_id[1:len(new_id)]
    if (new_id[len(new_id) - 1] == '.'):
        new_id = new_id[0:len(new_id) - 1]
    # 길이가 15 이상이면 자르기
    if (len(new_id) >= 16):
        new_id = new_id[0:15]
        #자른 후 마지막 글자가 .인 경우 삭제
        if (new_id[len(new_id) - 1] == '.'):
            new_id = new_id[0:len(new_id) - 1]
    # 길이가 3보다 작을 경우 마지막 글자 반복하기
    if (len(new_id) < 3):
        new_id = new_id + new_id[len(new_id) - 1] * (3 - len(new_id))
    return new_id