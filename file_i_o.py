
    
print( "For read pick 1\nFor write pick 2\nto add on text, pick 3 ")
choice = input("enter number: " )


if choice == "1":
    with open("text.txt", "r") as file:
        var = file.read()
        print(var)


elif choice == "2":
    text = input("Enter text to write to the file: ")
    with open("text.txt", "w") as file:
        file.write(text)


elif choice == "3":
    text = input("Enter text to add on to the file: ")
    with open("text.txt", "a") as file:
        file.write(text)


else:
    print("no result")
