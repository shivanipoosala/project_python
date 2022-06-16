def shows(cosmetics_name):
    cosmetics_list=[]
    product_list=[]
    product_price=[]
    if  cosmetics_name=="hair_fall":
        cosmetics_list=['hair_oil','shampoo','conditioner','hair_mask']
        product_list_dict={'hair_oil':['25ml','50ml','100ml','250ml','500ml'],
                           'shampoo':['25ml','50ml','100ml','250ml','500ml'],
                           'conditioner':['25ml','50ml','100ml','250ml','500ml'],
                           'hair_jell':['25ml','50ml','100ml','250ml','500ml']
                           }
        product_price={'25':['100\-'],



        }
        return product_list_dict

    elif cosmetics_name=="makeup":
        cosmetics_list=['foundation','powder','lipstick','mascara']
        product_list_dict={'foundation':['liquid','dry','powder','jell'],
                           'powder':['white_tone','fruit','sandle_wood','ponds'],
                           'lipstick':['red','pink','purple','blue'],
                           'mascara':['lash','curl','waterproof','fiber']
                           }
        return product_list_dict

    elif cosmetics_name=="face_wash":
        cosmetics_list=['fruit','aloevera','neem','teatree']
        product_list_dict={'fruit':['25ml','50ml','100ml','250ml','500ml'],
                           'aloevera':['25ml','50ml','100ml','250ml','500ml'],
                           'neem':['25ml','50ml','100ml','250ml','500ml'],
                           'teatree':['25ml','50ml','100ml','250ml','500ml']
                           }
        return product_list_dict
    elif cosmetics_name == "face_mask":
        cosmetics_list = ['fruit', 'aloevera', 'neem', 'teatree']
        product_list_dict = {'fruit': ['25ml', '50ml', '100ml', '250ml', '500ml'],
                             'aloevera': ['25ml', '50ml', '100ml', '250ml', '500ml'],
                             'neem': ['25ml', '50ml', '100ml', '250ml', '500ml'],
                             'teatree': ['25ml', '50ml', '100ml', '250ml', '500ml']
                             }
        return product_list_dict


def cosmetic_selected(cosmetics_name):
    if cosmetics_name=="hair_fall":
        print("25ml=100\-\t\t ")
        print(shows(cosmetics_name))
    elif cosmetics_name=="makeup":
        print(shows(cosmetics_name))
    elif cosmetics_name=="face_wash":
        print(shows(cosmetics_name))
    elif cosmetics_name=="face_mask":
        print(shows(cosmetics_name))
