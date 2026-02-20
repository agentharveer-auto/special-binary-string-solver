from collections import Counter
import math

def special_binary_string(s):
    """
    Calculates the number of special permutations of a string.
    A special permutation is one where no two adjacent characters are the same.

    Args:
        s: The input string.

    Returns:
        The number of special permutations.
    """

    counts = Counter(s)
    n = len(s)
    memo = {}

    def solve(remaining_counts, prev_char):
        """
        Recursive helper function to calculate the number of permutations.

        Args:
            remaining_counts: A Counter object representing the remaining character counts.
            prev_char: The previous character in the permutation.

        Returns:
            The number of permutations for the remaining characters.
        """

        # Convert Counter to tuple for memoization key
        counts_tuple = tuple(sorted(remaining_counts.items()))
        key = (counts_tuple, prev_char)

        if key in memo:
            return memo[key]

        if sum(remaining_counts.values()) == 0:
            return 1

        total_permutations = 0
        for char, count in remaining_counts.items():
            if char != prev_char and count > 0:
                new_counts = remaining_counts.copy()
                new_counts[char] -= 1
                if new_counts[char] == 0:
                    del new_counts[char]
                total_permutations += solve(new_counts, char)

        memo[key] = total_permutations
        return total_permutations

    return solve(counts, '')


# Unit Tests (from QA Engineer - slightly modified)
import unittest

class TestSpecialBinaryString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(special_binary_string(""), 1)

    def test_single_character(self):
        self.assertEqual(special_binary_string("a"), 1)

    def test_two_different_characters(self):
        self.assertEqual(special_binary_string("ab"), 2)

    def test_two_same_characters(self):
        self.assertEqual(special_binary_string("aa"), 0)

    def test_example_1(self):
        self.assertEqual(special_binary_string("abc"), 6)

    def test_example_2(self):
        self.assertEqual(special_binary_string("aba"), 2)

    def test_example_3(self):
        self.assertEqual(special_binary_string("aabb"), 2)

    def test_longer_string(self):
        self.assertEqual(special_binary_string("aab"), 2)

if __name__ == '__main__':
    unittest.main()