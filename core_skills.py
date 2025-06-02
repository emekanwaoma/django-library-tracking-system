import random

random_numbers = [random.randint(1,20) for _ in range(10)]

nums_below_ten_lc = [num for num in random_numbers if num < 10]

nums_below_ten_filter = list(filter(lambda x: x < 10, random_numbers))