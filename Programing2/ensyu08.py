from random import randint

target_list = [randint(1, 1000) for _ in range(10)]

print(target_list)
for count in range(len(target_list)):
    for i in range(len(target_list) - 1 - count):
        if target_list[i] > target_list[i + 1]:
            target_list[i], target_list[i + 1] = target_list[i + 1], target_list[i]
print(target_list)



