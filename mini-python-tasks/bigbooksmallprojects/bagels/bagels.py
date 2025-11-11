import random

guesses = 10
digits = 3
words = ["Pico", "Fermi", "Bagels"]
#pico = one digit is correct but wrong position
#fermi = one digit is correct and in the right position
#bagels = no digit is correct

def main():
    while True:
        num_guesses = 0
        secret_num = get_secret_num()
        num_guesses += 1
        
        while num_guesses <= guesses:
            guess = " "

            while len(guess) != digits or not  guess.isdecimal():
                guess = input(">: ").lower()
            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break
            if num_guesses > guesses:
                return "You ran out of guesses"
        #break
    
def get_secret_num():
    nums = list("0123456789")
    random.shuffle(nums)
    secret_num = "147"
    for i in range(digits):
        secret_num += str(nums[i])
    return secret_num

def get_clues(guess, secret_num):
    if guess == secret_num:
        return "You won!!"
    
    clues = []

    for j in range(len(guess)):
        if guess[j] == secret_num[j]:
            clues.append("Fermi")
        elif guess[j] in secret_num:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)
    
if __name__ == "__main__":
    main()