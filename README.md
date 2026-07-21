# Leetcode-Questions

This repository contains my personal solutions to LeetCode problems written in Python 3, serving as a log of my practice with data structures and algorithm design. 

Every individual Python file contains the complete problem statement, a brief explanation of the approach used, time and space complexity evaluations, and a runnable test case within a standard execution block. 

To test any solution locally, clone the repository using `git clone https://github.com/your-username/leetcode-python.git`, navigate to the project directory, and execute the desired file directly using `python Easy/0001_two_sum.py`. 

This project is licensed under the MIT License and is open for personal reference, learning, and review.


I have solved the LeetCode Questions from the leetcode platform and written the codes in the best possible way for the particular question.



---

## 📌 Repository Questions

The repository is organized by problem number or difficulty levels. Each `.py` file corresponds to a problem, clean code, and comments explaining the approach.

```text
.
├── Easy/
│   ├── 0001_two_sum.py
│   ├── 0020_valid_parentheses.py
│   └── ...
├── Medium/
│   ├── 0002_add_two_numbers.py
│   ├── 0015_3sum.py
│   └── ...
├── Hard/
│   ├── 0004_median_of_two_sorted_arrays.py
│   └── ...
└── README.md

```

---

## <p style="font-size: 35px;">💡 Code Template </p>

Each .py file follows a consistent structure:


``` python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


```

---
