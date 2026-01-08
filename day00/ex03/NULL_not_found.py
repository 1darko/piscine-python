def NULL_not_found(object: any) -> int:
    """
    if(isinstance(object, float)) and object != object:
        print("Cheese: nan", type(object))
        return
    """
    if type(object) == float and object != object:
        print("Cheese: nan", type(object))
    elif object is None:
        print("Nothing : None", type(object))
    elif object is False:
        print("Fake : False", type(object))
    elif object == 0:
        print("Zero: 0", type(object))
    elif object == "":
        print("Empty:", type(object))
    elif object is False:
        print("Fake : False", type(object))
    else:
        print("Type not Found")
        return 1
    return 0