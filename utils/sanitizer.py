def sanitize(un_sanitized_string):
    words_to_remove = ["episode", "season", "subbed", "dubbed", "english"]
    sanitized_string = un_sanitized_string.lower()
    for word in words_to_remove:
        sanitized_string = sanitized_string.replace(word, "").strip()

    # Find the index of the first parenthesis
    index_of_first_parenthesis = sanitized_string.find("(")

    # Extract the substring before the first parenthesis
    if index_of_first_parenthesis != -1:
        sanitized_string = sanitized_string[:index_of_first_parenthesis].strip()
        return sanitized_string
    else:
        # If there's no parenthesis, return the original string
        return sanitized_string.strip()


def dashed_title(un_dashed_title):
    title = sanitize(un_dashed_title)
    seperator = title.split(" ")
    filtered_list = [item for item in seperator if item and not (str(item).isnumeric())]
    dashed = '-'.join(filtered_list)
    return dashed
