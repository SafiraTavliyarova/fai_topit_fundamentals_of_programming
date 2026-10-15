import copy

# original = [
#     ["Python", 5],
#     ["Algorithms", 4],
# ]

# alias = original
# shallow = original.copy()
# deep = copy.deepcopy(original)

# # === До изменений ===
# print('=== До изменений: ===')
# print('original:', original)
# print('alias:', alias)
# print('shallow:', shallow)
# print('deep:', deep)

# # id:
# # 1.
# print('\n id-ры внешних списков:')
# print('original:', id(original))
# print('alias:', id(alias)) 
# print('shallow:', id(shallow))
# print('deep:', id(deep))

# # 2.
# print('\n id-ры первого вложенного списка ([0]):')
# print('original:', id(original[0]))
# print('alias:', id(alias[0]))
# print('shallow:', id(shallow[0]))
# print('deep:', id(deep[0]))

# # 3.
# print('\n id-ры объекта, содержащего первую оценку ([0][1]):')
# print('original:', id(original[0][1]))
# print('alias:', id(alias[0][1]))
# print('shallow:', id(shallow[0][1]))
# print('deep:', id(deep[0][1]))



# # === Изменение 1. Append ===
# print('\n === Изменение 1. Append ===')
# original.append(["Databases", 5])


# print('original:', original)
# print('alias:', alias)
# print('shallow:', shallow)
# print('deep:', deep)

# # id:
# # 1.
# print('\n id-ры внешних списков:')
# print('original:', id(original))
# print('alias:', id(alias))
# print('shallow:', id(shallow))
# print('deep:', id(deep))

# # 2.
# print('\n id-ры первого вложенного списка ([0]):')
# print('original:', id(original[0]))
# print('alias:', id(alias[0]))
# print('shallow:', id(shallow[0]))
# print('deep:', id(deep[0]))

# # 3.
# print('\n id-ры объекта, содержащего первую оценку ([0][1]):')
# print('original:', id(original[0][1]))
# print('alias:', id(alias[0][1]))
# print('shallow:', id(shallow[0][1]))
# print('deep:', id(deep[0][1]))





# # === Изменение 2. original[0][1] = 3 ===
# print('\n === Изменение 2. original[0][1] = 3 ===')
# original[0][1] = 3


# print('original:', original)
# print('alias:', alias)
# print('shallow:', shallow)
# print('deep:', deep)

# # id:
# # 1.
# print('\n id-ры внешних списков:')
# print('original:', id(original))
# print('alias:', id(alias))
# print('shallow:', id(shallow))
# print('deep:', id(deep))

# # 2.
# print('\n id-ры первого вложенного списка ([0]):')
# print('original:', id(original[0]))
# print('alias:', id(alias[0]))
# print('shallow:', id(shallow[0]))
# print('deep:', id(deep[0]))

# # 3.
# print('\n id-ры объекта, содержащего первую оценку ([0][1]):')
# print('original:', id(original[0][1]))
# print('alias:', id(alias[0][1]))
# print('shallow:', id(shallow[0][1]))
# print('deep:', id(deep[0][1]))



wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1

print(wrong_matrix)

correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1
print(correct_matrix)

# Мини-эксперимент для наглядности

wrong = [[0] * 3] * 3
correct = [[0] * 3 for i in range(3)]

print("wrong:  id строк =", [id(row) for row in wrong])
print("correct: id строк =", [id(row) for row in correct])

wrong[0][0] = 1
correct[0][0] = 1

print("wrong:  ", wrong)
print("correct:", correct)
