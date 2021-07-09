'''
Clement's Google Mock Interview Question First Question
https://www.youtube.com/watch?v=rw4s4M3hFfs&ab_channel=Cl%C3%A9mentMihailescu

Given a two parameters, the first is a list representing a neighborhood, each item in the list is a dictionary representing an apartment block.
Within this dictionary, our keys are buildings in the neighborhood and the values are booleans on whether that building 
is in the neighborhood. The second param is a list of these buildings that we would want in our neighborhood

Find out which apartment building would minimize the furthest distance to each of these buildings that we would want to visit.

Some constraints:
The blocks list can include extra keys in the dictionary that are not in the buildings list
however, if building exists in the building list, then each of the dictionaries within the blocks list must have that building
as a key

Within each dictionary in the blocks list, at least one of the buildings will be set to true (so there's no case the buildings aren't in any of the apartment blocks)

For example in the following blocks list:

blocks = [
	{
		gym : false,
		school : true,	
		store : false,
	},
	{
		gym: true,
		school : false,	
		store : false,
	},
	{
		gym: true,
		school: true,
		store: false,	
	},
	{
		gym : false,
		school : true,
		store : false,	
	},
	{
		gym: false,
		school: true,
		store: true	
	}
]

and the following list of buildings we want:

buildings = [gym, school, store]

The apartment which minimizes the furthest distance to each of the buildings is i = 3, because 
the distance to reach a gym is 1, distance to reach a school is 0 (since school = true) and distance to reach store is 1
so max total is 1


Approach:

for each apartment block
figure out the distance to each of the desired buildings
	-to figure this out, within the list, we'd need to iterate forwards until i = len(blocks) - 1 and backwards until i = 0
	in the case that we find a distance to the building in one direction, we stop the loop and then iterate the the other direction
	to see if there is a shorter distance and pick the minimum between these two

out all of the distances we've found, figure out which one of these distances is the max for this apartment block i 

at the end, we pick the lowest value

'''

def findMinDistance(blocks : [dict()], buildings: []) -> int:
	min_distance = float('inf')
	res = -1
	for i in range(len(blocks)):
		apartment_block = blocks[i]
		apt_block_max_distance = 0 
		for j in range(len(buildings)):
			building = buildings[j]
			## if our current building is not at the current apartment block
			if (not apartment_block[building]):
				## starting from the current apartment, use two pointers to iterate outwards
				## in order to find when we've found the building that we want
				left = i
				right = i
				distance_to_building = 0
				has_apt_building_left = blocks[left][building]
				has_apt_building_right = blocks[right][building]
				## we can use this as a condition due to the constraint that we'll eventually find a building in our list that
				## has the value set to "true" 
				while (not has_apt_building_left and not has_apt_building_right):
					if (left >= 0):
						has_apt_building_left = blocks[left][building]
						left -= 1	
					if (right < len(blocks)):
						has_apt_building_right = blocks[right][building]
						right += 1
					distance_to_building += 1
				apt_block_max_distance = max(apt_block_max_distance, distance_to_building)
		## within each apartment block, if the max distance it takes to any of the buildings is less than our 
		## current min distance, set the min distance
		if (apt_block_max_distance < min_distance):
			min_distance = apt_block_max_distance
			res = i
	return res

'''
Time: O(N^3), at the top level we iterate through N apartment blocks O(N), 
for each building B, we iterate through each building O(N), and within the second inner loop, perform the while loop operation O(N)

Space: excluding the parameters is O(1) since we're only using two constant variables
'''
blocks1 = [
	{
		'gym' : False,
		'school' : True,	
		'store' : False,
		'office' : False,
	},
	{
		'gym': True,
		'school' : False,	
		'store' : False,
		'office' : True,
	},
	{
		'gym': True,
		'school': True,
		'store': False,	
		'office' : False,
	},
	{
		'gym' : False,
		'school' : True,
		'store' : False,	
		'office' : False,
	},
	{
		'gym': False,
		'school': True,
		'store': True,
		'office' : True,
	}
]
buildings1 = ['gym', 'school', 'store']

blocks2 = [
	{
		'gym' : False,
		'school' : True,	
		'store' : False,
		'office' : True,
	},
	{
		'gym': True,
		'school' : False,	
		'store' : False,
		'office' : False,
	},
	{
		'gym': True,
		'school': True,
		'store': False,	
		'office' : False,
	},
	{
		'gym' : False,
		'school' : True,
		'store' : False,	
		'office' : False,
	},
	{
		'gym': False,
		'school': True,
		'store': True,
		'office' : False,
	}
]

buildings2 = ['gym', 'office']

blocks3 = [
	{
		'gym' : True,
		'store' : True,
		'school' : False,
		'office' : False,
	}
]

buildings3 = ['gym', 'store']
assert findMinDistance(blocks1, buildings1) == 3
assert findMinDistance(blocks2, buildings2) == 0
assert findMinDistance(blocks3, buildings3) == 0
