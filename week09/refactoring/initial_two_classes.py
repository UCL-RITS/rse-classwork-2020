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
        return len(self.members)

    def contains(self, name):
        """Check whether the group contains a person with the given name.
        Useful to throw errors if we try to add a person who already exists or forget someone.
        """
        return any(member.name == name for member in self.members)

    def add_person(self, name, age, job):
        """Add a new person with the given characteristics to the group."""
        if self.contains(name):
            raise ValueError(f"I already know about {name}.")
        self.members.append(Person(name, age, job))

    def number_of_connections(self, name):
        """Find the number of connections that a person in the group has"""
        # Raise an error if the specified person is not in the group
        if not self.contains(name):
            raise ValueError(f"I don't know about {name}.")
        num_of_con = 0
        for first_person, second_person in self.connections:
            if first_person == name:
                num_of_con = num_of_con+1
        return num_of_con

    def connect(self, name1, name2, relation, reciprocal=True):
        """Connect two given people in a particular way.
        Optional reciprocal: If true, will add the relationship from name2 to name 1 as well
        """
        if not self.contains(name1):
            raise ValueError(f"I don't know who {name1} is.")
        if not self.contains(name2):
            raise ValueError(f"I don't know who {name2} is.")
        if (name1, name2) in self.connections:
            raise ValueError(f"{name1} already knows {name2} as a "
                             f"{self.connections[(name1, name2)]}")
        # The part below is for when the reciprocal relation is needed.
        self.connections[(name1, name2)] = relation
        if reciprocal:
            self.connections[(name2, name1)] = relation


    def forget(self, name1, name2):
        """Remove the connection between two people."""
        # Raise errors
        if not self.contains(name1):
            raise ValueError(f"I don't know who {name1} is.")
        if not self.contains(name2):
            raise ValueError(f"I don't know who {name2} is.")
        if (name1, name2) not in self.connections:
            raise ValueError(f"{name1} does not know {name2} yet.")
        # If pass, remove it
        self.connections.pop((name1, name2))

    def average_age(self):
        """Compute the average age of the group's members."""
        all_ages = [person.age for person in self.members]
        return sum(all_ages) / self.size()


if __name__ == "__main__":
    # Start with an empty group...
    my_group = Group()
    # ...then add the group members one by one...
    my_group.add_person("Jill", 26, "biologist")
    my_group.add_person("Zalika", 28, "artist")
    my_group.add_person("John", 27, "writer")
    my_group.add_person("Nash", 34, "chef")

    # ...then their connections
    my_group.connect("Jill", "Zalika", "friend")
    my_group.connect("Jill", "John", "partner")
    my_group.connect("Nash", "John", "cousin", reciprocal=False)
    my_group.connect("Nash", "Zalika", "landlord", reciprocal=False)
    
    # ... then forget Nash and John's connection
    my_group.forget("Nash", "John")

    assert my_group.size() == 4, "Group should have 4 members"
    assert my_group.average_age() == 28.75, "Average age of the group is incorrect!"
    assert my_group.number_of_connections("Nash") == 1, "Nash should only have one relation"
    print("All assertions have passed!")
