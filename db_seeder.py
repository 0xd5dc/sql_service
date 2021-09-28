from faker import Faker
from db import User, Event, Guest, dal
from random import randint

# use faker to populate the database with dummy data
fake = Faker()


def user_seeder(size: int):
    """
    :rtype: list
    :return generated a list of user objects with a specific size
    """
    return [User(name=fake.name(),
                 password=fake.password(),
                 email=fake.email(),
                 phone=fake.phone_number(),
                 email_confirmed=fake.boolean()) for _ in range(size)]


def event_seeder(size: int, user_size: int):
    """ event_seeder selects random user_id within user_size
    :rtype: list
    :return generated a list of event objects with a specific size
    """
    return [Event(name=fake.sentence(5),
                  intro=fake.sentence(),
                  user_id=randint(1, user_size),
                  is_virtual=fake.boolean(),
                  is_private=fake.boolean()) for _ in range(size)]


def guest_seeder(size: int, user_size: int, event_size: int):
    """ guest_seeder selects random user_id and event_id within user_size and event_size respectfully
    :rtype: list
    :return generated a list of guest objects with a specific size
    """
    return [Guest(user_id=randint(1, user_size),
                  event_id=randint(1, event_size)) for _ in range(size)]


if __name__ == '__main__':
    users = user_seeder(size=50)
    events = event_seeder(size=100, user_size=50)
    guests = guest_seeder(size=100, user_size=50, event_size=100)
    dal.connect()
    session = dal.Session()

    # truncate tables
    session.execute("delete from users")
    session.execute("delete from events")
    session.execute("delete from guests")
    session.commit()

    session.bulk_save_objects(users)
    session.bulk_save_objects(events)
    session.bulk_save_objects(guests)
    session.commit()
