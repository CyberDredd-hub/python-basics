#define function
def red_light():
    print("Stop! The light is red")
def yellow_light():
    print("Caution! The light is yellow")
def green_light():
    print("Go! The light is green")
#control state of Traffic light
def traffic_light():
    state = input("Current State of the light:").lower()
    print(f'Current state of the light:{state}')
    return state

if traffic_light == "red":
    red_light()
elif traffic_light == "yellow":
    yellow_light()
elif traffic_light == "green":
    green_light()
else:
    print("Error the state is not red, yellow or green!")


