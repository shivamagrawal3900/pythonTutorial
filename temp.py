"""This file is just to test out the random stuff"""


# a = "Bodaciou"
# print(a[::-2])

# mylist = [10, 20]
# s1 = frozenset(mylist )
# print(s1)
# print(type(s1))

# print(9 ^ 6)

# l1 = [1, 2, 7, 4, "5"]
# l1.sort()
# l1.reverse()
# l1.update([1,7,7, "one",3])
# print(l1)

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


# l1 = [(x/1000) for x in range(1, 11)]
# a = 0
# for x in itertools.product(l1, repeat=2):
#     print(x)
#     a += 1
# print(a)

# l1 = [1,2,3,4,5]
# del l1[1::-1]
# print(l1)


# d1 = {
#     "one": 1,
#     "two": 2
# }
# print(d1.popitem())
# print(d1.popitem())
# print(d1.popitem())
# d1.update({'three': 3})
# l1 = {1, 2, 3, 4}
# l1.discard(9)
# x = [a for a in l1]
# print(type(x))

# def var_arg(*args):
#     print(type(args))
# var_arg(1,2,3)

# squares = list(x * y for x in [2, 3, 5, 6] for y in [1, 2, 3, 4] if x != y)
# squares = list(map(lambda x, y: x * y, [2, 3, 5, 6], [1, 2, 3, 4]))
# print(squares)


# def abc(one,two):
#     print(one, two)
#
# xyz = abc
# xyz(10, 10)

# class A:
#
#     def __init__(self) -> None:
#         self.a = 11
#
#     def __init__(self, c) -> None:
#         self.a = c
#
#     def one(self):
#         print("A")
#
#     def one(self, o):
#         print("B")
#
#
# class C:
#     def __init__(self) -> None:
#         self.c = 12
#
#     def one(self):
#         print("C")
#
#
#
# class B(A):
#     def __init__(self):
#         super().__init__(111)
#         self.b = 13
#
#     def one(self):
#         print(type(super(B, self).one()), type(super().one()))
#         print(self.b, self.a)
#
# class D:
#     def __init__(self, b):
#         self.a = 10
#         self.b = b
#
#     def __init__(self):
#         self.a = 10
#
#     def one(self):
#         print(self.b)
#
# # a = B()
# # print(a.a, a.b)
# # a.one()
#
# a = A()
# a.one()

class OpOverload:
    one = 1

    def __idiv__(self, other):
        print("idiv")
        return 100

    def __itruediv__(self, other):
        print("itruediv")
        self.this_is_method()
        return 1000

    @staticmethod
    def this_is_method():
        OpOverload.one += 1
o1 = OpOverload()
o2 = OpOverload()
# o1 /= o2

print(o1.one)
o1.this_is_method()
OpOverload.this_is_method()
print(OpOverload.one)