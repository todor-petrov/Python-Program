from project.room import Room


class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room and not room.is_taken and people <= room.capacity:
            room.is_taken = True
            room.guests = people

    def free_room(self, room_number):
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room and room.is_taken:
            room.is_taken = False
            room.guests = 0

    def status(self):
        total_guests = sum([r.guests for r in self.rooms])
        free_rooms = [str(r.number) for r in self.rooms if r.is_taken is False]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken is True]
        return f"Hotel {self.name} has {total_guests} total guests\n"\
               f"Free rooms: {', '.join(free_rooms)}\n"\
               f"Taken rooms: {', '.join(taken_rooms)}"
