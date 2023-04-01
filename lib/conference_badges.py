def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    badge_list = ["Hello, my name is " + i + "." for i in names]
    return badge_list

def assign_rooms(names):
    rooms = range(1,9)
    room_list = [f"Hello, {speaker}! You'll be assigned to room {room}!" for speaker, room in zip(names, rooms)] 
    return room_list

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    rooms = assign_rooms(names)
    for room in rooms:
        print(room)
