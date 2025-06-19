def get_word_count(string): 
    split_string = string.split()
    word_count = len(split_string)
    return word_count

def get_char_count(string):
    char_counts = {}
    for char in string.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def get_sorted_char_count(dict):
   list_of_dicts = [{"char": key, "num": value} for key, value in dict.items()]
   list_of_dicts.sort(reverse=True, key=sort_on)
   return list_of_dicts

def sort_on(dict):
    return dict["num"]