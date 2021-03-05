# Задание 1
def odd_nums(n):
    for i in range(1, n + 1, 2):
        yield i


nums1 = odd_nums(15)

print('Задание 1')
print(next(nums1))
print(next(nums1))
print(next(nums1))
print(*nums1)

# Задание 2
n = 15
nums2 = (i for i in range(1, n + 1, 2))

print('Задание 2')
print(next(nums2))
print(next(nums2))
print(next(nums2))
print(*nums2)

