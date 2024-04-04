#Emma and Allison
#Lab 9 part D

velvet = {"flour":3, "baking soda":1, "cpowder":2, "salt":0.5, "butter":0.5, "sugar":2, "oil":1, "eggs":4, "vanilla":1, "vinegar":1, "coloring":1, "buttermilk":1}
lemon = {"flour":1.5, "baking powder":2, "salt":0.5, "butter":0.5, "sugar":1, "eggs":2, "vanilla":1.5, "milk":0.5, "zest":2}

common_keys = set(velvet).intersection(lemon)
for key in sorted(common_keys):
    print(key,end="\n")
