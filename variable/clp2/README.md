
## 1. List: Remove Duplicates and Sort in Ascending Order

### **Code:**
```python
numbers = [4, 2, 7, 3, 2, 4, 9, 1, 5]
unique_sorted_numbers = sorted(set(numbers))
print(unique_sorted_numbers)
```

### **Explanation:**
- `set(numbers)`: Removes duplicate elements since sets do not allow duplicates.
- `sorted()`: Sorts the unique numbers in ascending order.
- **Output Example:** `[1, 2, 3, 4, 5, 7, 9]`

---

## 2. Set: Find Common Elements Between Two Lists

### **Code:**
```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = set(list1) & set(list2)
print(common_elements)
```

### **Explanation:**
- `set(list1) & set(list2)`: Finds the intersection (common elements) between both lists.
- **Output Example:** `{4, 5}`

---

## 3. Tuple: Create a Tuple of Student Records and Sort by Grade

### **Code:**
```python
students = [("Rana", 20, 85),
    ("Riyad", 22, 78),
    ("Rony", 21, 92),
    ("Emtiaz", 23, 88),
    ("Mishal", 19, 76)]
sorted_students = sorted(students, key=lambda x: x[2])
print(sorted_students)
```

### **Explanation:**
- `students`: List of tuples containing student name, age, and grade.
- `sorted(students, key=lambda x: x[2])`: Sorts students by **grade** (third element in each tuple).
- **Output Example:** `[("Bob", 22, 78), ("Alice", 20, 85), ("Charlie", 21, 92)]`

---

## 4. Dictionary: Count Word Occurrences in a Given Text

### **Code:**
```python
text = "hello world hello python world python"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
```

### **Explanation:**
- `text.split()`: Splits text into words.
- `word_count.get(word, 0) + 1`: Counts occurrences of each word.
- **Output Example:** `{'hello': 2, 'world': 2, 'python': 2}`

---

## 5. NumPy #1: Generate a 5x5 Matrix of Random Integers and Compute Row-Wise Sums

### **Code:**
```python
import numpy as np
matrix = np.random.randint(1, 100, (5, 5))
row_sums = np.sum(matrix, axis=1)
print("Matrix:", matrix, "\nRow-wise sums:", row_sums)
```

### **Explanation:**
- `np.random.randint(1, 100, (5, 5))`: Creates a 5×5 matrix with random integers between 1 and 100.
- `np.sum(matrix, axis=1)`: Computes sum of each row.
- **Output Example:**
```
Matrix:
[[10 20 30 40 50]
 [15 25 35 45 55]
 [11 22 33 44 55]
 [16 26 36 46 56]
 [12 24 36 48 60]]
Row-wise sums: [150 175 165 180 180]
```
---
## 6. NumPy #2: Create an Array of 100 Random Values and Normalize Them Between 0 and 1

### **Code:**
```python
import numpy as np
values = np.random.rand(100)
normalized_values = (values - np.min(values)) / (np.max(values) - np.min(values))
print("Original Values:", values, "\nNormalized Values:", normalized_values)
```

### **Explanation:**
- `np.random.rand(100)`: Generates 100 random values between 0 and 1.
- `(values - np.min(values)) / (np.max(values) - np.min(values))`: Normalizes values.
- **Output Example:** Normalized values between 0 and 1.