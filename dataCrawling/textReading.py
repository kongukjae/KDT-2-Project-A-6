example = "해맑은 베어가 가족을 기다려요\n\n베어 (남아)\n\n- 2022.09.25일 출생 추정 (8개월)\n- 10kg, 미중성\n- 해맑고 밝아요\n- 노즈워크도 잘하는 똑똑이에요\n-친구를 좋아해요\n-장난감을 좋아해요\n-공놀이를 좋아해요\n-5차접종까지 완료\n- 줄산책 경험이 없어 겁이 있지만\n산책연습을 통해 충분히 좋아질 가능성이 많아요\n\n\n베어는 2개월 아가때 입양갔다가 파양되어\n얼마전 임보처로 다시 돌아왔어요.\n지금은 임보처에서 엄마강아지 조이(7kg)와 함께 지내고 있어요.\n아파트 화단에 버려진 엄마강아지에게서 태어난 4남매 중 첫번째로 입양을 갔던 아이\n입니다.\n아이에게 문제가 있어 파양된건 아니고\n입양자가 산책을 안시켜 에너지 소모가 안되었고\n그로인해 물건을 물어뜯는다는 이유로 파양되었습니다.\n\n지금 임보처에서의 베어는 그런모습을 전혀 찾아볼 수 없으며, 에너지도 엄청 많은 아이가 아닌\n그 나이의 아이들이 가지고 있는 기본적인 에너지를 가진 아이입니다.\n\n운동장에서는 매우 잘 놀고,\n공놀이도 잘하는 아이지만\n다만, 줄산책 경험이 없어 산책을 아직 무서워합니다.\n그러나 이 부분은 연습을 통해\n좋아질 가능성이 충분히 많습니다.\n\n이런경험에도 베어는 해맑고 밝은 아이이며\n친구들을 무척 좋아하고, 어린 아이들과도\n잘 지낼 정도로 순하고 사랑스러운 아이입니다.\n한번의 아픔이 있는 베어에게 정말 찐가족이 되어주실 평생가족을 기다립니다.\n\n\n마당견,실외견 X\n25살미만 X\n1인가구 X"

def agePicker(value):
    checkerList = ['','','','','']
    # 나이, 살, 세, 개월, 년
    for i in range(len(value)):
        if value[i] == ' ':
            continue
        elif i != 0 and value[i] == '살':
            pointer = i - 1
            cnt = 0
            if value[i-1].isdigit():
                    #숫자 끝나는 곳 찾는 포인터
                while value[pointer].isdigit() and cnt <= 5 and pointer >= 0 and value[pointer] != '\n':
                    pointer -= 1
                    cnt += 1
                checkerList[1] = value[pointer + 1 : i + 1]
            else:
                while value[pointer] != ' ' and cnt <= 5 and pointer >= 0 and value[pointer] != '\n':
                # 스페이스 찾는 포인터
                    pointer -= 1
                    cnt += 1
                checkerList[1] = value[pointer + 1 : i + 1]
        elif i != 0 and value[i] == '세':
            pointer = i - 1
            cnt = 0
            if value[i-1].isdigit():
                    #숫자 끝나는 곳 찾는 포인터
                while value[pointer].isdigit() and cnt <= 5 and pointer >= 0 and value[pointer] != '\n':
                    pointer -= 1
                    cnt += 1
                checkerList[2] = value[pointer + 1 : i + 1]
            else:
                while value[pointer] != ' ' and cnt <= 5 and pointer >= 0 and value[pointer] != '\n':
                # 스페이스 찾는 포인터
                    pointer -= 1
                    cnt += 1
                checkerList[2] = value[pointer + 1 : i + 1]
        elif i != 0 and value[i] == '년':
            pointer = i - 1
            cnt = 0
            if value[i-1].isdigit():
                    #숫자 끝나는 곳 찾는 포인터
                while value[pointer].isdigit() and cnt <= 5 and pointer >= 0 and value[pointer] != '\n':
                    pointer -= 1
                    cnt += 1
                checkerList[4] = value[pointer + 1 : i + 1]
            else:
                while value[pointer] != ' ' and cnt <= 5 and pointer >= 0 and value[pointer] != '\n':
                # 스페이스 찾는 포인터
                    pointer -= 1
                    cnt += 1
                checkerList[4] = value[pointer + 1 : i + 1]
        elif i >= 2:
            try:
                if value[i - 1:i+1] == '개월':
                    pointer = i - 2
                    cnt = 0
                    if value[i-1].isdigit():
                            #숫자 끝나는 곳 찾는 포인터
                        while value[pointer].isdigit() and cnt <= 5 and pointer >= 0 and value[pointer] != '\n':
                            pointer -= 1
                            cnt += 1
                        checkerList[3] = value[pointer + 1 : i + 2]
                    else:
                        while value[pointer] != ' ' and cnt <= 5 and pointer >= 0 and value[pointer] != '\n':
                        # 스페이스 찾는 포인터
                            pointer -= 1
                            cnt += 1
                        checkerList[3] = value[pointer + 1 : i + 2]
            except:
                continue
    for i in checkerList:
        if len(i) > 0:
            return i
    return '예측 불가'

if __name__ == '__main__':
    print(agePicker(example))