def main():
    userChoice = str(input("Do you want to check the image's size (y/n): ")).lower()
    if userChoice.strip() == "y":
        verifier.verifier()
    elif userChoice.strip() == "n":
        exit()
    else:
        print("Invalid input")
        exit()

if __name__ == '__main__':
    import verifier
    main()