def all_thing_is_obj(object: any) -> int:
    """This fun. takes any object as an argument and prints its type."""
    if(isinstance(object, str)):
        print(object, "is in the kitchen :", type(object))
    elif(isinstance(object, int)):
        print("Type not found")
    else:
        print(f'{type(object).__name__ } : {type(object)}')
    return 42   