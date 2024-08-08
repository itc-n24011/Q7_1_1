name_age = {'tanaka': 35, 'taiki': 25, 'kouta': 27} 

def dict_info(dict_tbl, key):
    try:
        return dict_tbl[key]
    except:
        return 'key is not found'

print(dict_info(name_age, 'taiki'))
print(dict_info(name_age, 'yamada'))
