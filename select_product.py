import BeautyStock
from BeautyStock.Beauty_products import cosmetics_name as td
import price as p
print("Select product:")
print('''1. hair_fall,
2. makeup,
3. face_wash,
4.face_mask''')
cosmetics_name=int(input("Enter the selection (1/2/3/4)"))
if cosmetics_name==1:
    td.cosmetic_selected('hair_fall')
    inp=input("Whether you wanted to know the prices? Say (yes/no)")
    if inp=='yes' or inp=='Yes' or inp=='YES':

    elif:


    else:
        print("non_valid")

elif cosmetics_name==2:
    td.cosmetic_selected('makeup')
elif cosmetics_name==3:
    td.cosmetic_selected('face_wash')
elif cosmetics_name==4:
    td.cosmetic_selected('face_mask')

