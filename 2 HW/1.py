a = int(input())
s1 = 0
s2 = 0
for i range(a):
    print("Введите 1, если решка, 2")
    m = int(input())
    if m == 1:
        s1 = s1 + 1
    else:
        s2 = s2 + 1
if s1 < s2:
    print(s1)
else:
    print(s2)
