# function to check if two strings are
# anagram or not
def check(s1, s2):
	
	# the sorted strings are checked
	if(sorted(s1)== sorted(s2)):
		print("The strings are anagrams.")
	else:
		print("The strings aren't anagrams.")		
		
# driver code
s1 ="listen"
s2 = s1[::-1]
check(s1, s2)
