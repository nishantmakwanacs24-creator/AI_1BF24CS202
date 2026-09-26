class VacuumCleaner:
    def __init__(self):
        self.location = "A"
        self.rooms = {}

    def get_room_status(self):
        print("Enter the condition of each room:")
        self.rooms["A"] = input("Is Room A clean or dirty? ").strip().lower()
        self.rooms["B"] = input("Is Room B clean or dirty? ").strip().lower()

    def clean(self):
        if self.rooms[self.location] == "dirty":
            print(f"Room {self.location} is DIRTY.")
            print(f"Cleaning Room {self.location}...")
            self.rooms[self.location] = "clean"
        else:
            print(f"Room {self.location} is already CLEAN.")

    def move(self):
        if self.location == "A":
            print("Moving: Room A -> Room B")
            self.location = "B"
        else:
            print("Moving: Room B -> Room A")

    def show_status(self):
        print("\nCurrent Status:")
        print(f"Room A: {self.rooms['A']}")
        print(f"Room B: {self.rooms['B']}")
        print(f"Vacuum Location: Room {self.location}")
        print("-" * 30)

    def run(self):
        self.get_room_status()

        print("\nInitial State")
        self.show_status()

        self.clean()
        self.show_status()

        self.move()
        self.show_status()

        self.clean()
        self.show_status()

        print("Both rooms have been checked!")


agent = VacuumCleaner()
agent.run()
