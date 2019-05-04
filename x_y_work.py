import math
f = open('x_y_input.txt', 'r')
people_num = []
for i in range(16):
    people_num.append(float(f.readline()))
# print(people_num)
axis = []
mean_x = 0
mean_y = 0
for i in range(16):
    str_tmp = f.readline()
    str_tmp = str_tmp.replace('\n', '')
    list_tmp = str_tmp.split(',')
    num_list = []
    for word in list_tmp:
        num_list.append(float(word))
    mean_x += num_list[0]
    mean_y += num_list[1]
    # print(num_list)
    axis.append(num_list)

learning_rate = 1e-10
x = mean_x / 16
y = mean_y / 16
# print('x=', x)
# print('y=', y)
flag = True
while flag:
    dx = 0
    dy = 0
    for i in range(16):
        xi = axis[i][0]
        yi = axis[i][1]
        if x >= xi:
            dx += math.sqrt(people_num[i])
        else:
            dx -= math.sqrt(people_num[i])
        if y >= yi:
            dy += math.sqrt(people_num[i])
        else:
            dy -= math.sqrt(people_num[i])
    x -= learning_rate * dx
    y -= learning_rate * dy
    if dx < 1e-4:
        break
print('x=', x)
print('y=', y)
