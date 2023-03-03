from py2neo import Graph, Node, Relationship
from chainofcommandgenerator import ordered_persons

# Connect to the Neo4j graph database
graph = Graph("bolt://localhost:7687", auth=("neo4j", "cultgenerator"))

# Create the nodes for each person
nodes = []
for person in ordered_persons:
    node = Node("Person", id = person['id'], name=person['name'], age=person['age'], race=person['race'], gender=person['gender'], position=person['position'])
    nodes.append(node)

# Create the relationships between the persons
#for person in ordered_persons:
#    if 'superior' in person:
#        superior = next(filter(lambda p: p['id'] == person['superior'], ordered_persons))
#        relationship = Relationship(nodes[ordered_persons.index(person)], "REPORTS_TO", nodes[ordered_persons.index(superior)])
#        graph.create(relationship)
        
# Create the nodes for each location
locations = list(set(person['location'] for person in ordered_persons))
location_nodes = []
for location in locations:
    location_node = Node("Location", name=location)
    location_nodes.append(location_node)

# Create the relationships between persons and their locations
for person in ordered_persons:
    person_node = nodes[ordered_persons.index(person)]
    location_node = next(filter(lambda n: n['name'] == person['location'], location_nodes))
    relationship = Relationship(person_node, "BASED_IN", location_node)
    graph.create(relationship)

    if 'superior' in person:
        superior = next(filter(lambda p: p['id'] == person['superior'], ordered_persons))
        superior_node = nodes[ordered_persons.index(superior)]
        relationship = Relationship(person_node, "REPORTS_TO", superior_node)
        graph.create(relationship)
    if 'contact' in person:
        contact = next(filter(lambda p: p['id'] == person['contact'], ordered_persons), None)
        if contact:
            person_node = nodes[ordered_persons.index(person)]
            contact_node = nodes[ordered_persons.index(contact)]
            relationship = Relationship(person_node, "IN_CONTACT_WITH", contact_node)
            graph.create(relationship)        