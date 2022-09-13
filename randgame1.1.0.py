#Code made by Liam Parker (@realangel1c55 on Instagram), please credit the creator if using
#This is made to be both challenging and fun!

import random

print('1: Civilizaton VI (AKA Civilization 6)')
print('2: Legends of Runeterra')
print('3: Apex Legends')
print('4: Pokemon Unite')
gameName = int(input('Please select a game from the following list above.'))

if gameName == 1:
    print('Please disable the "Score" victory option and reroll if you do not own the rolled Civilization.')
    print('The optimal rules of play will be any selected map or difficulty with the "Heroes", "Secret Societies", and Corporations & Monopolies" modes added on.')
    Civ6 = {
        'Civs': ['America' , 'America (Rough Rider)' , 'Arabia' , 'Australia' , 'The Aztec' , 'Babylon' , 'Brazil' , 'Byzantine' ,  'Canada' , 'China (Kublai Khan)' , 'China (Qin Shi Huang)' , 'The Cree' , 'The Netherlands' , 'Egypt', 'England (Elanor)' , 'England (Victoria)' , 'Ethiopia' , 'France (Elanor)' , 'France (Catherine Black Queen)' , 'France' , 'Gaul' , 'Georgia' , 'Germany' , 'Gran Columbia' , 'Greece (Pericles)' , 'Greece (Gorgo)' , 'Hungary' , 'The Inca' , 'India (Gandhi)' , 'India (Chandragupta' , 'Indonesia' , 'Japan' , 'Khmer' , 'The Kongo' , 'Korea' , 'Macedon(ia)' , 'Mali' , 'The Maori' , 'The Mapuche' , 'The Maya' , 'Mongolia (Ghengis Khan)' , 'Mongolia (Kublai Khan)' , 'Norway' , 'Nubia' , 'Ottoman Empire' , 'Persia' , 'Phonenicia' , 'Poland' , 'Portugal' , 'Rome' , 'Russia' , 'Scotland' , 'Scythia' , ' Spain' , 'Sumeria' , 'Sweden' , 'Vietnam' , 'The Zulu'],
        'Wins': ['Science' , 'Domination' , 'Religion' , 'Culture' , 'Diplomacy']
        }
    print('You will use ' + random.choice(list(Civ6.get('Civs'))) + ' to get a ' + random.choice(list(Civ6.get('Wins'))) + ' victory')


elif gameName == 2:
    print('Only reroll if you do not have the assigned champions. Otherwise, deckbuilding is completely up to you. Good luck!')
    LoR = {
    'Shurima': ['Akshan' , 'Azir' , "Kai'sa" , 'Nasus' , "Rek'sai" , 'Renekton' , 'Sivir' , 'Taliyah' , 'Xerath' , 'Ziggs' , 'Zilean'],
    'Frelijord': ['Anivia' , 'Ashe' , 'Braum' , 'Gnar' , 'Lissandra' , 'Ornn' , 'Sajuani' , 'Trundle' , 'Tryndamere' , 'Udyr'],
    'Noxus': ['Annie' , 'Darius', 'Draven' , 'Katerina' , 'Leblanc' , 'Riven' , 'Rumble' , 'Sion' , 'Swain' , 'Vladamir'],
    'BandleCity': ['Fizz' , 'Gnar' , 'Heimerdinger' , 'Kennen' , 'Lulu' , 'Norra' , 'Poppy' , 'Rumble' , 'Teemo' , 'Tristana' , 'Veigar' , 'Yummi' , 'Ziggs'],
    'Bilgewater': ['Fizz' , 'Gangplank' , 'Illaoi' , 'Miss Fortune' , 'Nautilus' , 'Nami' , 'Pyke' , 'Tahm Kench' , 'Twisted Fate'],
    'ShadowIsle': ['Elise' , 'Gwen' , 'Hecarim' , 'Kalista' , 'Kindred' , 'Maokai' , 'Nocturne' , 'Senna' , 'Thresh' , 'Veigar' , 'Viego'],
    'Demacia': ['Fiora' , 'Galio' , 'Garen' , 'Jarvan IV' , 'Lucian' , 'Lux' , 'Poppy' , 'Quinn' , 'Shyvana'],
    'PiltoverZaun': ['Caitlyn' , 'Ekko' , 'Ezreal' , 'Heimerdinger' , 'Jayce' , 'Jinx' , 'Teemo' , 'Vi' , 'Viktor'],
    'Ionia': ['Ahri' , 'Irellia' , 'Karma' , 'Kennen' , 'Lee Sin' , 'Lulu' , 'Master Yi' , 'Shen' , ' Yasuo' , 'Zed'],
    'Targon': ['Arulion Sol' , 'Aphelios' , 'Diana' , 'Leona' , 'Malphite' , 'Pantheon' , 'Soraka' , 'Taric' , 'Yuumi' , 'Zoe'],
    'Runeterra': ['Evelynn' , 'Bard' , 'Jax' , 'Jhin' , 'Kayn']
    }
    region1 = random.choice(list(LoR.keys()))
    region2 = random.choice(list(LoR.keys()))
    print('Your regions will be ' + region1 + ' and ' + region2 + '. Your champions will be ' + random.choice(LoR[region1]) + ' and ' + random.choice(LoR[region2]))

