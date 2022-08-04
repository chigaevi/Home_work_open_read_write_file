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
# pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for dish_in_book, ingredients in cook_book.items():
            if dish == dish_in_book:
                for ingredient in ingredients:
                    ingredient = list(ingredient.values()) # переводим словарь ingredient в список вида [Название ингредиента, Количество, Единица измерения]
                    measure = ingredient[2]
                    if ingredient[0] in shop_list:
                        total_quantity = shop_list[ingredient[0]]['quantity'] + int(ingredient[1]) * person_count
                    else:
                        total_quantity = int(ingredient[1]) * person_count
                    shop_list[ingredient[0]] = {'measure': measure, 'quantity': total_quantity}
    return pprint(shop_list)

order = ['Омлет', 'Омлет', 'Фахитос']
get_shop_list_by_dishes(order, 2)
