class Solution:
    def knightDialer(self, n: int) -> int:
        """
        1/18/2024
        https://leetcode.com/problems/knight-dialer/
        https://www.youtube.com/watch?v=vlsUUm_qqsY&ab_channel=NeetCodeIO

        Bottom Up Dynamic Programming
        
        O(N) solution
        O(1) space
        
        1) Define a "jumps" 2-D array where from each number 0 to 9,
        we show which numbers we can jump to as defined by how the knight in chess moves
        2) The key concept utilizing DP here is that we only need to know 
        how many times we can reach a particular digit from any other digit. So we can build up the DP array, knowing that from a given digit, we use that digit as an index into our "jumps" array,
        and see what other numbers we can jump to. Then we would aggregate those results together.
        
        An Example Run Through:
        jumps = [
            # at number 0, we can jump to 4 or 6 
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            # because we can't jump to # or *, at 5, there's no possible jumps
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [4, 2]
        ]
        dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        n = 2
        
        for _ in range(2-1):
            nextDp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for k in range(10):
                ...
                
                
                1st iteration of the loop k = 0
                for j in jumps[k]:
                    ...
                    jumps[k] is jumps[0], which is [4, 6], 
                    # what this means is that
                    # IF we are able to jump to 0, we are ALSO able to jump to 4, so we should
                    # "sum" together their amounts
                    nextDp[4] = nextDp[4] + dp[0] = 1
                    ... 
                    nextDp[6] = nextDp[6] + dp[0] = 1
                
                at this point, nextdp = [0,0,0,0,1,0,1,0,0,0]
                ---------------------------------------------
                2nd iteration of the loop, k = 1
                for j in jumps[k]:
                    ...
                    jumps[k] is jumps[1], which is [6, 8]
                    nextDp[6] = nextDp[6] + dp[1] = 2
                    ...
                    nextDp[8] = nextDp[8] + dp[1] = 1
                
                at this point, nextDp = [0,0,0,0,1,0,2,0,1,0]
                 ---------------------------------------------
                3rd iteration of the loop, k = 2
                for j in jumps[k]:
                    ...
                    jumps[k] is jumps[2], which is [7, 9]
                    nextDp[7] = nextDp[7] + dp[1] = 1
                    ...
                    nextDp[9] = nextDp[9] + dp[1] = 1
                
                at this point, nextDp = [0,0,0,0,1,0,2,1,1,1]
                 ---------------------------------------------
                4th iteration of the loop, k = 3
                for j in jumps[k]:
                    ...
                    jumps[k] is jumps[3], which is [4,8]
                    nextDp[4] = nextDp[4] + dp[1] = 2
                    ...
                    nextDp[8] = nextDp[8] + dp[1] = 2
                
                at this point, nextDp = [0,0,0,0,2,0,2,1,2,1]
                 ---------------------------------------------
                5th iteration of the loop, k = 4
                for j in jumps[k]
                    ...
                    jumps[k] is jumps[4], which is [3, 9, 0]
                    nextDp[3] = nextDp[3] + dp[1] = 1
                    ...
                    nextDp[9] = nextDp[9] + dp[1] = 2
                    ...
                    nextDp[0] = nextDp[0] + dp[1] = 1
                
                at this point, nextDp = [1,0,0,1,2,0,2,1,2,2]
                 ---------------------------------------------
                6th iteration of the loop, k = 5
                because there are no jumps available at jumps[k], we can skip this
                ----------------------------------------------
                7th iteration of the loop, k = 6
                for j in jumps[k]
                    ...
                    jumps[k] is jumps[6], which is [1, 7, 0]
                    nextDp[1] = nextDp[1] + dp[1] = 1
                    ...
                    nextDp[7] = nextDp[7] + dp[1] = 2
                    ...
                    nextDp[0] = nextDp[0] + dp[1] = 2
                
                at this point, nextDp = [2,1,0,1,2,0,2,1,2,2]
                ---------------------------------------------
                8th iteration of the loop, k = 7
                for j in jumps[k]
                    ...
                    jumps[k] is jumps[7], which is [2,6]
                    nextDp[2] = nextDp[2] + dp[1] = 1
                    ...
                    nextDp[6] = nextDp[6] + dp[1] = 3
                    
                at this point, nextDp = [2,1,1,1,2,0,3,2,2,2]
                ---------------------------------------------
                9th iteration of the loop, k = 8
                for j in jumps[k]
                    ...
                    jumps[k] is jumps[8], which is [1,3]
                    nextDp[1] = nextDp[1] + dp[1] = 2
                    ...
                    nextDp[3]= nextDp[3] + dp[1] = 2
                
                at this point, nextDp = [2,2,1,2,2,0,3,2,2,2]
                ---------------------------------------------
                10th iteration of the loop, k = 9
                for j in jumps[k]
                    ...
                    jumps[k] is jumps[9], which is [4,2]
                    nextDp[4] = nextDp[4] + dp[1] = 3
                    ...
                    nextDp[2] = nextDp[2] + dp[1] = 2
                
                at this point, nextDp = [2,2,2,2,3,0,3,2,2,2]
                
            
            we've now finished this loop (for k in range(10)),
            so now we set dp = nextDp
            
            dp = [2,2,2,2,3,0,3,2,2,2]
        
        
        We're also done with the outer most loop (for _ in range(n-1))
        
        sum(dp) = 2+2+2+2 = 8, 3 + 3 = 6, 2 + 2 +2 = 6, 8 + 6 + 6 = 20
        20 % (10**9 + 7) = 20
        
        Final answer is 20
        
        In other examples, normally we'd continue this process for another jump,
        and then re-use our newly populated dp array.
                        
        """
        # if n is 1, the knight doesn't jump, so this is essentially just placing the knight
        # in 10 different squares (not counting * and #)
        if n == 1:
            return 10
        jumps = [
            # at number 0, we can jump to 4 or 6 
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            # because we can't jump to # or *, at 5, there's no possible jumps
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [4, 2]
        ]
        # dp will track the number of ways to land on the ith digit
        dp = [1] * 10
        # we do n-1, since we know that at n = 1, it's only one possible way since
        # we're not actually jumping, just placing the knight at that spot
        for _ in range(n-1):
            nextDp = [0] * 10
            for k in range(10):
                for j in jumps[k]:
                    nextDp[j] = nextDp[j] + dp[k]
            dp = nextDp
        return sum(dp) % (10**9 + 7)
            