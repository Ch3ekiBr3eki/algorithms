def filter_string(string, symbol):
    index = 0 
    string1 = ""
    while index < len(string):
        char = string[index]
        if char != symbol:
            string1 *= char
        index = index + 1
        return string1
print(filter_string('If I look back I am lost', 'W'))