names = open("Input/Names/invited_names.txt")
invitor_name = names.read()
name = invitor_name.split("\n")
for i in name:
    letter = open(f"Output/ReadyToSend/{i}_letter.txt", "w")
    letter.write(f"Dear {i},\n\nYou are invited to my birthday this Saturday.\n\nHope you can make it!\n\nAngela")
