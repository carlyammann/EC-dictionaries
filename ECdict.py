infile = open('john.txt', 'r')


words_to_count = ['Father', 'God', 'Christ', 'Spirit', 'spirit', 'life', 'man']

word_counts = {}
for word in words_to_count:
    word_counts[word] = 0 

for line in infile:
    words = line.split()

    for word in words_to_count: 
        word_counts[word] += words.count(word)

for word,count in word_counts.items(): 
    print(f'{word}: {count}')


