import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Chào mừng bạn đến với trò chơi đoán số!")
    print("Tôi đã chọn một số từ 1 đến 100. Hãy đoán xem đó là số nào!")

    while True:
        guess = int(input("Nhập số của bạn: "))
        attempts += 1
        
        if guess < number_to_guess:
            print("Số của bạn thấp hơn.")
        elif guess > number_to_guess:
            print("Số của bạn cao hơn.")
        else:
            print(f"Chúc mừng! Bạn đã đoán đúng số {number_to_guess} sau {attempts} lần đoán.")
            break

    play_again = input("Bạn có muốn chơi lại không? (có/không): ").lower()
    if play_again == "có":
        guess_the_number()

guess_the_number()
