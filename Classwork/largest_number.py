def largest_number(smallest_number, medium_number, large_number):
    largest_number = smallest_number
if medium_number > smallest_number:
    largest_number = medium_number
elif large_number > medium_number:
    largest_number = large_number
 return largest_number

print(largest_number(10, 100, 50))
