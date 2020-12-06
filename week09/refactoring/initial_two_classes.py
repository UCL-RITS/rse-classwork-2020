class Person:
    """A class to represent an individual."""

    def __init__(self, name, age, job):
        """Create a new Person with the given name, age and job."""
        self.name = name
        self.age = age
        self.job = job

class Group:
    """A class that represents a group of individuals and their connections."""

    def __init__(self):
        """Create an empty group."""
        self.members = []
        self.connections = {}

    def size(self):
        """Return how many people are in the group."""
        group_size = len([member for member in self.members])
        return(group_size)

    def contains(self, name):
        """Check whether the group contains a person with the given name.
        Useful to throw errors if we try to add a person who already exists or forget someone.
        """
        return any(member.name == name for member in self.members)

    def add_person(self, name, age, job):
        """Add a new person with the given characteristics to the group."""
        self.members.append(Person(name, age, job))

    def number_of_connections(self, name):
        """Find the number of connections that a person in the group has"""
        #number =len([connections = name for connections in self.connections])
        number = 0
        if name in self.connections:
            own_connections = self.connections.get(name)        
            number = len(own_connections)
        return (number)

    def connect(self, name1, name2, relation, reciprocal=True):
        """Connect two given people in a particular way.
        Optional reciprocal: If true, will add the relationship from name2 to name 1 as well
        """
        new_entry = {name2 : relation}
        if name1 in self.connections:
            self.connections[name1].update(new_entry)
        else:
            self.connections[name1] = new_entry
        if reciprocal == True:
            new_entry2 = {name1 : relation}
            if name2 in self.connections:
                self.connections[name2].update(new_entry2)
            else:
                self.connections[name2] = new_entry2

    def forget(self, name1, name2):
        """Remove the connection between two people."""
        for person1, relations in self.connections.items():
            for person2, relationship in relations.items():
                if person1 == name1:
                    if person2 == name2:
                        pop_name1 = person1
                        pop_name2 = person2
        self.connections[pop_name1].pop(pop_name2, None)
        self.connections[pop_name2].pop(pop_name1, None)
        
    def average_age(self):
        """Compute the average age of the group's members."""
        all_ages = [person.age for person in self.members]
        return sum(all_ages) / self.size()

if __name__ == "__main__":
    # Start with an empty group...
    my_group = Group()
    # ...then add the group members one by one...
    my_group.add_person('Jill', 26, 'biologist')
    my_group.add_person('Zalika', 28, 'artist')
    my_group.add_person('John',27,'writer')
    my_group.add_person('Nash', 34, 'chef')
    # ...then their connections
    my_group.connect('Jill','Zalika','friend', True)
    my_group.connect('John','Jill','partner', True)
    my_group.connect('John','Nash','cousin', True)
    my_group.connect('Nash','Zalika','landlord')

    # ... then forget Nash and John's connection
    my_group.forget("Nash", "John")

    assert my_group.size() == 4, "Group should have 4 members"
    assert my_group.average_age() == 28.75, "Average age of the group is incorrect!"
    assert my_group.number_of_connections('Nash') == 1, "Nash should only have one relation"
    print("All assertions have passed!")