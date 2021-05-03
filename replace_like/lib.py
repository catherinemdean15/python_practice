def replace_like(phrase):
    if 'like' in phrase and 'computer' in phrase:
        new_phrase = phrase.replace('like', 'love')
        return(new_phrase)
    elif 'like' in phrase:
        new_phrase = phrase.replace('like', 'dislike')
        return(new_phrase)
    else:
        return(phrase)
