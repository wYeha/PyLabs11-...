a = {}
for _ in range(int(input())):
    s = input().split()
    country = s[0]
    cityes = s[1:]
    for city in cityes:
        a[city] = country
for i in range(int(input())):
    print(a[input()])
   