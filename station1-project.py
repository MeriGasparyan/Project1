from random import choice 

if __name__ == '__main__':

    noun_1 = input("Please input a noun: ")
    adjective_1 = input("Please input an adjective: ")
    verb_1 = input("Please input a verb: ")
    adjective_2 = input("Please input an adjective: ")
    part_of_body_1 = input("Please input a body part: ")
    verb_2 = input("Please input a verb: ")
    adjective_3 = input("Please input an adjective: ")
    noun_2 = input("Please input a noun: ")
    color_1 = input("Please input a color: ")
    mode_of_transportation = input("Please input a mode of transportation: ")
    number_1 = input("Please input a number: ")
    time_measure = input("Please input a measure of time: ")
    color_2 = input("Please input a color: ")
    noun_3 = input("Please input a noun: ")
    part_of_body_2 = input("Please input a body part: ")
    number_2 = input("Please input a number: ")
    silly_word = input("Please input a silly word: ")
    noun_4 = input("Please input a noun: ")

    nouns = [noun_1, noun_2,noun_3,noun_4]
    adjectives = [adjective_1, adjective_2, adjective_3]
    parts_of_body = [part_of_body_1, part_of_body_2]
    verbs = [verb_1, verb_2]
    colors = [color_1, color_2]
    numbers = [number_1, number_2]

    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    print_adjective_1 = choice(adjectives)
    if print_adjective_1[0] in vowels:
        print_adjective_1 = "an " + print_adjective_1
    else:
        print_adjective_1 = "a " + print_adjective_1


    story = f'''It was about {choice(numbers)} {time_measure} ago when I arrived at the hospital in a {mode_of_transportation}.
     The hospital is {print_adjective_1} place, there are a lot of {choice(adjectives)} {choice(nouns) + 's'} here. There are nurses here who have 
     {choice(colors)} {choice(parts_of_body) + 's'}. If someone wants to come into my room I told them that they have to {choice(verbs)} first.
      I’ve decorated my room with {choice(numbers)} {choice(nouns) + 's'}. Today I talked to a doctor and they were wearing a {choice(nouns) + 's'} on their 
      {choice(parts_of_body) + 's'}. I heard that all doctors {choice(verbs)} {choice(nouns) + "s"} every day for breakfast. The most {choice(adjectives)}
       thing about being in the hospital is the {silly_word} {choice(nouns)} !'''

print(story)