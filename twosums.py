""" I have two metods the brute force that checks through the 
        list twice one iterator starts from the front the other from the second checks if there are any pairs 
    The second method is one where iterated numbers are hashed in a dict a complement is found by subtracting
        the number from target if its in the hasheddict you display output if not the number is hashed
"""

def twosums(nums: list[int], target: int) -> list:
    """return the indices of the two numbers that add up to the target.
    """
    hash_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_dict:
            return [hash_dict[complement], i]
        hash_dict[num] = i
    return[]

