'''
A cafeteria table consists of a row of NN seats, numbered from 11 to NN from left to right. Social distancing guidelines require that every diner be seated such that KK seats to their left and KK seats to their right remain empty.
There are currently MM diners seated at the table, the iith of whom is in seat S_iS 
i
​
No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.
Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
'''
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here
	taken_spots = []
	for i in range(len(S)):
		r=calcRange(K, N, S[i])
		taken_spots.append(r)
	max_num_spots = 0
	for i in range(1, N+1):
		if (not isOverlapping(i, taken_spots)):
			r = calcRange(K,N,i)
			taken_spots.append(r)
			max_num_spots += 1
	return max_num_spots


def calcRange(K, N, num):
	left_side = num
	for j in range(K):
		if (left_side == 0):
			break
		left_side -= 1
	right_side = num
	for j in range(K):
		if (right_side == N):
			break
		right_side += 1
	return (left_side, right_side)

def isOverlapping(proposed_spot, taken_spots):
	for spot in taken_spots:
		taken_start,taken_end=spot
		if (taken_start <= proposed_spot <= taken_end):
			return True
	return False


if __name__ == '__main__':
	print(getMaxAdditionalDinersCount(10, 1, 2, [2,6])) # expected 3
	print(getMaxAdditionalDinersCount(15,2,3,[11,6,14])) # expected 1