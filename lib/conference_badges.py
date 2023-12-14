def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    badges = []
    for name in names:
        badge = f"Hello, my name is {name}."
        badges.append(badge)
    return badges


def assign_rooms(names):
    rooms = []
    for index, name in enumerate(names, start=1):
        room = f"Hello, {name}! You'll be assigned to room {index}!"
        rooms.append(room)
    return rooms


def printer(names):
    badge_messages = batch_badge_creator(names)
    for message in badge_messages:
        print(message)

    room_assignments = assign_rooms(names)
    for assignment in room_assignments:
        print(assignment)
