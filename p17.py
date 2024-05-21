input_num = input ('Enter number separated by spaces: ')
enter_list = []
squar_list = []


for i in range(0, len(input_num), 1):
    if(i % 2 == 0):
        x = input_num[i]
        enter_list.append(x)

for j in range(0, len(enter_list), 1):
    y = int(enter_list[j])
    squar_list.append(y ** 2)
    
print('Squared numbers: ', squar_list)
