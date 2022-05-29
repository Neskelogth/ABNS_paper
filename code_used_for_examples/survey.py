from collections import Counter
import matplotlib.pyplot as plt


ans_1 = ['robin', 'robin', 'robin', 'pigeon', 'pigeon', 'Great tit', 'eagle', 'pigeon', 'wren', 'Common nightingale',
         'magpie', 'sparrow', 'common blackbird ', 'parrot']
ans_2 = ['flamingo', 'flamingo', 'Heron', 'common cuckoo', 'canary', 'skylark', 'robin', 'pigeon', 'dove', 'swift',
         'Hummingbird', 'Common nightingale', 'crow', 'common kingfisher']
ans_3 = ['pigeon', 'pigeon', 'penguin', 'hoopoe', 'canary', 'dove', 'Hummingbird', 'robin', 'dove', 'Seagull',
         'parrot', 'crow', 'common blackbird ', 'partridge']
ans_4 = ['robin', 'robin', 'Seagull', 'Seagull', 'pigeon', 'swift', 'penguin', 'peacock', 'hoopoe', 'owl of Athena',
         'quail', 'great spotted woodpecker', 'swift', 'parrot']
ans_5 = ['eagle', 'Great tit', 'white stork', 'magpie', 'Hawk', 'chicken', 'Condor', 'goldfinch', 'pigeon', 'robin',
         'dove', 'swift', 'crow', 'owl']
ans_6 = ['Hawk', 'Hawk', 'common cuckoo', 'common cuckoo', 'Hummingbird', 'Hummingbird', 'eagle', 'magpie', 'crow',
         'common kingfisher', 'sparrow', 'owl of Athena', 'canary', 'common blackbird']
ans_7 = ['dove', 'dove', 'common blackbird', 'common blackbird', 'eagle', 'pigeon', 'Seagull', 'Ibis', 'toucan',
         'magpie', 'Woodpecker', 'Hawk', 'Common nightingale', 'eagle']
ans_8 = ['white stork', 'owl', 'magpie', 'Hawk', 'goldfinch', 'swift ', 'sparrow', 'sparrow', 'crow',
         'Common nightingale', 'kite', 'owl of Athena', 'dove', 'parrot']
ans_9 = ['robin', 'robin', 'eagle', 'common chaffinch', 'bald eagle', 'owl', 'chicken', 'Albatross',
         'common kingfisher', 'vulture', 'pigeon', 'swift ', 'crow', 'common blackbird']
ans_10 = ['Woodpecker', 'Woodpecker', 'toucan', 'penguin', 'magpie', 'Hawk', 'Albatross', 'common blackbird ',
          'turkey', 'Dodo', 'crow', 'nutcracker', 'sparrow']

all_ans = ans_1 + ans_2 + ans_3 + ans_4 + ans_5 + ans_6 + ans_7 + ans_8 + ans_9 + ans_10

for i in range(len(all_ans)):
    all_ans[i] = all_ans[i].lower()

c = Counter(all_ans)
print(c)

print(c.values())

keys = list(c.keys())

for i in range(len(keys)):
    keys[i] = keys[i].capitalize()

plt.bar(keys, c.values())
plt.xticks(rotation=30, ha='right')
plt.show()
