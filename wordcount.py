"""Count words in file."""
def load_txt(filename):
    '''list of words'''
    word_list = open(filename)
    result = []
    for row in word_list:
        word_phrase = row.rstrip(' ').split (' ')
        for word in word_phrase:
            result.append(word)

    return result

word_prep = load_txt('test.txt')

word_count = {}
for item in word_prep:
    word_count[item] = word_count.get(item , 0) + 1

for key, value in word_count.items():
    print(f"{key} = {value}")




# put your code here.
