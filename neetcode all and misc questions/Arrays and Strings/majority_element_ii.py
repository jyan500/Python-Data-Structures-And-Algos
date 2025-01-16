class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        O(N) Time O(N) Space with counter,
        just pick the elements that have a frequency > N//3 

        The O(1) Space solution involves an algorithm called
        Boyer-Moore Voting Algorithm. It doesn't seem like something
        that would be asked in an interview but the code for that is here:

        https://youtu.be/Eua-UrQ_ANo
        """
        c = Counter(nums)
        factor = len(nums)//3
        return [key for key in c if c[key] > factor]
