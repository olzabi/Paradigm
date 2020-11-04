print("task 1(1.1)")
#  % format
print("with percent:\n", "%4d" % int(input("percent format: ")))

# .format()
print("with .format:\n", "{0:4d}".format(
    int(input("choose number for .format(): "))
))


# f-string format
num = int(input("choose number:"))
print("with f-string:\n", f"{num:4d}")


# 1.2_1
chosen_float = float(input("choose float number:"))
print("{0:11f}".format(chosen_float))

# 1.2_2
float_num = float(input("float num:"))
print("{0:6.3f}".format(float_num))


# 1.3
chosen_str = str(input("pole to choose smth:"))
hidden_false = False if len(chosen_str) != 5 or chosen_str == "False" else True
print(hidden_false)
