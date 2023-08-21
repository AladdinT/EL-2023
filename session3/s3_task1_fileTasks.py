'''
Session 3
Task 1:
    write a Python program to count the Number of words in a file.
'''
def word_count (fname):
    with open(fname)as f:
        return len((f.read().split()))

'''
Task 2:
    Write a Python program to count the number of lines in a text file.
'''
def line_count (fname):
    with open(fname)as f:
        return len((f.readlines()))

'''
Task 3:
    Write a Python program to write a list content to a file.
'''
def append_list(fname , list):
    with open(fname, mode="a") as f:
        f.write(" ".join(list))

'''
Task 4:
    Write a python program to identify the longest words in a file
'''
def get_longest_word (fname):
    with open(fname, mode="r") as f:
        longest_word = ""
        for word in f.read().split():
            if len(word) > len(longest_word):
                longest_word = word;
    return longest_word

#Testing
print('-'*30)
print(f'file.txt has { word_count("file.txt") } Words')
print(f'file.txt has {line_count("file.txt")} Lines')

append_list("file.txt", ['Red' , 'Orange','Blue' , '\n'])
print(open("file.txt").readlines())

print(get_longest_word("file.txt"))