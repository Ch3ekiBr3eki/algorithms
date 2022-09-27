def is_contains_char(string, letter):
    index = 0
    length = len(string)
    while index <= length:
        current_char = string[index]
        if current_char == letter:
            return True 
        else:
            return False
        index += 1
print(is_contains_char('Hexlet', 'e'))