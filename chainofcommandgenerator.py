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
    
    eligible_allies = [person for person in persons if person not in consorts + [cult_leader]]

    allies = random.sample(eligible_allies, min(8, len(eligible_allies)-7))
        
    # Assign followers to a superior and the same location
    for person in persons:
        if 'position' not in person:
            person['position'] = 'Follower'
            superior = random.choice(consorts)
            person['superior'] = superior['id']
            person['location'] = superior['location']
            
    for ally in allies:
        contact = random.choice(persons)
        ally['position'] = 'Ally'
        ally['contact'] = contact['id']
        ally['location'] = contact['location']
        del ally['superior']
            
    return persons

# Example usage:
ordered_persons = generate_hierarchy()
for person in ordered_persons:
    print(person)
