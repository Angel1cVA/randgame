#Code made by Liam Parker (@realangel1c55 on Instagram), please credit the creator if using

#This is made to be both challenging and fun!

import random


print('1: Civilizaton VI (AKA Civilization 6)')
print('2: League of Legends')
print('3: Apex Legends')
gameName = int(input('Please select a game from the following list above.'))

if gameName == 1:
    print('Please disable the "Score" victory option and reroll if you do not own the rolled Civilization.')
    print('The optimal rules of play will be any selected map or difficulty with the "Heroes", "Secret Societies", and Corporations & Monopolies" modes added on.')
    CivList = ['America' , 'America (Rough Rider)' , 'Arabia' , 'Australia' , 'The Aztec' , 'Babylon' , 'Brazil' , 'Byzantine' , 'Canada' , 'China (Kublai Khan)' , 'China (Qin Shi Huang)' , 'The Cree' , 'The Netherlands' , 'Egypt', 'England (Elanor)' , 'England (Victoria)' , 'Ethiopia' , 'France (Elanor)' , 'France (Catherine Black Queen)' , 'France' , 'Gaul' , 'Georgia' , 'Germany' , 'Gran Columbia' , 'Greece (Pericles)' , 'Greece (Gorgo)' , 'Hungary' , 'The Inca' , 'India (Gandhi)' , 'India (Chandragupta' , 'Indonesia' , 'Japan' , 'Khmer' , 'The Kongo' , 'Korea' , 'Macedon(ia)' , 'Mali' , 'The Maori' , 'The Mapuche' , 'The Maya' , 'Mongolia (Ghengis Khan)' , 'Mongolia (Kublai Khan)' , 'Norway' , 'Nubia' , 'Ottoman Empire' , 'Persia' , 'Phonenicia' , 'Poland' , 'Portugal' , 'Rome' , 'Russia' , 'Scotland' , 'Scythia' , ' Spain' , 'Sumeria' , 'Sweden' , 'Vietnam' , 'The Zulu']
    WinList = ['Science' , 'Domination' , 'Religion' , 'Culture' , 'Diplomacy']
    randCiv = random.choice(CivList)
    randWin = random.choice(WinList)
    print('You will use ' + randCiv + ' to get a ' + randWin + ' Victory.')

