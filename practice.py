def remove_last_e(str):
    if str[-1] == "e" and str[-2] == "e":
        array = list(str)
        array.pop()
        return(''.join(array))
    else:
        return(str)
