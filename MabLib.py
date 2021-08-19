""" Mad Libs Generators
------------------------------
"""

Loop = 1

while (Loop < 10):

    #All the question that the programmed ask the users
    noun = input("Choose a Noun")
    p_noun = input("Choose a plural")
    noun2 = input("choose a noun")
    place = input("Name a place")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("choose a Noun")

    # |Display the story based on the users input
    print("--------------------------------------")
    print("Be kind to your", noun, "-footed", p_noun)
    print("For a duck may be somebody ",noun2)
    print("Be kind to your ", p_noun, "in", place)
    print("where the weather is always", adjective)
    print()
    print("you may think that is the ", noun3)
    print("well , it is ")
    print("---------------------------------------------")

    Loop = Loop + 1
    



