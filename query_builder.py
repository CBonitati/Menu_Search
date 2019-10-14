import sqlite3
#Vegetarian Options	
#Vegan Options	
#Peanut Allergy	
#Lactose Intolerance	
#Celiac Disease (Gluten Free)	
#Kosher	
#Eggs

# Make adjustments to map as needed
EXPAND_MAP = {
    "vegetarian_options": ["meat", "beef", "pork"],
    "vegan_options": ["vegetarian_options", "dairy"],
    "peanut allergy": ["peanut"],
    "lactose": ["milk"],
    "celiac disease (gluten free)": ["gluten", "wheat", "rye", "barley"],
    "kosher": ["pork"],
    "dairy": ["lactose", "cheese"]
}
# Comes from the check boxes
# Expands into a list of exclusions
def expand_exlusions(item_to_expand):
    expansion_set = set( EXPAND_MAP[item_to_expand] )
    for item in expansion_set:
        if item in EXPAND_MAP.keys():
            expansion_set =  expand_exlusions.union( expand_search_term(item) )
    return expansion_set

def generate_exclusions( exclusion_list, ing_column_name="ingredients", item_column_name="item" ):
     
    

# Code to test and run the query generator
def main():
    print( expand_search_term( "vegan_options" ) )

if __name__ == "__main__":
    main()
