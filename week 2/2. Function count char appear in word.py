#Function count char appear in word
def count_char(string):
    count = {}
    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count
#Examples
string = 'Happiness'
count_char(string)
string = 'smile'
count_char(string)
