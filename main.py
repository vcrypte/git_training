print("Hello world!")

import copy
original = [[1, 2], [3, 4]]
shallow = original.copy()     # поверхностная копия — вложенные списки всё ещё общие
deep = copy.deepcopy(original) # глубокая копия — полностью независима

shallow[0].append(99)
print(original[0])  # [1, 2, 99]  <- shallow-копия не защитила вложенный список
deep.append(99)
print(deep[0])      # [1, 2]      <- deep-копия независима

x = 42
name = "Alice"
print(f"{x=}, {name=}")  # x=42, name='Alice'

path = rf"C:\Users\Name\Documents\file.txt"
print(path)  # C:\Users\Name\Documents\file.txt

hello world

path = rf"C:\Users\Name\Documents\file.txt"
print(path)  # C:\Users\Name\Documents\file.txt