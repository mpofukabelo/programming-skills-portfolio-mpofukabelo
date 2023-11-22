guests = ['emiko', 'mpofu', 'ashley']

allowed_guests = guests[:2]

for guest in allowed_guests:
    print(f"Dear {'mpofu'}, you are invited to dinner.")

for guest in guests:
    if guest not in allowed_guests:
        print(f"Sorry {'ashley'}, the dinner table won't arrive in time. You won't be able to join us for dinner.")
