def switch_words(phrase):
    new_string = ""
    array = phrase.split()
    while len(array) > 0:
        new_string += array[-1]
        new_string += " "
        array.pop()
    final_string = new_string[:-1]
    return final_string
