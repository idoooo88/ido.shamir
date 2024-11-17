def carbs_or_pro_gr_amount(total_cal_, pro_or_carb_g, fat_g):
    """founds how many grams of carbohydrates or proteins are in a product

    :param total_cal_: all the calories in the product
    :param pro_or_carb_g: number of the proteins or carbs in the products (in grams)
    :param fat_g: number of the fats in the products (in grams)
    :type total_cal_: float or int
    :type pro_or_carb_g: float or int
    :type fat_g: float or int
    :return: amount of carbs or protein (in grams)
    :rtype: float or int
    """
    return (total_cal_ - (pro_or_carb_g * 4 + fat_g * 9)) / 4


def percent(my_tuple, num_percent):
    """The function receives in the first parameter a tuple consisting of one number or several numbers,
    each of which is an element within the tuple. The second parameter indicates the percentage by which each of the
    elements in the table will be multiplied, (for example: if the user writes 200 in the second parameter,
    it means 200 percent, which is 2 times the original number).
    The function will return a tuple after calculating the percentages

     :param my_tuple: the basic tuple, every item is a number only
     :param num_percent: the percent number for the result (0-100)
     :type my_tuple: tuple
     :type num_percent: int
     :return: new tuple with the result after multiply with the percent, respectively
     :rtype: tuple
     """
    new_list = []
    for number in my_tuple:
        new_list.append(number * num_percent / 100)
    return tuple(new_list)


def sum_calories_t_or_f(total_cal_, pro_g, carbs_g, fat_g):
    """verifies that the sum of all three micronutrients, protein, carbs and fat,  is approximately the total number
    of calories
    :param total_cal_: The
     number of calories in the food
    :param pro_g: the number of protein in grams
    :param carbs_g: the number of carbs in grams
    :param fat_g: the number of fat in grams
    :return: True - if the protein + carbs + fat are equal (or close) to total cal. False if not
    :type: total_cal, pro_g, carbs_g, fat_g: float or int
    :rtype: bool
    """
    return abs(total_cal_ - (pro_g + carbs_g) * 4 - fat_g * 9) <= 10


def total_cal(protein, carbs, fat):
    return (protein + carbs) * 4 + fat * 9


z = 0, 0, 0, 0


def sum_macronutrients(tuple1, tuple2, tuple3=z, tuple4=z, tuple5=z, tuple6=z, tuple7=z):
    """
    :type tuple1: tuple
    :type tuple2: tuple
    :type tuple3: tuple
    :type tuple4: tuple
    :type tuple5: tuple
    :type tuple6: tuple
    :type tuple7: tuple
    :rtype: tuple
    """
    list_of_the_tuples = [tuple1, tuple2, tuple3, tuple4, tuple5, tuple6, tuple7]
    sum_of_calll, sum_of_protss, sum_of_carbss, sum_of_fatss = 0, 0, 0, 0
    for each_tuple in list_of_the_tuples:
        sum_of_calll += each_tuple[0]
        sum_of_protss += each_tuple[1]
        sum_of_carbss += each_tuple[2]
        sum_of_fatss += each_tuple[3]
    return round(sum_of_calll, 2), round(sum_of_protss, 2), round(sum_of_carbss, 2), round(sum_of_fatss, 2)













