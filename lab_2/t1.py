districts = [4312, 2733, 1400, 7705, 5361, 4072, 2941, 2259, 1157, 1588, 8246, 1992]  # 43 766
general_amount = 0

# (1к человек на км * км) - площадь района (?)
# район + район... = площадь области
dis_S = ((i / 1000 * 1000) for i in districts)

for i in dis_S:
    general_amount += i

print(general_amount)
