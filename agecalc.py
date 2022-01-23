age = int(input('How old are you?\n'))
# The answer to input is a string so you must convert it to a number datatype by wrapping it in the int()
decades = age // 10
years = age % 10
print("You are " + str(decades) + " decades and " + str(years) + " years old!")
# decades is a float and could not be concatenated. It needs to be converted to a string.