def find_waldo(str):
    new_str = str.lower()
    if new_str.__contains__('waldo'):
        return "here"
    else:
        return "not here"
