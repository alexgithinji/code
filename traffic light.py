import time

class TrafficLight:
    def __init__(self):
        self.state = "red"

    def change_state(self):
        if self.state == "red":
            self.state = "green"
        elif self.state == "green":
            self.state = "yellow"
        else:
            self.state = "red"

    def display_state(self):
        print(f"Traffic light is {self.state}")

def main():
    traffic_light = TrafficLight()

    while True:
        try:
            traffic_light.display_state()
            time.sleep(2)  # Traffic light stays in a state for 2 seconds
            traffic_light.change_state()
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()









