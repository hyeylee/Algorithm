T = int(input())
answer = list('abcdefghijklmnopqrstuvwxyz')
 
for test_case in range(1, T + 1):
    exam = list(input())
    count = 0
    for i in range(len(exam)):
        if exam[i] != answer[i]:
            break
        count += 1
 
    print('#' + str(test_case), count)