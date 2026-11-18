import math

class Solution:
    def countPrimes(self, n: int) -> int:
        """
        11/18/2026
        Reverse thinking
        Rather than going from i ... n - 1 and determining whether each 
        number in that range is prime, 
        you can assume every number starting from 2 (because 0 and 1 are not prime by default)
        by creating a boolean array
        then mark the multiples of that number to be false
        i.e n = 10
          0      1       2            9
        [False, False, True, ....., True]
        So starting from 2, we would mark 4, 6, 8 as False, since automatically
        know these are not primes
        at 3, we would identify 6 and 9 as False
        at 4, we already know this isn't prime since we marked it false previously, so we skip
        at 5, we would mark 10, but this is outside our range
        6, is already false
        7  (would mark 14 but its outside the range)
        8 already false
        9 already false

        Note that with a few optimizations, you can shrink this so that you decrease the bound
        of the outer loop to just the floor(sqrt(n)), since the inner loop optimization with
        finding the first possible multiple that hasn't been covered already would no longer apply
        once i * i > n

        Also this process is well known in mathematics, called the sieve of eratosthenes.

        The time complexity is O(Nlog(logN)), the log(logN) is essentially measuring the growth
        of the amount of overall inner while loop operations, for example at the prim enumber 2, you would have the most
        writes since you're crossing off 4,6,8, etc, and then each prime after would have less writes 
        since the number is bigger. The gist of it is that log(logN) grows very slowly, so this is still an efficient algorithm.
        """
        if n == 0 or n == 1:
            return 0
        primes = [True] * n 
        primes[0] = False
        primes[1] = False
        # note that you don't need to iterate all the way up to n,
        # because you can do the floor(sqrt(n)), there's no point in going any further
        # because that would mean that in the inner while loop, i * i would always exceed n
        for i in range(2, math.floor(math.sqrt(n))+1):
            if primes[i]:
                # automatically mark all the multiples of the given prime
                # as "False" up to n.
                # note that because previous prime number multiples could've overlapped and marked
                # some of these multiples as False, already we can just start at k = i instead of k = 2,
                # for example, at i = 2, if we started k = 2, we mark 4, 6 and 8 as FAlse
                # now if we were at i = 3 and started k = 2 again, if we did 3 * 2, we would hit 6 again,
                # so instead, we just start at k = 3, which is just the value of i itself.
                k = i
                while (i * k < n): 
                    primes[i*k] = False
                    k += 1
        count = 0
        for i in range(len(primes)):
            if primes[i]:
                count += 1
        return count
            