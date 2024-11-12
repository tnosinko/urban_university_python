immutable_var = 123, "Phyton"
print (immutable_var)
#immutable_var[0] = "Something" (так как нет функции tuple к которой обращается
# кортеж или то что immutable_var[0] обращение к индексу 0, которого нет в списке ранее)

mutable_list = (["бантик", "салфетка", "ручка","жевачка"])
print(mutable_list [1])
mutable_list [1]= ("персик")
print(mutable_list)