def isPalin(s):
    if s==s[::-1]:
        return 1
    return 0
def rightShift(s):
    return s[1:]+s[:1]
def leftShift(s):
    return s[-1:]+s[:-1]
t=int(input())
for _ in range(t):
    string=input()
    shift=0
    left_word,right_word=string,string
    while(shift<=len(string)//2):
        if isPalin(left_word) or isPalin(right_word):
            print(shift)
            break
        left_word=leftShift(left_word)
        right_word=rightShift(right_word)
        shift+=1
    else:
        print(-1)
        





