n = int(input())
if n > 3:
    o_count = 1
    i_count = 1
    for _ in range(n-3):
        temp_o = o_count + i_count
        temp_i = o_count
        o_count = temp_o
        i_count = temp_i
    print(o_count + i_count)
elif n == 3:
    print(2)
else:
    print(1)