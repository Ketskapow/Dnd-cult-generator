import random

# Define race distribution
race_dictionary = {
    'Human': 0.25,
    'Elf': 0.15,
    'Dwarf': 0.10,
    'Halfling': 0.10,
    'Half-Elf': 0.10,
    'Half-Orc': 0.05,
    'Gnome': 0.05,
    'Dragonborn': 0.05,
    'Tiefling': 0.03,
    'Minotaur': 0.03,
    'Triton': 0.02,
    'Aasimar': 0.02,
    'Goliath': 0.02,
    'Kenku': 0.02,
    'Yuan-ti Pureblood': 0.01,
    'Tabaxi': 0.01,
    'Genasi': 0.02
}

# create a list of races with probabilities
races = list(race_dictionary.keys())
race_distribution = list(race_dictionary.values())

# Define age range for each race
age_range = {
    'Human': (18, 70),
    'Elf': (25, 250),
    'Dwarf': (40, 350),
    'Halfling': (20, 120),
    'Gnome': (40, 500),
    'Half-Elf': (20, 180),
    'Half-Orc': (18, 60),
    'Dragonborn': (15, 80),
    'Tiefling': (20, 100),
    'Aasimar': (20, 100),
    'Genasi': (20, 150),
    'Goliath': (18, 80),
    'Kenku': (15, 60),
    'Tabaxi': (20, 80),
    'Triton': (20, 200),
    'Yuan-ti Pureblood': (18, 80),
    'Minotaur': (17,150)
}

gender_options = ['Male', 'Female', 'Nonbinary']

gendered_races = ['Human', 'Elf', 'Dwarf', 'Halfling', 'Half-Elf', 'Half-Orc', 'Gnome', 'Dragonborn', 'Tiefling', 'Minotaur', 'Triton', 'Aasimar', 'Goliath']

# Generate 10 persons
persons = []
for i in range(70):
    # Randomly select race based on distribution
    race = random.choices(races, race_distribution)[0]
    
    # Generate age based on race age range
    age = random.randint(age_range[race][0], age_range[race][1])

    #Generate gender based on options
    gender = random.choices(gender_options)[0]
    
    #If gender is male or female, and race is male or female, pull name from corresponding text file.
    if race in gendered_races and gender in ['Male', 'Female']:
        filename = f"data/{race}_{gender}.txt"
        with open(filename) as f:
            names_list = f.readlines()
        name = random.choice(names_list).strip()
    #If gender is nonbinary, but race is gendered, pull name form either text file    
    elif race in gendered_races and gender == 'Nonbinary':
        filename = f"data/{race}_{random.choices(['Male','Female'])[0]}.txt"
        with open(filename) as f:
            names_list = f.readlines()
        name = random.choice(names_list).strip()
    #If race is ungendered, pull name from race file    
    elif race in ['Tabaxi', 'Yuan-ti Pureblood', 'Kenku']:
        filename = f"data/{race}.txt" 
        with open(filename) as f:
            names_list = f.readlines()
        name = random.choice(names_list).strip()
    #If race is genasi, first generate element, then take name from corresponding file, then update race.
    elif race is 'Genasi':
        element = random.choice(['Air', 'Water', 'Fire'])
        filename = f"data/{race}_{element}.txt" 
        with open(filename) as f:
            names_list = f.readlines()
        name = random.choice(names_list).strip()
        race = element + " " + race  

    # Add person to list
    person = {'name': name, 'age': age, 'race': race, 'gender': gender}
    persons.append(person)

# Print list of persons
print(persons)