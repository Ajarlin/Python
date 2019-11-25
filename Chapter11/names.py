import name_functions as nf

print("Enter 'q' at any time to quit.")
while True:
    first = input("\n Please give me a first name: ")
    if first is 'q':
        break
    last = input("\n Please give me a last name: ")
    if last is 'q':
        break

    fullname = nf.get_formatted_name(first, last)
    print(f"\n Your name formatted: {fullname}")
