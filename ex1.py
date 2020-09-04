def word_transform_2(word_to_transform, word_origin):
    
    word_to_transform = word_to_transform.lower()
    word_origin = word_origin.lower()
    
    if word_to_transform == word_origin:
        return 1
    
    if len(word_origin) != len(word_to_transform):
        return 0
    
    if len(word_origin) >= 33:
        list_of_letters = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        for symbol in word_origin:
            if symbol in list_of_letters:
                list_of_letters.remove(symbol)
        if len(list_of_letters) == 0:
            return 0
    
    dict_to_check = {}
    for i, item in enumerate(word_to_transform):
        
        if item not in dict_to_check:
            
            dict_to_check[item] = word_origin[i]
        
        else:
            
            if dict_to_check[item] != word_origin[i]:
                
                return 0
    return 1

word_to_transform, word_origin = input().split()
print(word_transform_2(word_to_transform, word_origin))