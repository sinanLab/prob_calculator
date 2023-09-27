from prob_calculator import Hat, experiment

hat = Hat(blue=5, red=4, green=2)
probability = experiment(hat=hat, expected_balls={"red": 1, "green": 2}, num_balls_drawn=4, num_experiments=10000)
print(f"Probability: {probability}")
