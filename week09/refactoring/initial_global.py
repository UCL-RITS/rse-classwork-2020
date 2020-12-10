def average_age():
    """Compute the average age of the group's members."""
    all_ages = [person["age"] for person in group.values()]
    return sum(all_ages) / len(group)


def forget(person1, person2):
    """Remove the connection between two people."""
    group[person1]["relations"].pop(person2, None)
    group[person2]["relations"].pop(person1, None)


def add_person(name, age, job, relations):
    """Add a new person with the given characteristics to the group."""
    new_person = {
        "age": age,
        "job": job,
        "relations": relations
    }
    group[name] = new_person


group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend",
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    }
}

nash_relations = {
    "John": "cousin",
    "Zalika": "landlord"
}

add_person("Nash", 34, "chef", nash_relations)

forget("Nash", "John")

if __name__ == "__main__":
    assert len(group) == 4, "Group should have 4 members"
    assert average_age() == 28.75, "Average age of the group is incorrect!"
    assert len(group["Nash"]["relations"]) == 1, "Nash should only have one relation"
    print("All assertions have passed!")
