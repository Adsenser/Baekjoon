n = int(input())
divide_number = 10
level_count = 0
while True:
    if n / divide_number >= 1:
        divide_number *= 10
        level_count +=1
    else:
        break
past_number = 0
past_index = 0
i = 0
for i in range(1,level_count+1,1):
    past_index = 9*(10**(i-1))
    past_number += past_index*i

after_number = (n - (10**(i)-1))*(i+1)

print(past_number+after_number)