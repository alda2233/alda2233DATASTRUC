"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-15"

Author:  Mohamed Aldakhil
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = '2024-01-12'
-------------------------------------------------------
"""


from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a Food object by requesting data from a user.
    Use: source = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """
   
    name=input("Name:")
    print("Origin")
    print(Food.origins())
    origin=int(input("Origin:"))
    is_vegetarian=input("Vegetarian (Y/N):")
    if is_vegetarian=='Y':
        is_vegetarian=True
    if is_vegetarian=='N':
        is_vegetarian=False
    calories=int(input("Calories:"))
    
    food=Food(name,origin,is_vegetarian,calories)
    
    return food
    

def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a Food object from a line of string data.
    Use: source = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """
  
        
    parts = line.split("|")
   
    
    
    name = parts[0]
    origin= int(parts[1])
    is_vegetarian=(parts[2])
    if is_vegetarian=="True":
        is_vegetarian=True
    if is_vegetarian=="False":
        is_vegetarian=False
    calories=int(parts[3])
   
    food=Food(name,origin,is_vegetarian,calories)
    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    
    foods = []

    for line in file_variable:
        parts = line.split("|")
        name, origin, is_vegetarian, calories = parts
        origin = int(origin)
        
        if is_vegetarian=="True":
            is_vegetarian=True
        if is_vegetarian=="False":
            is_vegetarian=False
            
        calories = int(calories)
        food = Food(name, origin, is_vegetarian, calories)
        foods.append(food)

    return foods
    
    
    

def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of Food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file variable)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    
    for food in foods:
        # Create a string representation of the food object
        food_str = f"{food.name}|{food.origin}|{food.is_vegetarian}|{food.calories}\n"
        # Write the string to the file
        file_variable.write(food_str)
    
def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian Food objects.
    foods is unchanged.
    Use: v_foods = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
   
    veggies = []
    for food in foods:
        if food.is_vegetarian:
            veggies.append(food)
    return veggies

def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of Food objects by origin.
    foods is unchanged.
    Use: o_foods = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    

    origins=[]
    
    for i in foods:
        if i.origin==origin:
            origins.append(i)

        
    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """

    cal=0
    count=0
    for i in foods:
        cal+=i.calories
        count+=1
    
    avg=cal/count
    
    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: by_origin = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    cal=0
    count=0
    for i in foods:
        if i.origin==origin:
            cal+=i.calories
            count+=1
    avg=cal/count
    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of Food objects, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    
    max_origin_length = max(len(origin) for origin in Food.ORIGIN)
    print(f"{ 'Food':<32} { 'Origin':<{max_origin_length}} { 'Vegetarian':<2} { 'Calories':<6}")
    print("-" * 60)

    # Sort the foods list by name
    sorted_foods = sorted(foods, key=lambda x: x.name.lower())

    # Print each food in the sorted list
    for food in sorted_foods:
        print(f"{food.name:<32} {Food.ORIGIN[food.origin]:<{max_origin_length}} {str(food.is_vegetarian):<2} {food.calories:6,d}")
        
        
        

    return None


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for Food objects that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))
    
    result=[]
    
    if is_veg==False:
        for i in foods:
            if i.origin==origin and i.calories==max_cals:
                result.append(i)
        
    
    elif max_cals==0:
        for i in foods:
            if i.origin==origin and i.is_vegetarian==is_veg:
                result.append(i)
    
    elif origin==-1:
         for i in foods:
             if i.calories==max_cals and i.is_vegetarian==is_veg:
                  result.append(i)
                
    else:
        for i in foods:
            if i.origin==origin and i.calories==max_cals and i.is_vegetarian==is_veg:
                result.append(i)
                
    return result 
