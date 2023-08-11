print("---add new number(a)\n---search(s)\n---view all contacts(v)\n---close phone book(c): ")
while True:
    contact_ctrl = input("> ")
    if contact_ctrl == "a":
        with open("contact.txt", "a") as f:
            print("---create new contact---")
            name = input("Name: ")
            phone = input("Phone: ")
            f.writelines((name, " : ", phone, "\n"))
    elif contact_ctrl == "s":
        with open("contact.txt", "r") as f:
            u_search = input("--search name or phone_No: ")
            for i in f:
                if u_search in i:
                    print(i)
    elif contact_ctrl == "v":
        with open("contact.txt", "r") as f:
            viewer = f.read()
            print(viewer)
    elif contact_ctrl == "c":
        break
