import json
def hydrateCards(rawDeckDataPath):
    pack = []
    rawDeckData = json.load(open(rawDeckDataPath,))
    for index, item in enumerate(rawDeckData):
        deck = []
        # print(index,item)
        for i in rawDeckData[item]:
            card ={
                f'{index}':
                    {
                        "name": "",
                        "type": "",
                        "level": None,
                        "spell_name": "",
                        "creature_name": "",
                        "artifact_name": "",
                        "enchantment_name": "",
                        "spell_magnifier": "",
                        "spell_type": "",
                        "name_modifier": "",
                        "creature_modifier": "",
                        "mythic_creature_modifier": "",
                        "location": "",
                        "mythic_location": ""
                     }
                }
            nameSplit = i[0].split()
            card[f'{index}']['name'] = i[0]
            card[f'{index}']['type']= i[1]
            card[f'{index}']['level']=i[2]
            if i[1] == 'spell':
                if len(nameSplit) == 1:
                    card[f'{index}']['spell_name']= i[0]
                elif len(nameSplit) == 2:
                    card[f'{index}']['spell_type']= nameSplit[0]
                    card[f'{index}']['spell_name']= nameSplit[1]
                elif len(nameSplit) == 3:
                    card[f'{index}']['spell_magnifier']=nameSplit[0]
                    card[f'{index}']['spell_type']=nameSplit[1]
                    card[f'{index}']['spell_name']=nameSplit[2]
            elif i[1] == 'artifact':
                if 'Divine Robe' or 'Ghost Wand' in i[0]:
                    if 'Divine Robe' in i[0]:
                        i[0] = i[0].replace('Divine Robe', 'DivineRobe')
                    if 'Ghost Wand' in i[0]:
                        i[0] = i[0].replace('Ghost Wand', 'GhostWand')
                    nameSplit = i[0].split()
                    card[f'{index}']['name'] = i[0]
                if len(nameSplit) == 1:
                    card[f'{index}']['artifact_name']= i[0]
                elif len(nameSplit) == 2:
                    card[f'{index}']['artifact_name']= nameSplit[1]
                    card[f'{index}']['spell_type']= nameSplit[0]
                elif len(nameSplit) == 3:
                    card[f'{index}']['artifact_name']= nameSplit[2]
                    card[f'{index}']['spell_magnifier']= nameSplit[0]
                    card[f'{index}']['spell_type']= nameSplit[1]
            elif i[1] == 'enchantment':
                if len(nameSplit) == 1:
                    card[f'{index}']['enchantment_name']= i[0]
                if len(nameSplit) == 2:
                    card[f'{index}']['enchantment_name']= nameSplit[1]
                    card[f'{index}']['spell_type']= nameSplit[0]
                if len(nameSplit) == 3:
                    card[f'{index}']['enchantment_name']=nameSplit[2]
                    card[f'{index}']['spell_type']=nameSplit[1]
                    card[f'{index}']['spell_magnifier']=nameSplit[0]
            elif i[1] == 'monster':
                card[f'{index}']['type']= 'creature'
                if len(nameSplit) == 1:
                    card[f'{index}']['creature_name']= nameSplit[0]
                if len(nameSplit) == 3:
                    card[f'{index}']['creature_name']= nameSplit[2]
                    card[f'{index}']['creature_modifier']= nameSplit[1]
                    card[f'{index}']['name_modifier']= nameSplit[0]
                if len(nameSplit) >3:
                    keyword = 'of'
                    before_keyword, keyword, after_keyword = i[0].partition(keyword)
                    if i[2] == 2:
                        card[f'{index}']['creature_name']= nameSplit[2]
                        card[f'{index}']['creature_modifier']= nameSplit[1]
                        card[f'{index}']['name_modifier']= nameSplit[0]
                        card[f'{index}']['location']= nameSplit[2] = keyword + after_keyword
                    elif i[2] == 3:
                        card[f'{index}']['creature_name']= nameSplit[2]
                        card[f'{index}']['mythic_creature_modifier']= nameSplit[1]
                        card[f'{index}']['name_modifier']= nameSplit[0]
                        card[f'{index}']['mythic_location']= keyword + after_keyword
            deck.append(card[f'{index}'])
            index +=1
            if len(deck) == 45:
                break
        pack.append(deck)
    return(pack)