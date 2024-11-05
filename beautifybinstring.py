def minchanges(s: str) -> int:
    """A beautiful string lookes like 00110011 or 110011001100
    substrings have to be even ... this case we take substrings of 2 
    """

    changes = 0
    # Traverse in pairs
    for i in range(0, len(s), 2):
        # Check each pair
        if s[i] != s[i + 1]:
            # Increment changes if the two characters are different
            changes += 1
    return changes