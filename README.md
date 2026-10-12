
# Python Programming Assessment

This repository contains solutions to three Python programming tasks.

## Requirements

- Python 3.8 or later
- No third-party packages required

## Task 1: Command-Line Banking System

**File:** `task1_banking_system.py`

An object-oriented banking system that supports:
- Creating multiple customer accounts.
- Unique account numbers.
- Password authentication.
- Depositing and withdrawing money.
- Viewing account details and balances.
- Listing all accounts.

### Run

```bash
python task1_banking_system.py
```

### Video explanation

[Watch the Task 1 code walkthrough](PASTE_TASK_1_VIDEO_URL_HERE)

## Task 2: Longest Substring Without Repeating Characters

**File:** `task2_longest_substring.py`

Uses a sliding-window algorithm and a dictionary to find the length of the longest substring without repeated characters.

### Run

```bash
python task2_longest_substring.py
```

### Example

```python
lengthOfLongestSubstring("abcabcbb")  # 3
lengthOfLongestSubstring("bbbbb")     # 1
lengthOfLongestSubstring("pwwkew")    # 3
```

### Complexity

- Time: O(n)
- Space: O(k), where k is the number of distinct characters tracked.

### Video explanation

[Watch the Task 2 code walkthrough](PASTE_TASK_2_VIDEO_URL_HERE)

## Task 3: Longest Palindromic Substring

**File:** `task3_longest_palindrome.py`

Uses the expand-around-center technique to find the longest substring that reads the same forwards and backwards.

### Run

```bash
python task3_longest_palindrome.py
```

### Example

```python
longestPalindrome("babad")  # "bab" or "aba"
longestPalindrome("cbbd")   # "bb"
longestPalindrome("racecar") # "racecar"
```

### Complexity

- Time: O(n^2)
- Auxiliary space: O(1), excluding the returned substring.

### Video explanation

[Watch the Task 3 code walkthrough](PASTE_TASK_3_VIDEO_URL_HERE)