import re
pattern = r'^[456](\d{15}|\d{3}(-\d{4}){3})$'

for _ in range(int(input())):
    card = input()
    if re.match(pattern, card):
        
        clean_card = card.replace('-', '')
        
        if re.search(r'(\d)\1{3,}', clean_card):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")