elif gameName == 2:
    print('Only reroll if the champion rolled is one you do not own and is not in the free rotation.')
    ChampList = ['Aatrox' , 'Ahri' , 'Akali' , 'Akshan' , 'Alistar' , 'Amumu' , 'Anivia' , 'Annie' , 'Aphelios' , 'Ashe' , 'Aurelion Sol' , 'Azir' , 'Bard' , "Bel'veth" , 'Blitzcrank' , 'Brand' , 'Braum' , 'Caitlyn' , 'Camille' , 'Cassiopeia' , "Cho'gath" , 'Corki' , 'Darius' , 'Diana' , 'Dr. Mundo' , 'Draven' 'Ekko' , 'Elise' , 'Evelynn' , 'Ezreal' , 'Fiddlesticks' , 'Fiora' , 'Fizz' , 'Gallio' , 'Gangplank' , 'Garen' , 'Gnar' , 'Gragas' , 'Graves' , 'Gwen' , 'Hecarim' , 'Heimerdinger' , 'Illaoi' , 'Irelia' , 'Ivern' , 'Janna' , 'Jarvan IV' , 'Jax' , 'Jayce' , 'Jhin' , 'Jinx' , "Kai'sa" , 'Kalista' , 'Karma' , 'Karthus' , 'Kassadin' , 'Katarina' , 'Kayle' , 'Kayn (Blue)' , 'Kayn (Red)' , 'Kennen' , "Kha'zix" , 'Kindred' , 'Kled' , "Kog'maw", 'Leblanc' , 'Lee Sin' , 'Leona' , 'Lillia' , 'Lissandra' , 'Lucian' , 'Lulu' , 'Lux' , 'Malphite' , 'Malzahar' , 'Maokai' , 'Master Yi' , 'Miss Fortune' , 'Mordekaiser' , 'Morgana' , 'Nami' , 'Nasus' , 'Nautilus' , 'Neeko' , 'Nidalee' ,'Nilah' , 'Nocturne' , 'Nunu and Willump' , 'Olaf' , 'Oriana' , 'Ornn' , 'Pantheon' , 'Poppy' , 'Pyke' , 'Qiyana' , 'Quinn' , 'Rakan' , 'Rammus' , "Rek'sai", 'Rell' , 'Renata Glasc' , 'Renekton' , 'Rengar' , 'Riven' , 'Rumble' , 'Ryze' , 'Samira' , 'Sejuani' , 'Senna' , 'Seraphine' , 'Sett' , 'Shaco' , 'Shen' , 'Shyvana' , 'Singed' , 'Sion' , 'Sivir' , 'Skarner' , 'Sona' , 'Soraka' , 'Swain' , 'Sylas' , 'Syndra' , 'Tham Kench' , 'Taliyah' , 'Talon' , 'Taric' , 'Teemo' , 'Thresh' , 'Tristana' , 'Trundle' , 'Tryndamere' , 'Twisted Fate' , 'Twitch' , 'Udyr' , 'Urgot' , 'Varus' , 'Vayne' , 'Veigar' , "Vel'koz" , 'Vex' , 'Vi' , 'Viego' , 'Viktor' , 'Vladamir' , 'Volibear' , 'Warwick' , 'Wukong' , 'Xayah' , 'Xerath' , 'Xin Zhao' , 'Yasuo' , 'Yone' , 'Yorick' , 'Yuumi' , 'Zac' , 'Zed' , 'Zeri' , 'Ziggs' , 'Zilean' , 'Zoe' , 'Zyra']
    BuildPath = ['Crit' , 'Lifesteal' , 'Tank' , 'AP Burst' , 'AD Burst' , 'On-hit' , 'AP' , 'AD' , 'Bruiser/Hybrid' , 'Burn']
    randChamp = random.choice(ChampList)
    randBuild = random.choice(BuildPath)
    print('You will use ' + randChamp + ' going ' + randBuild + '.')

elif gameName == 3:
    print("Reroll if you dont own the rolled Legend. Otherwise, you're stuck with what you got. If you get only Care Package weapons, you may use your hands and grenades until you get one of the weapons. You may not, however, use your hands or grenades if you do not have those as options when you have guns.")
    LegendList = ['Bloodhound' , 'Gibralter' , 'Lifeline' , 'Wraith' , 'Pathfinder' , 'Bangalore' , 'Caustic' , 'Mirage' , 'Octane' , 'Wattson' , 'Crypto' , 'Revenant' , 'Loba' , 'Rampart' , 'Horizon' , 'Fuze' , 'Valkerie' , 'Seer' , 'Ashe' , 'Mad Maggie' , 'Newcastle' , 'Vantage']
    GunList = ['Fists' , 'Grenades' , 'P2020' , 'Mozambique' , 'RE-45' , 'Wingman' , 'Peacekeeper' , 'EVA-8' , 'Flatline' , 'R-301' , 'HAVOC' , 'Hemlock' , 'R-99' , 'Prowler' , 'Volt' , 'CAR' , 'G7 Scout' , 'Triple Take' , '3030 Repeater' , 'Charge Rifle' , 'Longbow DMR' , 'Sentinel' , 'Devotion' , 'Spitfire' , 'L-STAR']
    #, 'Kraber' , 'Mastiff' , 'Bochec Compound Bow' , 'Rampage'
    #Use above line of code after the L-Star to include Care Package Weapons
    randLegend = random.choice(LegendList)
    randGun1 = random.choice(GunList)
    randGun2 = random.choice(GunList)
    print('You will use ' + randLegend + ' with the ' + randGun1 + ' and the ' + randGun2 + ' as your weapons.')

else:
    print('Game not found, please run again.')
