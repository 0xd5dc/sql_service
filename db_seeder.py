import db


def user_seeder(size: int):
    """
    :rtype: list
    :return generated a list of user objects with a specific size
    """
    return [db.User() for _ in range(size)]


def event_seeder(size: int, user_size: int):
    """
    :rtype: list
    :return generated a list of event objects with a specific size
    """
    pass


def guest_seeder(size: int, user_size: int, event_size: int):
    """
    :rtype: list
    :return generated a list of guest objects with a specific size
    """
    pass


if __name__ == '__main__':
    user_seeder(size=50)
    event_seeder(size=100, user_size=50)
    guest_seeder(size=100, user_size=50, event_size=100)
