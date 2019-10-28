friend_list = ['Arvin', 'Cristian', 'Dante', 'Jesus']
for i in range(len(friend_list)):
    msg = f"You {friend_list[i].title()} are invited to my birthday party!\n"
    print(msg)

# Jesus can't make it

out_list = friend_list.pop()

print(f"{out_list.title()} couldn't make the party\n")

# New Person

friend_list.insert(0, 'Eric')
friend_list.insert(int(len(friend_list)/2), 'Frank')
friend_list.append('Henry')

for j in range(len(friend_list)):
    msg = f"You {friend_list[j].title()} are invited to my birthday party!\n"
    print(msg)
