#File created by Yogesh Manghnani

import string

if __name__ == "__main__":

    # open file and put names in a list
    file_name = "problem_022.txt"
    file = open(file_name, "r")
    all_names = file.read()
    all_names = all_names.replace('"', '')
    all_names = all_names.split(',')
    all_names.sort()

    # make list of alphabets
    upper_case_alphabets = string.ascii_uppercase
    upper_case_alphabets = list(upper_case_alphabets)

    total_word_score = 0
    for name in all_names:
        curr_name_score = 0
        for char in name:
            curr_name_score += upper_case_alphabets.index(char) + 1

        curr_name_score *= (all_names.index(name) + 1)
        total_word_score += curr_name_score
    print(total_word_score)