from persongenerator import persons
import random

def generate_hierarchy():
    # Generate a hierarchy of persons in a cult-like organization
    cult_leader = random.choice(persons)
    cult_leader['position'] = 'Cult Leader'
    sidemen = random.sample(persons, min(2, len(persons) - 1))
    for sideman in sidemen:
        sideman['position'] = 'Sideman'
        sideman['superior'] = cult_leader['id']
    for person in persons:
        if 'position' not in person:
            person['position'] = 'Follower'
            person['superior'] = random.choice(sidemen)['id']
    return persons

# Example usage:
persons = generate_hierarchy()
for person in persons:
    print(person)