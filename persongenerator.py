import random

# Define race distribution
races = ['human', 'elf', 'dwarf', 'halfling', 'gnome', 'half-elf', 'half-orc', 'dragonborn', 'tiefling', 'aasimar', 'genasi', 'goliath', 'kenku', 'tabaxi', 'triton', 'yuan-ti pureblood', 'minotaur']
race_distribution = [0.30, 0.15, 0.10, 0.10, 0.10, 0.05, 0.05, 0.05, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02, 0.01, 0.01, 0.05]

# Define age range for each race
age_range = {
    'human': (18, 70),
    'elf': (25, 250),
    'dwarf': (40, 350),
    'halfling': (20, 120),
    'gnome': (40, 500),
    'half-elf': (20, 180),
    'half-orc': (18, 60),
    'dragonborn': (15, 80),
    'tiefling': (20, 100),
    'aasimar': (20, 100),
    'genasi': (20, 150),
    'goliath': (18, 80),
    'kenku': (15, 60),
    'tabaxi': (20, 80),
    'triton': (20, 200),
    'yuan-ti pureblood': (18, 80),
    'minotaur': (17,150)
}

gender_options = ['male', 'female', 'nonbinary']

# Generate 10 persons
persons = []
for i in range(70):
    # Randomly select race based on distribution
    race = random.choices(races, race_distribution)[0]
    
    # Generate age based on race age range
    age = random.randint(age_range[race][0], age_range[race][1])

    #Generate gender based on options
    gender = random.choices(gender_options)[0]
    
    if race in ['human', 'elf', 'dwarf', 'halfling', 'dragonborn', 'tiefling', 'half-orc'] and gender in ['male', 'female']:
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
