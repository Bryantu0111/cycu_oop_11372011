#第一種方法
def print_right(s):
    print(" "*(40-len(s))+s)

print_right("Monty")
print_right("Python's")
print_right("Flying Circus")


#第二種方法
str1 = "Monty"
str2 = "Python's"
str3 = "Flying Circus"

message1 = ' ' * (40-len(str1)) + str1
message2 = ' ' * (40-len(str2)) + str2
message3 = ' ' * (40-len(str3)) + str3

print(message1)
print(message2)
print(message3)