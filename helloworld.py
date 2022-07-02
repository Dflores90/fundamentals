# 1. TASK: print "Hello World"
print( "Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
name2 = "Daniel"
print( "Hello", name2 )	# with a comma
print( "Hello "+ name2 )	# with a +
# 3. print "Hello 42!" with the number in a variable
name ="42"
name2 = "70"
print( "Hello", name2 )	# with a comma
print("Hello " + name2 )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
fave_food3 = "ramen"
fave_food4 = "dumplings"
print( "I love to eat {} and {}.".format(fave_food3, fave_food4)) # with .format()
print(f"I love to eat {fave_food3} and {fave_food4}.") # with an f string


