keep_running = True

while keep_running:
    restart_prompt = False
    total_sum = 0
    user_input = int(input("Enter a number: "))
    while user_input != 0:
        if user_input > 0:
            total_sum += user_input
        else:
            print("Negative numbers won't be included in the sum!")
        user_input = int(input("Enter a number: "))

    print("Sum of the inputted numbers is:", total_sum)
    restart_prompt = True
    while restart_prompt:
        restart = input("Would you like to restart? (y/n): ")
        if restart.lower() == "y":
            restart_prompt = False
            keep_running = True
        elif restart.lower() == "n":
            restart_prompt = False
            keep_running = False
        else:
            restart_prompt = True
print("Terminated the program!")