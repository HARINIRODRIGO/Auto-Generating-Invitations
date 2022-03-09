# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

names = open("Input/Names/invited_names.txt")
invitor_name = names.read()
name = invitor_name.split("\n")
for i in name:
    letter = open(f"Output/ReadyToSend/{i}_letter.txt", "w")
    letter.write(f"Dear {i},\n\nYou are invited to my birthday this Saturday.\n\nHope you can make it!\n\nAngela")
