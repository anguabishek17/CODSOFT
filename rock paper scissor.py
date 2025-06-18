def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors Game!")
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors or quit to exit): ").lower()

        if user_choice == 'quit':
            print("Thanks for playing!")
            break

        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        
        print("For computer's choice:")
        print("Type 0 for Rock")
        print("Type 1 for Paper")
        print("Type 2 for Scissors")
        
        comp_input = input("Enter the number for computer's choice: ")

        if comp_input not in ['0', '1', '2']:
            print("Invalid computer input. Please enter 0, 1, or 2.")
            continue

        computer_choice = choices[int(comp_input)]
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a Tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You Win!")
        else:
            print("You Lose!")


rock_paper_scissors()
