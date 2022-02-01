with open("input/Names/invited_names.txt") as file_names:
    names = file_names.readlines()

with open("input/Letters\starting_letter.txt") as letter:
    content = letter.read()

    for name in names:
        strip_name = name.strip()
        new_content = content.replace("[name]", strip_name)
        with open(f"output/ReadyToSend/letter_to_{strip_name}.txt", "w") as new_letter:
            new_letter.write(new_content)
