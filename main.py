with open('recipes.txt', encoding='utf-8') as recipe_text:
    cook_book = {}
    for line in recipe_text:
        dish_name = line.strip()
        quantity_ing = int(recipe_text.readline().strip())
        ing_list = []
        ing_str = {}
        for line in range(quantity_ing):
            ing = recipe_text.readline().split('|')
            ing_str['ingredient_name'] = ing[0].strip()
            ing_str['quantity'] = ing[1].strip()
            ing_str['measure'] = ing[2].strip()
            ing_list.append(ing_str)
        cook_book[dish_name] = ing_list
        recipe_text.readline()
    print(cook_book)