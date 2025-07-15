class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 2)

    def update(self, index, delta):
        index += 1
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        # Sum from 0 to index
        index += 1
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        pos_in_nums2 = {val: i for i, val in enumerate(nums2)}
        mapped = [pos_in_nums2[val] for val in nums1]

        left_tree = FenwickTree(n)
        right_tree = FenwickTree(n)

        for val in mapped:
            right_tree.update(val, 1)  # initially all elements in right

        result = 0
        for val in mapped:
            right_tree.update(val, -1)  # move current to middle

            left_smaller = left_tree.query(val - 1)  # count of smaller before
            right_greater = right_tree.query(n - 1) - right_tree.query(val)  # count of greater after

            result += left_smaller * right_greater

            left_tree.update(val, 1)  # move current to left

        return result
