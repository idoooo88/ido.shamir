import functions_food
from functions_food import percent
from functions_food import sum_macronutrients
calories, protein_cal, carbs_cal, fat_cal = 0, 0, 0, 0

# A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   Q   Y   Z
avocado = (278, 3.48, 14.8, 25)
avocado_half = (139.0, 1.74, 7.4, 12.5)
apple = (100, 0, 25, 0)  # raw, unpeeled, 182 grams, medium apple
almonds_cho = (88.6, 2.42, 3.36, 7.62)  # 1 square of chocolate 90% + 7 almonds
almonds_7 = (49, 1.8, 1.66, 4.25)  # 7 pieces
almonds_10 = (70.07, 2.57, 2.37, 6.08)  # 10 pieces
banana = (99.1, 1.1, 23, 0.3)  # small.  120 grams unpeeled
berries_wood_100 = (57, 1.3, 13.9, 0.6)
beans_green_dose = (69, 1.89, 7.88, 3.28)  # 100 gr cocked, i added 3 gr fats
beans_white_100gr = (142, 9.7, 25.1, 0.4)
bread = (120, 7, 15, 2.7)  # angel 50 gr whole wheat
bread_halla_angel = (92.25, 4.88, 16.5, 0.77)
bread_halla = (98.28, 3.066, 20.244, 0.504)  # 42 grams = 1 slice
bread_loaf_100gr = scone_100 = (290, 13.2, 38.55, 9.2)  # the weight of loaf bread\scone\finger bun is a 100 gr
bread_loaf_passover_70gr = (170.1, 4.564, 15.4, 10.304)
bread_light = (70.3, 4.9, 10.1, 1.13)  # angel light bread - 35 grams for one
bread_light_3 = (211, 14.7, 30.4, 3.4)  # angel light bread 3 pieces - every piece is 35 grams approximately
bread_Whole_spelled_sourdough_4_66gr = (142.56, 7.65, 25.08, 1.254)
bread_angel_spelled_whole_wheat_4_152gr = (346.56, 18.088, 62.32, 2.888)
burger_vegan_tivol_14pro = (120, 14.1, 7.57, 3.7)
burger_vegan_tivol_99cal = (99, 12.9, 5.32, 2.9)
# break_van_4s_TorCou_50grCereal = pro_break, pro_25_vannila, ss, ss, tortilla_course, ce_ch
break_van_4s_TorCou_50grCereal = (1296.7, 69.5, 163.3, 39.5)
c = (31, 3.3, 1, 1.4)  # 50 ml
cs = (51, 3.3, 6, 1.4)  # coffe and 1 teaspoon sugar
csh = (41, 3.3, 3.5, 1.4)  # coffee and a half teaspoon sugar
c_soy_s = (43.25, 2.48, 5.45, 1.12)  # coffee 75ml soy light green with one teaspoon sugar
carrot_100gr = (41, 0.9, 10, 0.2)
cucumber = (16, 0.68, 3.8, 0.11)  # Raw cucumber (with peel)
cake_yeast_slice_40gr = yeast_cake = (155.6, 2.4, 23.2, 5.6)  # I checked it and 1 piece = 40 gr
cake_marble_slice_40gr = (136, 2.3, 16, 7)
cheese_white5_spoon = (19.6, 1.8, 0.86, 1)  # 1 tablespoon = 20 grams
cheese_pot_9 = (25.2, 2, 0.24, 1.8)  # # 1 tablespoon of pot cheese 9%  - 20 grams according to the internet
cheese_pot_5_100g = (97, 10.1, 3, 5)    # 100 g = 3 tablespoons. 5% fat
cheese_salty = (270, 40, 4.8, 10)  # one whole pack, 200 gr
cheese_yellow = (87, 6, 0.05, 7)  # internet : 25g
cho_splendid = (39.6, 0.62, 1.7, 3.37)  # 1/2 square of chocolate 90% = 12.5 grams
cereals_cru_light_50g = (202, 4.5, 35, 4)  # approximately 50 grams
cereals_cru_light_30g = (122, 2.7, 22.7, 2.3)
cereals_FIBER1 = (154, 4, 31.34, 1.4)  # FIBER1 :  50 grams
cereals_F_C = (178, 4.25, 34.17, 2.7)  # fiber1 and crunch cereals 50 grams
cereals_KELLOGS = (189, 3.5, 42, 0.45)  # 50 gr
cereals_cheerios_50gr_with_suger = (187.5, 4.15, 38.56, 1.85)  # big box 625 gr with honey and almond flavour
cereals_cheer30_cru30 = (235, 5.2, 45.9, 3.4)  # big box 625 gr with honey and almond flavour + crunch no suger
cereals_cheer50_cru30 = (310.0, 6.86, 61.32, 4.14)  # big box 625 gr with honey and almond flavour + crunch no suger
cereals_cheerios_100gr_with_suger = (375.0, 8.3, 77.12, 3.7)
cereals_cornflakes_100gr = (375, 7, 84.7, 0.9)  # flakes = פתיתים
chicken_breast_70gr = (140, 21, 0, 6)  # ready breast -  dose 70 gr plus oil
chicken_wing1_80gr = (100.8, 17.6, 0.0, 2.832)
chicken_leg = (153, 22, 0, 6.7)  # one regular 80 grams of boiled chicken leg
chicken_5_meatballs100g = (143, 10, 10, 7)  # I think 1 = 20gr -> 5 = 100gr
chicken_tight_skinless = (185, 28, 0, 12)  # I added 5 gr of oil
cranberry10g = (30, 0, 7.4, 0.15)  # cranberries suger free
cocoa_10g = (39, 2.4, 1.3, 2.1)
chocolate_shahar_60gr = (302.4, 2.16, 39.0, 15.3)
cho_mazza = (436, 5.52, 67.42, 15.86)
currants_red_100gr = red_currants = (56, 1.4, 12.6, 0)
dates_3 = (67.68, 0.6, 18.0, 0.1)   # tamar, from the palm tree (Dekel tree) according to 3 dates . 1 date = 8 grams
date_1 = (22.3, 0.198, 5.94, 0.033)
egg = (78, 6, 0.6, 5)  # large
egg_2 = (156, 12, 1.2, 10)
egg_wh = (17, 3.6, 0.24, 0.06)  # large white egg only
falafel_ball = (71, 2, 9, 3)  # from internet without even know how many grams is on ball
fish = (128, 26.15, 0, 7.65)  # amnon 1 fish 100 grams + 5 grams of oil
filo_dough_filled_with_meat = (290.4, 6.49, 31.9, 15.18)  # 110 gram
frozen_fruits_200gr_mix = (153, 1, 35, 1)
frozen_fruits_300gr_mix = (229.5, 1.5, 52.5, 1.5)
hummus = (39.84, 1.2, 2.2, 3)  # 1 teaspoon = 16 gr
jehanon_130g = (500.5, 7.8, 52.0, 28.6)  # not accurate! 130 gram I assumed its mother's normal size
meatball = (66.5, 5.25, 3.5, 3.5)  # not accurate!, from internet 1 meat ball - 35 grams
magnum_mini = (174, 2.7, 14.6, 11.6)
mango_100gr = (60.3, 0.8, 12.7, 0.7)  # the amount of the carbohydrate in the ingredients already includes fiber
mango_50g = (32.5, 0.25, 7.6, 0.14)   # the amount of the carbohydrate in the ingredients already includes fiber
milk3_50ml = (30, 1.6, 2.4, 1.5)
milk1_50ml = (22, 1.67, 2.5, 0.5)
milk_soy_light_75ml_green = (23.25, 2.475, 0.45, 1.125)
muller_25_0 = (140, 25, 12.6, 0)
mazza_35g = (134.05, 3.36, 28.42, 0.56)

