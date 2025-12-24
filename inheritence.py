class car:
    color="black"
    def start(self):
        print("Car is started")
    def stop(self):
        print("Car is stopped")

class i10(car):
    color="blue"

c1=i10()

print(c1.start())
print(c1.color)