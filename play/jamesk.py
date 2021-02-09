def knockknock():
    import time
    import random

    knockknock.jokes = {
    'Tank': "You're Welcome... not",
    'Owls': "You're right, Owls 'who'",
    'Cow says': "No, a cow says 'moo'!",
    'Woo': "Wow, someone's excited about knock knock jokes",
    'Water': "Water you doing telling jokes right now? Don’t you have things to do?",
    'Leaf': "Leaf me alone!",
    'Thermos': "Thermos be a better way to get a laugh",
    'Boo': "Don't cry, it's just a joke",
    'Spell': "W.H.O.",
    'Otto': "Otto know; I forgot.",
    'Adore': "Adore is between us, open up!",
    'Two-knee': "Two-knee fish!",
    'Abby': "Abby birthday to you!",
    }

    print('Knock Knock...')
    time.sleep(1)
    print('\t\tWho\'s there?')
    time.sleep(1)
    choice = random.choice(list(knockknock.jokes))
    print(choice)
    time.sleep(1)
    print(f'\t\t{choice} who?')
    time.sleep(1.25)
    print(knockknock.jokes[choice])


