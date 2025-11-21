def solution(a, b):
    ab = int(str(a) + str(b))
    ab2 = 2 * int(a) * int(b)

    if ab > ab2 :
        return ab
    elif ab < ab2 :
        return ab2
    
print(solution(2, 91)) # 364
print(solution(91, 2)) # 912
