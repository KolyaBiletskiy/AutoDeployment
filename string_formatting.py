


user_input = input("Enter your name:")

# 1 , py2
message = "Hello %s" % user_input

# 2, py3
message = f"Hello {user_input}"

# 3 , py3
message = "Hello {}".format(user_input)

print(message)


