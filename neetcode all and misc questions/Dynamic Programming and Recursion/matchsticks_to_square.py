class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        Note: revisited on 2/6/2025 with the same solution as below
        
        https://www.youtube.com/watch?v=hUe0cUKV-YY&ab_channel=NeetCode
        https://leetcode.com/problems/matchsticks-to-square/submissions/ 

        1) in order for sticks to form a square, each side
        must be the same length
        2) need to use up all sticks in such a way where we have
        four configurations that add up to the same number essentially
        
        therefore, we can figure out the side length that each number needs to be
        by adding all the numbers together and dividing by 4
    
        Then, we can use backtracking and figure out the configuration of where each matchstick needs to go
        
        1 1 2 2 2 
        
        side length must be = (1 + 1 + 2 + 2 + 2)/4=2
        
        *   *
        
        *   *
        
        we can try placing 1 in 4 different spots, the top, left, bottom or right sides
          1
        *-- *
        
        *   *
        
        If we place 1 on top, we then go onto the recursive call, where figure out where to place 
        the following 1
        
        if we try placing 1 at any point that's not the top, we can see that we'll then go onto
        place 2 somewhere, and then realize that one side will end up being length 3 (1 + 2),
        which is greater than the limit of 2 that we already calculated
        
        the only configuration that works is placing 1 at the top next to the 1 that we already placed
        
        *-- --*
        
        
        *     *
        
        the 2's can then go into the other remaining spots
        
        Approach:
        
        One minor optimization to make is to sort the matchsticks in reverse order first,
        that way we use up the "biggest" matchsticks first to hopefully cut down on the amount of time
        needed to find a configuration. This also happens to prevent TLE on leetcode.
        
        1) In our recursive function, we pass in the index i to keep track of which matchstick we're on
        within our matchsticks list parameter
        2) We then use a for loop which loops through our self.sides array below, and checks whether
        a given side (i.e sides[j]) has reached the side length, if not then we can add
        the matchstick to that side. 
            -Note that within this for loop, if our recursive call results
        in "True", we can just return True since we only care if one of the configurations results in True
            - if our last decision didn't result in a valid configuration, we need to 
            "reverse" our last decision by removing the matchstick (sides[j] - matchsticks[i])
        3) As our base case, if we don't have any more matchsticks (i == len(matchsticks)), we return True,
        since that means we were able to use all matchsticks on each side with proper side length.
    	
    	Time Complexity: O(4^N), since our decision tree is height of N, which is the amount of matchsticks,
    	and then at each level of our decision tree, there's 4 decisions to be made,
    	so 4 * 4 * 4 ... N times

    	Example 1:
    	matchsticks = 
    	1 3 3 2 2 1 1 3

    	This could potentially form a square, since all the sides add up 16,
    	so each side length could be 4 

    	self.sides = [0, 0, 0, 0]	

    	Reverse sort the matchsticks
    	3 3 3 2 2 1 1 1 

    	First Call:
    	search(0)
		in our loop,
    	we can add 3 to self.sides[0],
    	now we search(1)
    	self.sides = [3, 0, 0, 0]

    	Second Call:
    	search(1)
    	in our loop,
    	we can't add 3 to self.sides[0], but we can add
    	it to self.sides[1],
    	so [3, 3, 0, 0]

    	Third Call:
    	search(2)
    	in our loop,
    	we can't add 3 to self.sides[0] and self.sides[1], but
    	we can add 3 to self.sides[2]

    	so [3, 3, 3, 0]

    	Fourth Call:
    	search(3)
    	in our loop,
    	we can add 2 to self.sides[3],

    	so [3, 3, 3, 2]

    	Fifth Call:
    	search(4)
    	we can only add 2 to self.sides[3] again,

    	so [3, 3, 3, 4]

    	Sixth Call:
    	search(5)
    	we can add 1 to self.sides[0]
    	so [4, 3, 3, 4]

    	Seventh Call:
    	search(6)
    	we can add 1 to self.sides[1]
    	so [4, 4, 3, 4]

    	Eighth Call:
    	search(7)
    	we can add 1 to self.sides[2]
    	so [4, 4, 4, 4]

    	Ninth Call:
    	i is now equal to the length of matchsticks, so we return True here

	    ----------------------------------------------------------------------	
		Example 2:
		[5,5,5,5,4,4,4,4,3,3,3,3]

		Here, the matchsticks add up to 48, so each side length needs to be 12

		This example demonstrates why it's important we're able to backtrack 
		by subtracting from self.sides

		Doing normal execution,
		we'll get something like this, where both 5's add into sides[0] and sides[1],
		and then 4 adds into sides[2]
		self.sides = [10, 10, 8, 0]
		
		the remaining two 4's will go into sides[2] and sides[3] 
		self.sides = [10, 10, 12, 4]

		however, only two 3's can fit into sides[3]
		3 + 3 + 4 = 10
		self.sides = [10, 10, 12, 10]

		**** 
		Therefore at this point, we would return False since there's two threes left that we 
		cannot use 
		*****

		we would then need to backtrack to 
		self.sides = [10, 10, 12, 7],

		by subtracting one 3 from self.sides[3] so we can reuse it
		self.sides = [10, 10, 12, 4]

		subtracting another 4 from self.sides[3]
		self.sides = [10, 10, 12, 4]

		all the way until we get to 
		self.sides = [5, 0, 0, 0], 
		where we're back to being on matchstick i = 1, so we 
		are figuring out where to add our 5

		at this point, instead of adding another 5 to self.sides[0] which is 
		what we did originally, going back to this recursive call, our loop variable j would dictate that we try
		it at self.sides[1] instead

		self.sides = [5, 5, 0, 0]

		And the process would repeat itself, where it tries to stack itself onto self.sides[1]
		again and realizes it won't work, then does

		self.sides = [5, 5, 5, 0],

		at the end,
		
		each side will have 5 + 4 + 3 = 12, when done properly

		self.sides = [12, 12, 12, 12], and returns True

        """
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        self.sideLength = total/4
        self.sides = [0, 0, 0, 0]
        matchsticks.sort(reverse=True)
        # we pass in i to point to where the matchstick should be 
        def search(i):
            if i == len(matchsticks):
                return True
            for j in range(len(self.sides)):
                if matchsticks[i] + self.sides[j] <= self.sideLength:
                    self.sides[j] += matchsticks[i]
                    if search(i+1):
                        return True
                    # if our last decision didn't result in a valid configuration, we need to 
                    # "reverse" our last decision by removing the matchstick
                    self.sides[j] -= matchsticks[i]
            # if our match stick did not fit into any sides, that means
            # we made a wrong decision somewhere, so we'd return False out of this call
            return False
        return search(0)
       
                
            
            
        