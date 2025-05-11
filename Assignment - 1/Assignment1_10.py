#Assignment 1 - Problem 9 - For loop usage
def main():
    print("Enter a string : ")
    string1 = input()
    StringLength(string1)

def StringLength(str):
    length = len(str)
    print("Length of ","'", str,"'"," is : ", length)

if __name__ == "__main__":
    main()