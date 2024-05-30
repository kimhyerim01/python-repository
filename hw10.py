import pickle
import os

filepath = 'score.bin'

    
def input_scores() :
    scores = []
    i = 0
    while True :
        n = int(input(f'#{i+1}? '))
        if n < 0 : #if문이 append 뒤에 쓰이면 리스트에 추가가 된 후에 음수인지 판별하기 때문에 음수도 추가된다. if문은 append 하기 전에
            break
        scores.append(n)
        i += 1

    return scores


def get_average(scores) :
    avg = 0
    for n in scores :
        avg += n

    return avg / len(scores)


def show_scores(scores) :
    for n in scores :
        print(n, end = ' ')
    print()

def search(lst, n) :
    if n not in lst :
        return None

    return lst.index(n)
    
if os.path.exists(filepath):
    with open(filepath, 'rb') as file:
        s2 = pickle.load(file)
        print('[파일 읽기]\n')
        print('[점수 출력]\n개인점수: ', end = ' ')
        show_scores(s2)
        avg = get_average(s2)
        print(f'평균 : {avg:.1f}')
else:       
    print('[점수 입력]')
    scores = input_scores()
    print('\n[점수 출력]\n개인점수: ', end = ' ')
    show_scores(scores)
    avg = get_average(scores)
    print(f'평균 : {avg:.1f}')

    with open(filepath, 'wb') as file:
        s1 = scores
        pickle.dump(s1, file)
