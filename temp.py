"""This file is just to test out the random stuff"""

# a = "Bodaciou"
# print(a[::-2])

# mylist = [10, 20]
# s1 = frozenset(mylist )
# print(s1)
# print(type(s1))
import itertools

print(9 ^ 6)

l1 = [1, 2, 7, 4, "5"]
# l1.sort()
# l1.reverse()
# l1.update([1,7,7, "one",3])
print(l1)

# t1 = (1, 2, 3)
# t2 = (1, 2, 3, 1)
# print(t2.index(1))
# d1 = {
#     "one": 1
# }
# print(d1.keys())
#
# "one".replace()
# name = "Raj"
# age = 20
# percentage = 91.24
#
# print("Hello, My name is  %s. My age is %d and my score is %.3f"%(name, age, percentage))
#
# s1 = "php java sql java"
# print(s1.count("java", 0,8))
#
# print(s1.split(" ", 10))

# print({1,2,3}.intersection([1,2]))
#
# for combo in itertools.combinations(range(10), 3):
#     print(combo)

# a = [('CASE_DAYS_PASSED_GROUPS', 0.6041738160544823, 0.6409716472043235), ('TOTAL_DAYS_PASSED_GROUPS', 0.5983560476368939, 0.6413184692939964), ('MSRP_AMOUNT_GROUPS', 0.6142845374495502, 0.6114096718786014), ('total_part_expense_GROUPS', 0.5767056394650761, 0.6290922342196714), ('VEH_DAYS_DOWN_GROUPS', 0.5837602426500181, 0.6292767828142631), ('C109', 0.5833655584060602, 0.6319496018961823), ('C86', 0.5842907586117951, 0.6290572186835401), ('C35', 0.5865741848316114, 0.632148033314851), ('C217', 0.5840579011008393, 0.632148033314851), ('Issue: Fraud', 0.585333718327503, 0.629059837512975), ('Issue: TIPM', 0.5857904869011087, 0.6325923624227288)]
# param = [x[0] for x in a]
l1 = [(x/1000) for x in range(1, 11)]
a = 0
for x in itertools.product(l1, repeat=2):
    print(x)
    a += 1
print(a)


# sum()