oil = (119, 0, 0, 13.2)  # 1 tablespoon 15 gr = 3 teaspoon 5 gr
oil_t = (40, 0, 0, 4.44)  # 1 teaspoon 5 gr
oil_t_2 = (80, 0, 0, 8.88)
orange = (98, 1.96, 21.97, 0.25)  # 206 grams regular orange no peel, in my house 266 grams unpeeled!
orange_juice = (84, 1.8, 19.2, 0)  # orange_juice 1 cup 200 ml
olives_10 = (41.4, 0.28, 2.16, 3.96)  # 35 grams by the internet it is 10 olives = 3.5 gr each
oat = (84, 3.6, 14.4, 1.4)  # 2 spoon - 22 gr
passion_fruit_100gr = (97, 2.2, 19, 1.3)  # passiflora in hebrew
potato_170gr = (145, 2.89, 33.8, 1.69)
protein_powder = powder_pro = (130, 25, 4, 1.5)
pro_go20_soy_yogurt = (190, 20, 14.5, 6)
pro20_danone_yogurt_vanilla = (153, 20, 10.3, 2.6)  # small bottle with pic of flower
pro20_danone_yogurt_vanilla_130cal = (130, 20, 11.2, 0)  # small bottle with pic of flower 0 fat
pro_yogurt_yoplait_airy_texture = (123, 20, 6.2, 2)  # vanilla flavour
pro_go_127_drink_yogurt = (127, 20, 9, 1.25)  # banana and strawberry
pro_yogurt_light = (128, 20, 10, 0.8)  # pineapple flavor
pro_go_yogurt_berries = (128, 20, 7.2, 2)
pro20_go_yoplait_cup = (200, 21, 20.02, 4)  # Berry flavored yogurt
pro_soy = (197, 20, 10.75, 7.5)
pro_soy_TNUVA_yogurt_go_20 = (190, 20, 14, 6)  # Strawberry flavor cup color green and black
pro_break = break_pro = (252, 19.95, 29.61, 5.95)
pro_coffee_25_light140 = (140, 25.2, 10, 0)
pro_coffee_25_no_light = (217, 25.2, 17.5, 5.25)
pro_25_vannila = (224.0, 25.2, 18.55, 5.25)
pro_go_yogurt_114cal = (114, 20, 6.4, 0.8)
pro_27_sugar = (278, 27, 26.86, 6.8)  # coffee or vanilla or cookies flavour. high suger
pro_go_25_340ml_Hazelnuts_coffee = (231.2, 25.16, 17.68, 6.8)
pro_42protein = (265.0, 42.0, 17.0, 2.5)
pro_42_half = (132.5, 21.0, 8.5, 1.25)
pineapple_100 = (54, 0.5, 13.1, 0)  # frozen "Tree Of Fruit"
pear = (101, 0.71, 26.7, 0.18)    # 178 gr - medium
potato = (110, 3, 26, 0)  # one 148 grams
pizza100g = (242, 13, 25, 10)
pita = (259, 8.1, 52.9, 1.51)  # 108 gr
pita_half = (129.5, 4.05, 26.45, 0.755)
rice_cooked_spoon_30gr = (34, 0.3, 4.5, 0.5)  # I added 0.5 grams of oil because its cooked
rice_cooked_90gr = (106, 2.2, 23.23, 1.5)  # Medium dose, I added 1.5 grams of oil because its cooked
rice_flakes_150gr = (250, 6.6, 39, 2.1)  # one meal ptitim for me is 150 grams , I added 0.5 oil fat
s = (20, 0, 5, 0)
ss = (40, 0, 10, 0)
sh = (10, 0, 2.5, 0)  # half teaspoon of suger
silan_9g = (28, 0, 7, 0)  # 9 gr
sausage_mini_100g = (210, 13, 8, 14)  # 8 sausage = 100g
shawarma100g = (143, 19.8, 0, 7)
schnitzel_100gr = shnitzel_100 = (207, 15, 14, 10)  # from internet
schnitzel_1_68gr = shnitzel_68 = (140.76, 10.2, 9.52, 6.8)
pasta_spaghetti_cream_100 = (151.6, 4.0, 16.8, 7.6)  # 100 grams
pasta_spaghetti_tomato_sauce_100 = (123, 4, 20, 3)  # when I took on plant it was 160 grams BY THE WAY
pesto_tspoon = (42, 0.27, 1.72, 3.8)
salat_mayonnaise_eggs_50gr = (83, 4.55, 1.8, 6.35)
strawberry_100 = (38, 0.4, 9.1, 0)  # frozen "Tree Of Fruit"
tahini_30gr_raw_2spoons = (180, 6, 0, 19)  # 2 spoons of a raw tahini \ # just to know 1 raw tahini = 2 ready
tahini_15gr_ready_1spoon = (51.5, 1.9125, 0.8025, 5)  # just to know - 1 raw tahini = 2 ready
coating_yogurt = (211, 5.75, 18.75, 13)  # abbreviation acwsc represent : almonds, cranberry. walnuts, silan and cocoa
tomato = (20, 0.9, 3.9, 0.2)
tortilla_light = (98, 3.37, 19, 0.25)
tortilla_wheat_flour_1 = (126.9, 3.375, 23.8, 2.025)  # 45 gram each
tortilla_wheat_flour_2 = (253.8, 6.75, 47.6, 4.05)  # 45 gram each = 90 gr 2
# tortilla_course = tortilla_wheat_flour_2, egg_2, pesto_tspoon, tomato, olives_10, oil_t
tortilla_course = (553.2, 20.2, 56.58, 26.45)
tuna_small = (115, 13.7, 0.1, 6.66)  # 56 grams (drained) small tuna in canola oil
tuna_starkist_oil_100gr_filtered = (194, 26, 0, 10)
tuna_water_starkist = (116, 27, 0, 0.7)
tuna_starkist_oil_84gr_filtered = (162.96, 21.84, 0.0, 8.4)
tuna_Meule_canola_100gr_filtered = (153, 24.9, 0, 7)
walnuts10g = (65, 1.52, 1.37, 6.52)
quinoa_100gr_ready = (120, 4.4, 21.3, 1.92)
# sum_macronutrients(passion_fruit_100gr, mango_100gr, red_currants))
mix_mango_currants_passion_300 = (213.3, 4.4, 44.3, 2.0)  # 100 gr each = 300 gr \ frozen "Tree Of Fruit"
# sum_macronutrients(pineapple_100, strawberry_100, berries_wood_100))
mix_pineapple_berriesWood_strawberry_300 = (149, 2.2, 36.1, 0.6)  # frozen "Tree Of Fruit"
# sum_macronutrients(pro_yogurt_yoplait_airy_texture, almonds_10, cranberry10g, cocoa_10g)
yogurt_10alm_10gcran_10gco = (262.07, 24.97, 17.27, 10.33)

# A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   Q   Y   Z

