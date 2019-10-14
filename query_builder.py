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
            expansion_set =  expansion_set.union( expand_exlusions(item) )
    return expansion_set

def gen_not_like_clause( exclusion, exclusion_column = "ingredients" ):
    return "%s NOT LIKE %%%s%%" % (exclusion_column, exclusion)

def gen_inclusion( inclusion, item_column_name= "item"):
    return "%s LIKE %%%s%%" % (item_column_name, inclusion)

def generate_exclusions( exclusion_list, ing_column_name="ingredients" ):
    full_exclusion_clause = " AND ".join([gen_not_like_clause(ex) for ex in exclusion_list])
    return full_exclusion_clause

def generate_inclusions( inclusions, inclusion_column_name="item"):
    full_inclusion_clause = " OR ".join([gen_inclusion(inc) for inc in inclusions])
    return full_inclusion_clause


def generate_search_query( inclusions, exclusions ):
    full_inclusions = generate_inclusions(inclusions)
    full_exclusions = generate_exclusions(exclusions)
    full_query = "SELECT manufacturer, item, ingredients from foods WHERE ( %s ) AND ( %s ) COLLATE NOCASE" % ( full_inclusions, full_exclusions)
    return full_query

# Code to test and run the query generator
def main():
    a = generate_search_query( ["ass"], ["nadeeka", "jenna"] )
    print( a )



if __name__ == "__main__":
    main()
