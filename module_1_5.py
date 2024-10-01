immutable_var = [3,4, '1s']
print("Дан список:", immutable_var)
immutable_var.append('Modified')
immutable_var=tuple([3,4,'1s'])
#Теперь не возможно изменить список immutable_var, командой "immutable_var.append('Modified')", так как список зафиксирован функцией tuple
print('Immutable tuple:', immutable_var)
mutable_list=[3,4, '1s']
mutable_list.append('Modified')
print("Mutable list:", mutable_list)
print("Вызванный второй элемент из списка Immutable var", immutable_var[1])
print("Вызванный третий элемент из списка  Mutable list", mutable_list[2])