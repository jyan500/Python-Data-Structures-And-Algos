"""
https://leetcode.com/problems/insert-delete-getrandom-o1/
https://www.youtube.com/watch?v=j4KwhBziOpg&ab_channel=NeetCode
Insert Delete Get Random, all in O(1) Time

Concept:
1) In order to have `getRandom` be O(1) time, we need to pick a random index, which requires us to keep a list
2) To have O(1) inserts and removes, we need a dictionary
3) The issue now is making sure the indices are always updated, especially after we remove an element
    -to keep this process O(1) we need to:
        - find the index of the value we want to remove from the dict
        - take the last element of the list, and then replace the value
        of the index we want to remove with the last element
        - update the index of the last element of the list within our dict
        - delete the last index of the list
        - delete the item from the dict

Example:

If we added list = [1, 2, 3], dict = {1: 0, 2: 1, 3: 2}

1) If want to delete 2...

the index of 2 is 1

2) we then replace the value of 2 with 3

[1, 3, 3]

3) Update the index within the dict

dict = {1: 0, 2: 1, 3: 1}

4) Delete the last element of the list

[1, 3]

5) Delete the value from the dict

dict = {1: 0, 3: 1}

Now the next time we add an element, it'll get added to the end of the list
correctly with the proper index

Add 4

dict = {1: 0, 3: 1, 4: 2}

list = [1, 3, 4]
"""
class RandomizedSet:

    def __init__(self):
        self.s = dict()
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.s:
            self.list.append(val)
            index = len(self.list) - 1
            self.s[val] = index
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.s:
            index = self.s[val]
            self.list[index] = self.list[-1]
            self.s[self.list[-1]] = index
            self.list.pop(-1)
            del self.s[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        import random
        return self.list[random.randint(0, len(self.list)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()