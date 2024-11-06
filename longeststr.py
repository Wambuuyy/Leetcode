def lengthOfLongestSubstring(s: str) -> int:
    """We gonna use the sliding window
    first create a set that we gonna use to store the unique string
     have two iterator one goes first the otherone follows..
      if the character accessed by the first iterator is in the subset...
      remove the character at the left iterator 
      replace the chr at the right iterator to the setand move the iterator forward...
      this loops to the end of the string
      update max length by right - left + 1"""
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length