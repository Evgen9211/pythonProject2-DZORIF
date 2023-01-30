
cook_book ={}
with open('cookbook.txt', 'rt', encoding='utf8') as file:
    for l in file:
        dish = l.strip()
        ingredients = []
        cookbook = {dish: ingredients}
        ingredients_count = file.readline()
        for i in range(int(ingredients_count)):
            ingr = file.readline()
            ingredient_name, quantity, measure = ingr.strip().split(' | ')
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        blank_line = file.readline()
        cook_book.update({dish: ingredients})
print(cook_book, '\n')

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for i in dishes:
        if i in cook_book.keys():
            for l in cook_book[i]:
                person_quantity = int(l['quantity']) * person_count
                shop_list.update({l['ingredient_name']: {'measure': l['measure'], 'quantity': person_quantity}})
    return shop_list
print(get_shop_list_by_dishes(['Запеченный картофель', 'Утка по-пекински'], 2), '\n')


import os

lin_1 = {}
for file in os.listdir('all_files'):
  with open(os.path.join('all_files', file), encoding='utf-8') as f:
    text = f.readlines()
    text_ = "".join(text)
    len_ = len(text)
    lin_1[file] = (f' {len_}\n {text_}\n ')
lin_2 = {}
for x in sorted(lin_1, key=lin_1.get):
  lin_2[x] = lin_1[x]
text_dict = {}
for key, value in lin_2.items():
  with open('all_file.txt', 'a', encoding='utf-8') as f:
    f.writelines(f' {key}\n {value}\n ')
print(lin_2)




