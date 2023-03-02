from persongenerator import persons
import random

locations = ['Kingdom of Tamesia', 'Murgia', 'Kingdom of Kangenland', 'Principality of Karkasenia', 'Bobkia', 'Moschia', 'Ostopyl', 'Cheshyan Sultanate', 'Ari']

def generate_hierarchy():
    # Generate a hierarchy of persons in a cult-like organization
    cult_leader = random.choice(persons)
    cult_leader['position'] = 'Cult Leader'
    cult_leader['location'] = random.choice(locations)
    
    # Assign consorts to unique locations
    available_locations = locations.copy()
    random.shuffle(available_locations)
    consorts = random.sample(persons, min(9, len(persons) - 8))
    for i, consort in enumerate(consorts):
        consort['position'] = 'Consort'
        consort['superior'] = cult_leader['id']
        consort['location'] = available_locations[i % len(available_locations)]
        available_locations.remove(consort['location'])
        
    # Assign followers to a superior and the same location
    for person in persons:
        if 'position' not in person:
            person['position'] = 'Follower'
            superior = random.choice(consorts)
            person['superior'] = superior['id']
            person['location'] = superior['location']
            
    return persons

# Example usage:
ordered_persons = generate_hierarchy()
for person in ordered_persons:
    print(person)
