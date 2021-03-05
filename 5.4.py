src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

'''
nums = []
for i, v in enumerate(src[1:]):
    if v > src[i]:
        nums.append(v)
'''
# С помощью среза, расходуется память на копию строки
nums = [v for i, v in enumerate(src[1:]) if src[i]<v]

print(nums)

'''
nums = []
for i, v in enumerate(src):
    if i>0:
        if v > src[i-1]:
            nums.append(v)
'''
# Без срезов
nums = [v for i, v in enumerate(src) if i > 0 if v > src[i-1]]

print(nums)

