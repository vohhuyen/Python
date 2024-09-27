import threading
import random
import time

class GameBot(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.score = 0

    def run(self):
        for _ in range(5):  # Mỗi bot thực hiện 5 lần chơi
            points = random.randint(1, 10)  # Tính điểm ngẫu nhiên từ 1 đến 10
            self.score += points
            print(f"{self.name} scored {points} points.")
            time.sleep(random.uniform(0.1, 0.5))  # Giả lập thời gian chơi

        print(f"{self.name} finished with a total score of {self.score} points.")


def start_game(bot_names):
    bots = []

    # Tạo và khởi động các bot
    for name in bot_names:
        bot = GameBot(name)
        bots.append(bot)
        bot.start()

    # Chờ tất cả các bot hoàn thành
    for bot in bots:
        bot.join()

    print("Game Over!")


if __name__ == "__main__":
    bot_names = ['Bot A', 'Bot B', 'Bot C', 'Bot D']
    start_game(bot_names)
