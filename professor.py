import random

def main():
    x = get_level()                                                 # obtains user's specified level using get_level()
    guessing_game(x)                                                # begins the guessing game using the level value created by get_level()

def get_level():                                                    # obtains "level" between 1 and 3 from user
    while True:
        user_level = input("Level: ")
        if user_level.isnumeric() == True and 3 >= int(user_level) > 0: # chosen level must be numeric and between 1 and 3, or else is invalid
            return int(user_level)                                      # returns value of int(user_level)
        else:
            user_level = input("Level: ")                               # if user_level is invalid, re-prompt for input and assign to user_level
            continue

def generate_integer(n):                                        # key function to be used in guessing_game()
    if n == 1:
        return random.randint(0, 9)
    elif n ==2:
        return random.randint(10, 99)                               # these generate random numbers between range (a, b)
    else:
        return random.randint(100, 999)

def guessing_game(n):
    user_score = 0
    i = 0
    j = 0
    while i < 9:                                                # we will have 10 rounds of guessing
        a = generate_integer(n)
        b = generate_integer(n)
        while j <= 2:                                            # repeats question a maximum of three times
            print(f"{a} + {b} = ", end = "")                    # prints, e.g., "5 + 6  = "
            user_guess = input("")
            if int(user_guess) == (a + b):
                user_score += 1
                i += 1                                          # updates user_score upon correct answer
                break
            elif j == 2 and int(user_guess) != (a + b):         # if user answers incorrectly on the third try, prints "EEE" error message
                print("EEE")
                print(f"{a} + {b} = {a + b}")
                break
            elif int(user_guess) != (a + b) or user_guess.isnumeric() == False:     # if user answers incorrectly or places invalid input, prints "EEE" error message
                print("EEE")
                j += 1                                          # updates j on wrong answer; 3 will return "EEE" error message

    print(f"Score: {user_score}")

if __name__ == "__main__":
    main()
