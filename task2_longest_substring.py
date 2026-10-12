
def lengthOfLongestSubstring(s: str) -> int:
    """
    Return the length of the longest substring
    without repeating characters.
    """
    last_seen = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        # Move the window past the repeated character.
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        # Record the most recent position of this character.
        last_seen[char] = right

        # Update the longest valid substring length.
        current_length = right - left + 1
        max_length = max(max_length, current_length)

    return max_length


if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("abcdef", 6),
        ("abba", 2),
    ]

    for text, expected in test_cases:
        result = lengthOfLongestSubstring(text)
        print(f"Input: {text!r}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Passed: {result == expected}\n")