#Code made by Liam Parker (@realangel1c55 on Instagram), please credit the creator if .
#This is made to be both challenging and fun!

import random
start = 1

while start == 1:
	print('1: Civilizaton VI (AKA Civilization 6)')
	print('2: Legends of Runeterra')
	print('3: Apex Legends')
	print('4: Pokemon Unite')
	print('5: Skyrim')
	print('6: Monster Hunter Rise: Sunbreak')
	print('7: Splatoon 3')
	gameName = int(input('Please select a game from the following list above.'))

	if gameName == 1:
		print('Please disable the "Score" victory option and reroll if you do not own the rolled Civilization.')
		print('The optimal rules of play will be any selected map or difficulty with the "Heroes & Legends", "Secret Societies", and "Corporations & Monopolies" modes added on.')
		Civ6 = {
		'Civs': ['America' , 'America (Rough Rider)' , 'Arabia' , 'Australia' , 'The Aztec' , 'Babylon' , 'Brazil' , 'Byzantine' ,  'Canada' , 'China (Kublai Khan)' , 'China (Qin Shi Huang)' , 'The Cree' , 'The Netherlands' , 'Egypt', 'England (Elanor)' , 'England (Victoria)' , 'Ethiopia' , 'France (Elanor)' , 'France (Catherine Black Queen)' , 'France' , 'Gaul' , 'Georgia' , 'Germany' , 'Gran Columbia' , 'Greece (Pericles)' , 'Greece (Gorgo)' , 'Hungary' , 'The Inca' , 'India (Gandhi)' , 'India (Chandragupta)' , 'Indonesia' , 'Japan' , 'Khmer' , 'The Kongo' , 'Korea' , 'Macedon(ia)' , 'Mali' , 'The Maori' , 'The Mapuche' , 'The Maya' , 'Mongolia (Ghengis Khan)' , 'Mongolia (Kublai Khan)' , 'Norway' , 'Nubia' , 'Ottoman Empire' , 'Persia' , 'Phonenicia' , 'Poland' , 'Portugal' , 'Rome' , 'Russia' , 'Scotland' , 'Scythia' , ' Spain' , 'Sumeria' , 'Sweden' , 'Vietnam' , 'The Zulu'],
		'Wins': ['Science' , 'Domination' , 'Religion' , 'Culture' , 'Diplomacy']
		}

		print(f'Your civilization will be {random.choice(Civ6["Civs"])} and you will win via {random.choice(Civ6["Wins"])}.')


	elif gameName == 2:
		print('Only reroll if you do not have the assigned champions. Otherwise, deckbuilding is completely up to you. Good luck!')
		LoR = {
		'Shurima': ['Akshan' , 'Azir' , "Kai'sa" , 'Nasus' , "Rek'sai" , 'Renekton' , 'Sivir' , 'Taliyah' , 'Xerath' , 'Ziggs' , 'Zilean'],
		'Frelijord': ['Anivia' , 'Ashe' , 'Braum' , 'Gnar' , 'Lissandra' , 'Ornn' , 'Sajuani' , 'Trundle' , 'Tryndamere' , 'Udyr'],
		'Noxus': ['Annie' , 'Darius', 'Draven' , 'Katerina' , 'Leblanc' , 'Riven' , 'Rumble' , 'Sion' , 'Swain' , 'Vladamir'],
		'Bandle City': ['Fizz' , 'Gnar' , 'Heimerdinger' , 'Kennen' , 'Lulu' , 'Norra' , 'Poppy' , 'Rumble' , 'Teemo' , 'Tristana' , 'Veigar' , 'Yummi' , 'Ziggs'],
		'Bilgewater': ['Fizz' , 'Gangplank' , 'Illaoi' , 'Miss Fortune' , 'Nautilus' , 'Nami' , 'Pyke' , 'Tahm Kench' , 'Twisted Fate'],
		'Shadow Isle': ['Elise' , 'Gwen' , 'Hecarim' , 'Kalista' , 'Kindred' , 'Maokai' , 'Nocturne' , 'Senna' , 'Thresh' , 'Veigar' , 'Viego'],
		'Demacia': ['Fiora' , 'Galio' , 'Garen' , 'Jarvan IV' , 'Lucian' , 'Lux' , 'Poppy' , 'Quinn' , 'Shyvana', 'Vayne'],
		'Piltover and Zaun': ['Caitlyn' , 'Ekko' , 'Ezreal' , 'Heimerdinger' , 'Jayce' , 'Jinx' , 'Teemo' , 'Vi' , 'Viktor', 'Seraphine'],
		'Ionia': ['Ahri' , 'Irellia' , 'Karma' , 'Kennen' , 'Lee Sin' , 'Lulu' , 'Master Yi' , 'Shen' , ' Yasuo' , 'Zed'],
		'Targon': ['Arulion Sol' , 'Aphelios' , 'Diana' , 'Leona' , 'Malphite' , 'Pantheon' , 'Soraka' , 'Taric' , 'Yuumi' , 'Zoe'],
		'Runeterra': ['Evelynn' , 'Bard' , 'Jax' , 'Jhin' , 'Kayn', 'Varus']
		}

		region1 = random.choice(list(LoR.keys()))
		region2 = random.choice(list(LoR.keys()))
		print(f'You will use the regions of {region1} and {region2}, using the champions {random.choice(LoR[region1])} and {random.choice(LoR[region2])}.')

	elif gameName == 3:
		print("Reroll if you dont own the rolled Legend. Otherwise, you're stuck with what you got. If you get only Care Package weapons, you may use your hands and grenades until you get one of the weapons. You may not, however, use your hands or grenades if you do not have those as options when you have guns. For cases of rolling a gun and grenades/hands, you cannot run dupes of your weapon.")
		Apex = {
		'Legends': ['Bloodhound' , 'Gibralter' , 'Lifeline' , 'Wraith' , 'Pathfinder' , 'Bangalore' , 'Caustic' , 'Mirage' , 'Octane' , 'Wattson' , 'Crypto' , 'Revenant' , 'Loba' , 'Rampart' , 'Horizon' , 'Fuze' , 'Valkerie' , 'Seer' , 'Ashe' , 'Mad Maggie' , 'Newcastle' , 'Vantage'],
		'Guns': ['Fists' , 'Grenades' , 'P2020' , 'Mozambique' , 'RE-45' , 'Wingman' , 'Peacekeeper' , 'EVA-8' , 'Flatline' , 'R-301' , 'HAVOC' , 'Hemlock' , 'R-99' , 'Prowler' , 'Volt' , 'CAR' , 'G7 Scout' , 'Triple Take' , '3030 Repeater' , 'Charge Rifle' , 'Longbow DMR' , 'Sentinel' , 'Devotion' , 'Spitfire' , 'L-STAR']
		}

	#, 'Kraber' , 'Mastiff' , 'Bochec Compound Bow' , 'Rampage'
	#Use above line next to L-Star if you want Care Package Weapons in the pool
		print(f'Using {random.choice(Apex["Legends"])}, you will run {random.choice(Apex["Guns"])} and {random.choice(Apex["Guns"])} as your weapons')


	elif gameName == 4:
		print('If you get duplicate Held Items, congrats! You get to pick the replacement for the duplication. Top Side and Bottom side are interchangeable, based on if one is full and if the other is not. GLHF!')
		Unite = {
		'Role': ['Top' , 'Bottom' , 'Middle'],
		'Pokemon': ['Mew' , 'Tyranitar' , 'Buzzwole' , 'Glaceon' , 'Delphox' , 'Espeon' , 'Azumarill' , 'Duraludon' , 'Hoopa' , 'Aegislash' , 'Trevanent' , 'Dragonite' , 'Tsareena' , 'Decidueye' , 'Sylveon' , 'Mamoswine' , 'Blastoise' , 'Blissy' , 'Gardevoir' , 'Zeraora' , 'Pikachu' 'Charizard' , 'Snorlax' , 'Crustle' , 'Greninja' , 'Eldegoss' , 'Talonflame' , 'Lucario' , 'Venasaur' , 'Mr. Mime' , 'Slowbro' , 'Absol' , 'Machamp' , 'Wigglytuff' , 'Alolan Ninetails' , 'Cramorant' , 'Gengar' , 'Garchomp' , 'Cindrance' , 'Clefable' , 'Scizor' , 'Dodrio'],
		'Held Items': ['Muscle Band' , 'Scope Lens' , 'Shell Bell' , 'Wise Glasses' , 'Focus Band' , 'Energy Amplifier' , 'Float Stone' , 'Buddy Barrier' , 'Score Shield' , 'Aeos Cookie' , 'Attack Weight' , 'Sp. Attack Specs' , 'Leftovers' , 'Exp. Share' , 'Assault Vest' , 'Rocky Helmet' , 'Razor Claw' , 'Choice Specs' , 'Weakness Policy']
		}
	
		print(f'Using {random.choice(Unite["Pokemon"])} in the {random.choice(Unite["Role"])} position, you will equip {random.choice(Unite["Held Items"])}, {random.choice(Unite["Held Items"])}, and {random.choice(Unite["Held Items"])}.')


	elif gameName == 5:
		print('The Skyrim edition of RandGame will pick your Race, Standing Stone Blessing, Point Array, and six skills you will use frequently, two from each category. Have fun with it!')
		Skyrim = {
		'Health': ['1' , '2' , '3'],
		'Magika': ['1', '2' , '3' , '4' , '5'],
		'Stamina': ['1' , '2' , '3' , '4'],
		'Race': ['Nord' , 'Breton' , 'Imperial' , 'Redguard' , 'Dark Elf' , 'Wood Elf' , 'High Elf' , 'Orc' , 'Khajiit' , 'Argonian'],
		'Blessing':['The Apprentice' , 'The Atronach' , 'The Lady' , 'The Lord' , 'The Lover' , 'The Mage' , 'The Ritual' , 'The Serpent' , 'The Shadow' , 'The Steed' , 'The Theif' , 'The Tower' , 'The Warrior'],
		'CSkill': ['Smithing' , 'Heavy Armor' , 'Block' , 'Two-Handed' , 'One-Handed' , 'Archery'],
		'SSkill': ['Light Armor' , 'Sneak' , 'Lockpicking' , 'Pickpocket' , 'Speech' , 'Alchemy'],
		'MSkill': ['Illusion' , 'Conjuration' , 'Destruction' , 'Restoration' , 'Alteration' , 'Enchanting']
		}

		print(f'Your race is {random.choice(Skyrim["Race"])} and your M/H/S point array is {random.choice(Skyrim["Magika"])}/{random.choice(Skyrim["Health"])}/{random.choice(Skyrim["Stamina"])}. Your Standing Stone Blessing will be {random.choice(Skyrim["Blessing"])} and your primary skills, two of each type, will be {random.choice(Skyrim["MSkill"])}, {random.choice(Skyrim["MSkill"])}, {random.choice(Skyrim["SSkill"])}, {random.choice(Skyrim["SSkill"])}, {random.choice(Skyrim["CSkill"])}, and {random.choice(Skyrim["CSkill"])}.')

	
	elif gameName == 6:
		Rise = {
		'Weapons': ['Great Sword' , 'Long Sword' , 'Sword and Shield' , 'Dual Blades' , 'Switch Axe' , 'Charge Blade' , 'Hammer' , 'Hunting Horn' , 'Lance' , 'Gunlance' , 'Insect Glaive' , 'Bow' , 'Heavy Bowgun' , 'Light Bowgun'],
		'Quest Type': ['Hunt' , 'Arena' , 'Capture' , 'Anomaly' , 'Rampage'],
		'Monsters' : ['Chameleos' , 'Risen Chameleos' , 'Crimson Glow Valstrax' , 'Gaismagorm' , 'Gore Magala' , 'Shagaru Magala' , 'Kushala Daora' , 'Teostra' , 'Wind Serpent Ibushi' , 'Thunder Serpent Narwa' , 'Narwa the Allmother' , 'Malzeno' , 'Apex Arzuros' , 'Apex Rathian' , 'Apex Rathalos' , 'Apex Zinogre' , 'Apex Mizutsune' , 'Apex Diablos' 'Aknosom' , 'Almudron' , 'Magma Almudron' , 'Anjanath' , 'Arzuros' , 'Astalos' , 'Barioth' , 'Barroth' , 'Basarios' , 'Bezelguese' , 'Seething Bezelguese' , 'Bishaten' , 'Blood Orange Bishaten (AKA Bob)' , 'Damiyo Hermitaur' , 'Diablos' , 'Espinas' , 'Flaming Espinas' , 'Rajang' , 'Furious Rajang' , 'Somnacanth' , 'Aurora Somnacanth' , 'Garangolm' , 'Rathian' , 'Gold Rathian' , 'Goss Harag' , 'Great Baggi' , 'Great Izuchi' , 'Great Wroggi' , 'Jyuratodus' , 'Khezu' , 'Kulu-Ya-Ku' , 'Lagombi' , 'Nargacuga' , 'Lucient Nargacuga' , 'Lunagaron' , 'Magnamalo' , 'Scorned Magnamalo' , 'Mizutsune' , 'Violet Mizutsune' , 'Pukei-Pukei' , 'Rakna-Kadaki' , 'Pyre Rakna-Kadaki' , 'Rathalos' , 'Silver Rathalos' , 'Royal Ludroth' , 'Seregios' , 'Shogun Caenataur' , 'Tentranadon' , 'Tigrex' , 'Tobi-Kadachi' , 'Volvidon' , 'Zinogre']
		}

		print(f'Using {random.choice(Rise["Weapons"])} you will complete a {random.choice(Rise["Quest Type"])} quest. Your quest target will be a {random.choice(Rise["Monsters"])}. Please reroll if you do not have access to your target or if no such quest exists. (You may use a hunt quest to capture. If you roll Hunt, you must kill it. Additionally, you may use Event Quests if you cannot find a hunt of the monsters or type you rolled.')


	elif gameName == 7:
		Splatoon3 = {
		'Weapons': ['Blaster' , 'Clash Blaster' , 'Luna Blaster' , 'Range Blaster' , 'Rapid Blaster' , 'Rapid Blaster Pro' , 'Splat Brella' , 'Tenta Brella' , 'Undercover Brella' , 'Inkbrush' , 'Octobrush' , 'Bamboozler 14 MK I' , 'Classic Squiffer' , 'E-Liter 4K' , 'E-Liter 4K Scope' , 'Goo Tuber' , 'Splatterscope' , 'Splat Charger' , 'Dapple Dualies' , 'Dualie Squlchers' , 'Dark Tetra Dualies' , 'Splat Dualies' , 'Glooga Dualies' , 'Carbon Roller' , 'Flingza Roller' , 'Splat Roller' , 'Dynamo Roller' , '.52 Gal' , '.96 Gal' , 'Aerospray MG' , 'Dual Squelcher' , 'H-3 Nozzlenose' , 'L-3 Nozzlenose' , 'Jet Squelcher' , "N-Zap '85", 'Squeezer' , 'Splash-O-Matic' , 'Splattershot' , 'Splattershot Jr.' , 'Splattershot Pro' , 'Sploosh-O-Matic', 'Bloblobber' , 'Explosher' , 'Slosher' , 'Tri-Slosher' , 'Sloshing Machine' , 'Splatana Wiper', 'Splatana Stamper' , 'Ballpoint Splattling' , 'Heavy Splattling' , 'Hydra Splattling' , 'Mini Splattling' , 'Nautilus 47' , 'Tri-Stringer' , 'REEF-LUX 450'],
		'Modes': ['Turf War' , 'Anarchy (Series)' , 'Anarchy (Open)']
		}
		
		print('The randomizer will select your weapon and game mode. If you wanted to play Salmon Run, it is not included here as it is already randomized for you.')
		print(f'Using the {random.choice(Splatoon3["Weapons"])}, you will play {random.choice(Splatoon3["Modes"])} until you win.')


	answer = input('Would you like to randomize again? (Y/N)')
	if answer.upper() == 'Y':
		start = 0
		start = start + 1
	elif answer.upper() == 'N':
		print("Let's play again sometime!")
		start = start + 1
	else:
		print('Invalid answer, please run again.')
		start = start + 1
