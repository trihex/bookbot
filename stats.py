
def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    character_counts = {}
    for char in text:
        if char.lower() not in character_counts:
            character_counts[char.lower()] = 1
        else:
            character_counts[char.lower()] += 1
    return character_counts

def sort_on(items):
    return items["num"]

def sort_dictionary(dictionary):
    return_val = []
    for key in dictionary:
        item = {"char": key, "num": dictionary[key]}
        return_val.append(item)

    return_val.sort(reverse=True, key=sort_on)
    return return_val