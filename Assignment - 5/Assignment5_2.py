#Assignment 5 - Problem 2 - Find the character is vowel or not

def CheckVowel(str1):
    data = ["a","e","i","o","u"]

    if len(str1) == 1 and str1.isalpha():
        if str1 in data:
            print(str1," is a vowel")
        else:
            print(str1," is not a vowel")
    else:
         print("Invalid input")

def main():

    str1 = input("Enter character : ")

    CheckVowel(str1)

if __name__ == "__main__":
    main()


    # Q2. Vowel or Consonant Check
    # Accept a single character from the user and check if it is a vowel (a, e, i, o, u). If not,
    # print it's a consonant.
    # Expected Input:
    # Enter a character: e
    # Expected Output:
    # 'e' is a vowel.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_2.py
    # Enter character : s45
    # Invalid input

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_2.py
    # Enter character : i
    # i  is a vowel

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_2.py
    # Enter character : g
    # g  is not a vowel