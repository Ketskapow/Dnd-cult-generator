import random

# Define race distribution
races = ['Human', 'Elf', 'Dwarf', 'Halfling', 'Half-Elf', 'Half-Orc', 'Gnome', 'Dragonborn', 'Tiefling', 'Minotaur', 'Triton', 'Aasimar', 'Goliath', 'Kenku', 'Yuan-ti Pureblood', 'Tabaxi', 'Air Genasi', 'Water Genasi', 'Fire Genasi']
race_distribution = [0.30, 0.15, 0.10, 0.10, 0.10, 0.05, 0.05, 0.05, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02, 0.01, 0.01, 0.05, 0.02, 0.02]\


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

# Generate 10 persons
persons = []
for i in range(70):
    # Randomly select race based on distribution
    race = random.choices(races, race_distribution)[0]
    
    # Generate age based on race age range
    age = random.randint(age_range[race][0], age_range[race][1])

    #Generate gender based on options
    gender = random.choices(gender_options)[0]
    
    if race in ['Human', 'Elf', 'Dwarf', 'Halfling', 'Dragonborn', 'Tiefling', 'Half-Orc', 'Aasimar', 'Gnome', 'Goliath'] and gender in ['Male', 'Female']:
        filename = f"data/{race}_{gender}.txt"
        with open(filename) as f:
            names_list = f.readlines()
        name = random.choice(names_list).strip()
    else:
        name = f"{race} {gender}"

    # Add person to list
    person = {'name': name, 'age': age, 'race': race, 'gender': gender}
    persons.append(person)

# Print list of persons
print(persons)
