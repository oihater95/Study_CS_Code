import copy

people = {1, 2, 3, 4}
s1 = people  # people과 같은 객체
s2 = people.copy()  # 다른 객체
s3 = set(people)  # 다른 객체
s1.remove(1)
s2.remove(3)
s3.remove(4)

print(people, s1, s2, s3)


obj = [1, 2, 3, 4]
l1 = obj  # 같은 객체
l2 = obj[:]  # 다른 객체
l3 = list(obj)  # 다른 객체
l4 = obj.copy()  # 다른 객체

print(id(obj), id(l1), id(l2), id(l3), id(l4))

obj2 = [1, 2, 3, [4, 5, 6]]
lst1 = obj2[:]  # shallow
lst2 = list(obj2)  # shallow
lst3 = obj2.copy()  # shallow
lst4 = copy.deepcopy(obj2)  # deep

lst1[3][0] = 0
lst2[3][1] = 0
lst3[3][2] = 0
lst4[3][0] = 1

print(obj2, lst1, lst2, lst3, lst4)