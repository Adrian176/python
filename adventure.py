room_list = []
room = []
room = ["You are in a stinky room, You see another room to the north, and a hallway to the east.",3,1,None,None]
room_list.append(room)
room = ["You are in the hallway, you go south and enter another room.",4,2,None,0]
room_list.append(room)
room = ["You enter the dining room; you look around and go take a break.",5,None,None,1]
room_list.append(room)
room = ["You are in a bedroom; you look around and lay down.",None,4,0,None]
room_list.append(room)
room = ["You are in the hallway, this time you go north and look around.",6,5,1,3]
room_list.append(room)
room = ["libs",None,None,2,4]
room_list.append(room)
room = ["You enter the balcony, you look at the view and enter another dimension.", None,None,4,1]
room_list.append(room)
current_room = 0
done = False
next_room = ""
while not done:
print()
print(room_list[current_room]
[0]
)
direction = input("What do you want to do?")
if direction == "n":
next_room = room_list[current_room]
[1]
elif direction == "e":
next_room = room_list[current_room]
[2]
elif direction == "s":
next_room = room_list[current_room]
[3]
elif direction == "w":
next_room = room_list[current_room]
[4]
else:
print()
print("I don't understand.")
if next_room == "None":
print("You can't go that!")
else:
current_room = next_room
