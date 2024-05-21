outStr =""
count, i = 0, 0

inStr = input("Type string: ")
count = len(inStr)

for i in range(0, count):
    outStr += inStr[count - (i + 1)]

print('Reversed string: %s' % outStr)