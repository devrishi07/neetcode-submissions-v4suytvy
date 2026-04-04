from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        need = Counter(t)
        window = defaultdict(int)

        required = len(need)   # number of unique chars in t
        formed = 0             # how many chars currently satisfied

        left = 0
        best_len = float("inf")
        best_window = (0, 0)

        # Expand the window
        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            # Check if this character just satisfied a requirement
            if char in need and window[char] == need[char]:
                formed += 1

            # Shrink while window is valid
            while formed == required:
                # Update best answer
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_window = (left, right)

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                # Check if window just became invalid
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        l, r = best_window
        return s[l:r+1]
