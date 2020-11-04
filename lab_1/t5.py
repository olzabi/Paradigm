import datetime

print("\ntask5, v1")


chosen_seconds = int(input("Amount of seconds you choose here: "))
my_time = (datetime.timedelta(seconds=chosen_seconds))

print("The next string shows converted time. \nChosen seconds: {0}. \nConverted in time is: {1}"
      .format(chosen_seconds, my_time))
