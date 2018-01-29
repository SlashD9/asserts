x = 2 # Change x to 1, to pass the assert test. 
y = 1 # Change y to 2, to pass the assert test.

# Here we assert that x is less than y followed by a comma and then a 
# message that will print if the test fails.

# We also use the "{0}".format(x) function to replace the variable with the 
# assigned value.
assert(x < y), "{0} should be less than {1}".format(x, y)
