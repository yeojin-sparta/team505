# comment

# let num = 100
num = 100
# true/false
boolean = True  # False

print('hello')

# 리스트, 딕셔너리는 js 동일
num_list = [10, 20, 30, 40]  # num_list[0] -> 10
num_dict = {'num1': 100, 'num2': 200}  # num_dict['num1'] -> 100

def sum(num1, num2):
    return num1 + num2

result = sum(100, 200)

print(result)

# js와 다르게 && -> and // || -> or
if (10 > 20 and 20 > 30) or (30 == 40 and 50 != 60):
    print('hahaha')

numbers = [1, 2, 3]
# for (int i = 0; i < numbers.length; i++) {
#     console.log(i)
# }

for number in numbers:
    print(number)
