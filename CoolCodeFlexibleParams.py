def GuestList(*guest):
    guestList = []
    for g in guest:
        guestList.append(g)
    return guestList

# you can enter practically any number of guests in GuestList
myGuests = GuestList('Amit','Sumit','Neha','Maya')
for name in myGuests:
    print(name)