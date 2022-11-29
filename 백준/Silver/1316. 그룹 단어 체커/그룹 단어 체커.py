import sys
n = int(input())
count = 0
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    set_word = set(word)
    list_word = list(set_word)
    last_word = word[0]
    error = 0
    for i in range(1,len(word)):
        if last_word == word[i]:
            continue
        else:
            try:
                list_word.remove(last_word)
            except:
                count -= 1
                break
            if len(list_word) != 0:
                for j in list_word:
                    if word[i] == j:
                        last_word = word[i]
                        break
            else:
                count -= 1
                break
result = n + count
print(result)