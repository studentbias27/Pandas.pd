#convert into -a3b2..
s = "aaabbcdddde"
result = ""
current = s[0]
count = 1
for i in s[1:]:
    if i == current:
        count += 1
    else:
        result += current + str(count)
        current = i
        count = 1
result += current + str(count)
print(result)
        
