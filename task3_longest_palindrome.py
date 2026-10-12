
def longestPalindrome(s: str) -> str:
    """
    Return the longest palindromic substring.
    """
    if not s:
        return ""

    start = 0
    max_length = 1

    def expand_around_center(left: int, right: int):
        nonlocal start, max_length

        # Expand while the characters match.
        while (
            left >= 0
            and right < len(s)
            and s[left] == s[right]
        ):
            current_length = right - left + 1

            if current_length > max_length:
                start = left
                max_length = current_length

            left -= 1
            right += 1

    for i in range(len(s)):
        # Odd-length palindrome, e.g. "racecar".
        expand_around_center(i, i)

        # Even-length palindrome, e.g. "abba".
        expand_around_center(i, i + 1)

    return s[start:start + max_length]


if __name__ == "__main__":
    test_cases = [
        ("babad", ["bab", "aba"]),
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("", [""]),
        ("racecar", ["racecar"]),
        ("abba", ["abba"]),
        ("abcdef", ["a", "b", "c", "d", "e", "f"]),
    ]

    for text, expected_options in test_cases:
        result = longestPalindrome(text)
        passed = result in expected_options

        print(f"Input: {text!r}")
        print(f"Output: {result!r}")
        print(f"Passed: {passed}\n")