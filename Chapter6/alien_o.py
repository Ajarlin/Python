alien_o = {"color": "green", "points":5}
print(alien_o["color"])
print(alien_o["points"])

alien_o["x_position"] = 0
alien_o["y_position"] = 25

alien_o["color"] = "blue"

del alien_o["points"]

print(alien_o)
