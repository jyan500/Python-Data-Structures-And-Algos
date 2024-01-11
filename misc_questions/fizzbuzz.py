def fizzbuzz(number: int) -> str:
	"""
	Prompt:
	1) If the number contains the digit "5" or is a multiple of "5", print the string "foo"
	2) If the number contains the digit "7" or is a multiple of "7", print the string "bar"
	3) If the number doesn't meet either condition, print "baz"
	
	A lesson in if/else operators 
	--------------------------------------------------------------------------------
	The key to fizzbuzz logic is that there are certain cases which will meet both
	conditions 1) and 2) 

	A common mistake is doing
	if ( condition 1 )
		do A
	if ( condition 2 )
		do B
	else:
		do C

	Thinking that if condition 1 and 2 are met, then 1 and 2 will be run and that's it

	However this is incorrect. Say if we ran fizzbuzz(5), we would actually get

	"foobaz"

	Why is that?
	
	Because if/else statements always act in pairs

	When looking at the condition above, we see that 5 meets condition 1), so we
	add "foo"

	We then look at condition 2, this condition is not met because 7 does not exist in 5,
	nor is 5 divisible by 7

	Therefore, because this if statement failed, we automatically jump to it's paired else statement.

	Which would then add "baz"
	
	--------------------------------------------------------------------------------
	How do we prevent this from happening?
	
	***
	we need a separate condition that checks where both condition 1 and condition 2 are met, and we need to make use 
	of the ELSE IF statement (elif in python) 
	***	

	if (condition 1 AND condition 2):
		do A 
		do B
	elif (condition 1)
		do A
	elif (condition 2)
		do B
	else:
		do C

	By doing this, we will make sure that in the case that both conditions 1 and 2 are met, 
	we do A and do B only ONCE. The elif statements only run if the paired if condition above
	was NOT met.

	fizzbuzz(35) meets both conditions 1) and conditions 2)

	we add foo and add bar

	But the elif statements do not run

	fizzbuzz(5) does not meet condition 1 AND conditions 2, but it does meet condition 1) only

	so we only add foo

	fizzbuzz(7) does not meet condition 1 AND condition 2, nor does it meet condition 1), but it 
	meets condition 2)

	so we only add bar
	
	finally,
	fizzbuzz(11) does not meet condition 1 AND condition 2, it does not meet condition 1, and does not meet condition 2)
	therefore, we now the run the paired else statement since the final ELIF statement was not met
	
	adds baz
	"""
	res = []
	digits = set(str(number))
	if ("5" in digits or number % 5 == 0) and ("7" in digits or number % 7 == 0):
		res.append("foobar")
	elif "5" in digits or number % 5 == 0:
		res.append("foo")
	elif "7" in digits or number % 7 == 0:
		res.append("bar")
	else:
		res.append("baz")	
	return "".join(res)

if __name__ == "__main__":
	assert fizzbuzz(5) == "foo"
	assert fizzbuzz(10) == "foo"
	assert fizzbuzz(14) == "bar"
	assert fizzbuzz(35) == "foobar"
	assert fizzbuzz(56) == "foobar"
	assert fizzbuzz(57) == "foobar"
	assert fizzbuzz(67) == "bar"
	assert fizzbuzz(11) == "baz"
