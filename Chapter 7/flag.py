prompt="Enter: \n Type 'quit' to stop "
active = True
while active:
   msg = input(prompt)

   if msg == 'quit':
        active = False
   else:
        print(msg)
