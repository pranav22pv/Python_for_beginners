from utils import get_input
from utils import find_max
from utils import find_min

numbers = get_input()
print(numbers)
maximum = find_max(numbers)
print(f"{maximum} is the largest number")
minimum = find_min(numbers)
print(f"{minimum} is the smallest number")