elif gameName == 3:
    print("Reroll if you dont own the rolled Legend. Otherwise, you're stuck with what you got. If you get only Care Package weapons, you may use your hands and grenades until you get one of the weapons. You may not, however, use your hands or grenades if you do not have those as options when you have guns. For cases of rolling a gun and grenades/hands, you cannot run dupes of your weapon.")
    Apex = {'Legends': ['Bloodhound' , 'Gibralter' , 'Lifeline' , 'Wraith' , 'Pathfinder' , 'Bangalore' , 'Caustic' , 'Mirage' , 'Octane' , 'Wattson' , 'Crypto' , 'Revenant' , 'Loba' , 'Rampart' , 'Horizon' , 'Fuze' , 'Valkerie' , 'Seer' , 'Ashe' , 'Mad Maggie' , 'Newcastle' , 'Vantage'],
            'Guns': ['Fists' , 'Grenades' , 'P2020' , 'Mozambique' , 'RE-45' , 'Wingman' , 'Peacekeeper' , 'EVA-8' , 'Flatline' , 'R-301' , 'HAVOC' , 'Hemlock' , 'R-99' , 'Prowler' , 'Volt' , 'CAR' , 'G7 Scout' , 'Triple Take' , '3030 Repeater' , 'Charge Rifle' , 'Longbow DMR' , 'Sentinel' , 'Devotion' , 'Spitfire' , 'L-STAR']
    }
    #, 'Kraber' , 'Mastiff' , 'Bochec Compound Bow' , 'Rampage'
    #Use above line next to L-Star if you want Package Weapons in the pool
    print('You will use ' + random.choice(list(Apex.get('Legends'))) + ' with the ' + random.choice(list(Apex.get('Guns'))) + ' and the ' + random.choice(list(Apex.get('Guns'))) + ' as your weapons.')


elif gameName == 4:
    print('If you get duplicate Held Items, congrats! You get to pick the replacement for the duplication. Top Side and Bottom side are interchangeable, based on if one is full and if the other is not. GLHF!')
    Unite = {
    'Role': ['Top' , 'Bottom' , 'Middle'],
    'Pokemon': ['Mew' , 'Tyranitar' , 'Buzzwole' , 'Glaceon' , 'Delphox' , 'Espeon' , 'Azumarill' , 'Duraludon' , 'Hoopa' , 'Aegislash' , 'Trevanent' , 'Dragonite' , 'Tsareena' , 'Decidueye' , 'Sylveon' , 'Mamoswine' , 'Blastoise' , 'Blissy' , 'Gardevoir' , 'Zeraora' , 'Pikachu' 'Charizard' , 'Snorlax' , 'Crustle' , 'Greninja' , 'Eldegoss' , 'Talonflame' , 'Lucario' , 'Venasaur' , 'Mr. Mime' , 'Slowbro' , 'Absol' , 'Machamp' , 'Wigglytuff' , 'Alolan Ninetails' , 'Cramorant' , 'Gengar' , 'Garchomp' , 'Cindrance'],
    'HeldItems': ['Muscle Band' , 'Scope Lens' , 'Shell Bell' , 'Wise Glasses' , 'Focus Band' , 'Energy Amplifier' , 'Float Stone' , 'Buddy Barrier' , 'Score Shield' , 'Aeos Cookie' , 'Attack Weight' , 'Sp. Attack Specs' , 'Leftovers' , 'Exp. Share' , 'Assault Vest' , 'Rocky Helmet' , 'Razor Claw' , 'Choice Specs' , 'Weakness Policy']
    }
    
    print('You will use ' + random.choice(list(Unite.get('Pokemon'))) + ' using ' + random.choice(list(Unite.get('HeldItems'))) + ' ' + random.choice(list(Unite.get('HeldItems'))) + ' and ' + random.choice(list(Unite.get('HeldItems'))) + ' going ' + random.choice(list(Unite.get('Role'))))


else:
    print('Game not found, please run again.')
