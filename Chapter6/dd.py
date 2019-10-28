users = {
    "scientist": {
    "first" : "albert",
    "last" : "einstein",
    "location" : "princeton",
    },

}

# scientist is the key for alberrt einstein
for username, user_info in users.items():
    print(f"\n Username: {username}")
    print(f"\n fullname: {user_info['first']} and {user_info['last']}")
