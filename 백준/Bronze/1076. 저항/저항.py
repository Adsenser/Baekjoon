value = []
multiple = []
for i in range(10):
    value.append(i)
    multiple.append(10**i)

color1 = str(input())
color2 = str(input())
color3 = str(input())

if color3 == 'black':
    result3 = multiple[0]
if color3 == 'brown':
    result3 = multiple[1]
if color3 == 'red':
    result3 = multiple[2]
if color3 == 'orange':
    result3 = multiple[3]
if color3 == 'yellow':
    result3 = multiple[4]
if color3 == 'green':
    result3 = multiple[5]
if color3 == 'blue':
    result3 = multiple[6]
if color3 == 'violet':
    result3 = multiple[7]
if color3 == 'grey':
    result3 = multiple[8]
if color3 == 'white':
    result3 = multiple[9]

if color2 == 'black':
    result2 = value[0]
if color2 == 'brown':
    result2 = value[1]
if color2 == 'red':
    result2 = value[2]
if color2 == 'orange':
    result2 = value[3]
if color2 == 'yellow':
    result2 = value[4]
if color2 == 'green':
    result2 = value[5]
if color2 == 'blue':
    result2 = value[6]
if color2 == 'violet':
    result2 = value[7]
if color2 == 'grey':
    result2 = value[8]
if color2 == 'white':
    result2 = value[9]

if color1 == 'black':
    result1 = value[0]
if color1 == 'brown':
    result1 = value[1]
if color1 == 'red':
    result1 = value[2]
if color1 == 'orange':
    result1 = value[3]
if color1 == 'yellow':
    result1 = value[4]
if color1 == 'green':
    result1 = value[5]
if color1 == 'blue':
    result1 = value[6]
if color1 == 'violet':
    result1 = value[7]
if color1 == 'grey':
    result1 = value[8]
if color1 == 'white':
    result1 = value[9]

final_result = result3*result2 + result3*10*result1
print(final_result)

