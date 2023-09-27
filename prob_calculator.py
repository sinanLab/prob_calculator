import random
from collections import Counter

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents[:]
        balls_drawn = random.sample(self.contents, num_balls)
        for ball in balls_drawn:
            self.contents.remove(ball)
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = Hat(**hat.contents)
        expected_balls_copy = dict(expected_balls)
        balls_drawn = hat_copy.draw(num_balls_drawn)

        for ball in balls_drawn:
            if ball in expected_balls_copy:
                expected_balls_copy[ball] -= 1

        if all(value <= 0 for value in expected_balls_copy.values()):
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability
