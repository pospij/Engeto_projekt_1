"""prvni projekt do Engeto online Python Akademie
autor: Jan Pospisil
email: honza@seamaster.cz
discord: Jan P#5449
"""

from task_template import TEXTS
separator = '-' * 50

# prihlaseni uzivatele a vyber textu
users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
username = input('username: ')
password = input('password: ')
print(separator)
if users.get(username) == password:
    print(f'''Welcome to the app, {username}.
We have 3 texts to be analyzed''')
else:
    print('!!!Unregistred user, terminating the program!!!')
    quit()
print(separator)
choice = input('Enter number between 1 and 3: ')
if choice not in ['1', '2', '3']:
    print('!!!Wrong number, terminating the program!!!')
    quit()
elif choice.isalpha():
    print('!!!Its not a number, terminating the program!!!')

print(separator)

selected = TEXTS[int(choice) - 1]

# uprava a rozdeleni textu podle zadani
splited = [word.strip(".,") for word in selected.split()]

numer = []
title = []
supper = []
lower = []

for word in splited:
    if word.isnumeric():
        numer.append(word)
    elif word.istitle():
        title.append(word)
    elif word.isupper():
        supper.append(word)
    elif word.islower():
        lower.append(word)
# secteni numerickych stringu
suma = sum(int(number) for number in numer)
print(f'''There are {len(splited)} words in the selected text.
There are {len(title)} titlecase words.
There are {len(supper)} uppercase words.
Thera are {len(lower)} lowercase words.
There are {len(numer)} numeric strings.
The sum of all the numbers is {suma}''')
print(separator)
# rozdeleni textu do slovniku s pocty znaku
quantity_words = {}
for word in splited:
    if len(word) in quantity_words:
        quantity_words[len(word)] += 1
    else:
        quantity_words[len(word)] = 1

# srovnani slovniku
dict_sort = sorted(quantity_words.items())
trans_dict = dict(dict_sort)

# graf poctu slov s poctem pismen
print(f'len|\t occurrences\t |nr.'.upper())
print(separator)
for key, value in trans_dict.items():
    graf = '>' * value
    print(str(key) + '|', graf.ljust(20), '|' + str(value).ljust(5))

print(separator)
quit()
