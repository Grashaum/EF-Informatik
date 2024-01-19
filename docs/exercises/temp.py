import time

def reset_display():
    print("Display has been reset.")

def happy_end():
    time.sleep(3)
    print("😊 Happy smile, playing winner sound")

def sad_end():
    time.sleep(3)
    print("😟 Sad smile, playing loser sound")

def main():
    current_state = "START"
    A_count = 0
    B_count = 0

    while True:
        if current_state == "START":
            reset_display()
            A_count = B_count = 0
            input_action = input("Enter 'A' or 'B'; 'quit' to exit: ").strip()

            if input_action == 'quit':
                break
            elif input_action == 'A':
                current_state = "A#1"
            else:
                current_state = "LOST"

        elif current_state == "A#1":
            A_count += 1
            current_state = "A#2"
        
        elif current_state == "A#2":
            A_count += 1
            input_action = input("Enter 'A' to continue, 'shake' to shake, 'quit' to exit: ").strip()

            if input_action == 'quit':
                break
            elif input_action == 'A':
                current_state = "SHAKE#3"
            elif input_action == 'shake':
                current_state = "LOST"
            else:
                current_state = "LOST"

        elif current_state == "SHAKE#3":
            if A_count >= 2:
                input_action = input("Enter 'shake' to continue, 'quit' to exit: ").strip()

                if input_action == 'quit':
                    break
                elif input_action == 'shake':
                    current_state = "B#4"
                else:
                    current_state = "LOST"
            else:
                current_state = "LOST"

        elif current_state == "B#4":
            B_count += 1
            current_state = "B#5"

        elif current_state == "B#5":
            B_count += 1
            if B_count >= 2:
                current_state = "WIN"
            else:
                current_state = "LOST"

        elif current_state == "WIN":
            happy_end()
            break

        elif current_state == "LOST":
            sad_end()
            break

    print("Game Over.")


main()