def NULL_not_found(object: any) -> int:
    if(isinstance(object, float)) and object != object:
        print("Cheese: nan", type(object))
        return
    if object is None:
        print("Nothing : None", type(object))
        return
    elif object is False:
        print("Fake : False", type(object))
        return
    elif object == 0:
        print("Zero: 0", type(object))
        return
    elif object == "":
        print("Empty:", type(object))
        return
    elif object is False:
        print("Fake : False", type(object))
        return
    print("Type not Found")
    return 1