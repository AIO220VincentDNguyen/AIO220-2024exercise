# Read file
a_file = open('/content/P1_data.txt', 'r')
content = a_file.read()
a_file.close()
# Count word appear in file
def Word_count(content):
    content = content.replace('\n', ' ')
    content = content.lower()
    content = content.split()
    word_count = {}
    for word in content:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

print(Word_count(content))