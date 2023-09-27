from prob_calculator import Hat, experiment

hat = Hat(yellow=3, blue=2, green=6)
balls_drawn = hat.draw(4)
print(f"Balls drawn: {balls_drawn}")
