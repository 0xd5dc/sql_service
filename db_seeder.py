def user_seeder(size: int):
    pass


def event_seeder(size: int, user_size: int):
    pass


def guest_seeder(size: int, user_size: int, event_size: int):
    pass


if __name__ == '__main__':
    user_seeder(size=50)
    event_seeder(size=100, user_size=50)
    guest_seeder(size=100, user_size=50, event_size=100)
