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

def counter(dishes):
    list_dish = []
    dic_dish = {}
    for dish in dishes:
        if dish in list_dish:
            dic_dish[dish] += 1
        else:
            dic_dish[dish] = 1
            list_dish.append(dish)
    return dic_dish



def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for dish_in_book, ingredients in cook_book.items():
            if dish == dish_in_book:
                for ingredient in ingredients:
                    ingredient = list(ingredient.values())
                    measure = ingredient[2]
                    dic_dish = counter(dishes)
                    quantity_dish = dic_dish[dish]
                    total_quantity = int(ingredient[1]) * person_count * quantity_dish
                    shop_list[ingredient[0]] = {'measure': measure, 'quantity': total_quantity}
    return print(shop_list)

order = ['Омлет', 'Омлет', 'Омлет', 'Омлет']
get_shop_list_by_dishes(order, 1)
