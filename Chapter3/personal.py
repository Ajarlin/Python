friend_list = ['Arvin', 'Cristian', 'Dante', 'Jesus']
msg = f"This is my friends name {friend_list[0].title()}"

for i in range(len(friend_list)):
    msg = f"This is my friend's name {friend_list[i].title()}"
    print(msg)
