from pprint import pprint

with open('recipes.txt', encoding='utf-8') as recipe_text:
    cook_book = {}
    for line in recipe_text:
        dish_name = line.strip()
        quantity_ing = int(recipe_text.readline().strip())
        ing_list = []
        ing_dic = {}
        for line in range(quantity_ing):
            ing = recipe_text.readline().split('|')
            ing_dic['ingredient_name'] = ing[0].strip()
            ing_dic['quantity'] = ing[1].strip()
            ing_dic['measure'] = ing[2].strip()
            ing_list.append(ing_dic.copy())
        cook_book[dish_name] = ing_list
        recipe_text.readline()
    pprint(cook_book)