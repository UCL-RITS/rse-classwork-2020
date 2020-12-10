class Person:
    """A class to represent an individual and their connections."""

    def __init__(self, name, age, job):
        """Create a new Person with the given name, age and job and no connections."""
        self.name = name
        self.age = age
        self.job = job
        self.connections = dict()

    def add_connection(self, person, relation):
        """Add a new connection to a person"""
        if person in self.connections:
            raise ValueError(f"I already know about {person.name}")
        self.connections[person] = relation

    def forget(self, person):
        """Removes any connections to a person"""
        self.connections.pop(person, None)
        pass


def average_age(group):
    """Compute the average age of the group's members."""
    all_ages = [person.age for person in group]
    return sum(all_ages) / len(group)


if __name__ == "__main__":
    Jill = Person("Jill", 26, "biologist")
    Zalika = Person("Zalika", 28, "artist")
    John = Person("John", 27, "writer")
    Nash = Person("Nash", 34, "chef")

    Jill.add_connection(Zalika, "friend")
    Jill.add_connection(John, "partner")
    Zalika.add_connection(Jill, "friend")
    John.add_connection(Jill, "partner")
    Nash.add_connection(John, "cousin")
    Nash.add_connection(Zalika, "landlord")


    Nash.forget(John)
    John.forget(Jill)

    # Then create the group
    my_group = {Jill, Zalika, John, Nash}

    assert len(my_group) == 4, "Group should have 4 members"
    assert average_age(my_group) == 28.75, "Average age of the group is incorrect!"
    assert len(Nash.connections) == 1, "Nash should only have one relation "
    print("All assertions have passed!")
