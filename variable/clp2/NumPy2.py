import random   
values = [random.randint(1, 1000) for _ in range(100)]
min_value = min(values)
max_value = max(values)
normalized_values = [(x - min_value) / (max_value - min_value) for x in values]
print("Original Values:", values)
print("\nNormalized Values:", normalized_values)
