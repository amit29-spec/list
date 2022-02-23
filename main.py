import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def names():
    user = (input("ENTER A WORD\n")).upper()
    try:
        result = [new_dict[letter] for letter in user]
    except KeyError:
        print("Sorry there is no such word")
        names()
        pass
    else:
        print(result)
names()

