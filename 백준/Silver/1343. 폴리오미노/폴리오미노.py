import sys
line = sys.stdin.readline().rstrip()
#입력받은 후 문자열 분리 파트
temp_list = list(line)
temp_listX = []
temp_listO = []
splited_line = []
for k in range(len(temp_list)):
    if temp_list[k] == 'X':
        temp_listX.extend(temp_list[k])
        if k == len(temp_list) - 1 and temp_list[k] == 'X':
            splited_line.append(temp_listX)
    else:
        if len(temp_listX)>0:
            splited_line.append(temp_listX)
            temp_listX = []
        splited_line.append(temp_list[k])
#분리받은 문자열을 폴리오미노로 덮는 파트
result = ''
go = True
for i in splited_line:
    if go == False:
        break
    temp_count = 0
    if i == '.':
        result += '.'
        continue
    while True:
        if (len(i)-temp_count) - 4 >= 0:
            result += 'AAAA'
            temp_count += 4
        elif (len(i)-temp_count) - 2 >= 0:
            result += 'BB'
            temp_count += 2
        elif (len(i)-temp_count) == 0:
            break
        else:
            go = False
            result = -1
            break
print(result)