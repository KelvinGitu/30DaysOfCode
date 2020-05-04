#the program counts the number of uppercase and lowercase characters in a given string.

def string_test(string_sentence):
    upper_case = 0
    lower_case = 0
    for letter in sentence:
        # define punctuation
        punctuations = """ !()-[]{ };:'"\,<>./?@#$%^&*_~ """
        # remove punctuation from the string
        no_punct = ""
        if letter not in punctuations:
            if letter == letter.upper() and letter != '':
                upper_case += 1
            elif letter == letter.lower() and letter != '':
                lower_case += 1

    print("Number of uppercase letters is: ", upper_case)
    print("Number of lowercase letters is: ", lower_case)
            
sentence = "My name is Bruce BANNER and I'm an Avenger."
string_test(sentence)
