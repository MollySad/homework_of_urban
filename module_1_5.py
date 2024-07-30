immutable_var = 25, 'привет', 2.55, 789
# immutable_var[0] = 12
# кортеж не возможно изменить, поскольку это неизменяемый обьект
print(immutable_var)

mutable_list = [25, 'привет', 2.55, 789]
mutable_list[0] = mutable_list[3]
mutable_list.append('пока')
mutable_list.extend([12, 34])
mutable_list.remove(34)
print(mutable_list)
