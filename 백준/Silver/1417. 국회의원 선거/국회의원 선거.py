n = int(input())
people = []
for _ in range(n):
    people.append(int(input()))
first_person = people[0]
person = people[0]
del(people[0])
while True:
    try:
        if person > max(people):
            break
        max_index = people.index(max(people))
        people[max_index] -= 1
        person += 1
    except:
        break
print(person-first_person)