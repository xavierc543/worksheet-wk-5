
# Your name: Xavier Cunningha,              
# Your student ID: 
# You state that the code submitted is wholly written by yourself. 
# Date: 19/10/25    

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"
timer=0

print(f"Time {systime:03} State {state}")

while systime < maxtime:
    timer += 1

    if timer == states[state]:

        if state == "red":
            state = "red_amber"
        elif state == "red_amber":
            state = "green"
        elif state == "green":
            state = "amber"
        elif state == "amber":
            state = "red"

        timer = 0

    systime += 1
    print(f"Time {systime:03} State {state}")


# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14