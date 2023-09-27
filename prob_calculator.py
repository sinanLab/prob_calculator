import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        num_balls = min(num_balls, len(self.contents))
        balls_drawn = random.sample(self.contents, num_balls)
        for ball in balls_drawn:
            self.contents.remove(ball)
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match_count = 0
    for _ in range(num_experiments):
        hat_copy = Hat(**hat.__dict__)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        drawn_counts = {}
        for ball in balls_drawn:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1
        match = True
        for color, count in expected_balls.items():
            if color not in drawn_counts or drawn_counts[color] < count:
                match = False
                break
        if match:
            match_count += 1
    return match_count / num_experiments
