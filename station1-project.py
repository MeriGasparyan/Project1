from random import choices

if __name__ == '__main__':
    while True:
        template_number = input(
            "Please input 1 or 2 or 3 (The number of template you want): ")
        if template_number in ['1', '2', '3']:
            break
        else:
            print("Please input an apropriate template number")
    template = int(template_number)
    if template == 1:
        adjective_1 = input("Please input an adjective: ")
        verb_1 = input("Please input a verb: ")
        adjective_2 = input("Please input an adjective: ")
        part_of_body_1 = input("Please input a body part: ")
        verb_2 = input("Please input a verb: ")
        adjective_3 = input("Please input an adjective: ")
        noun_2 = input("Please input a noun: ")
        pass
    elif template == 2:
        verb_1 = input("Please input a verb: ")
        verb_2 = input("Please input a verb: ")
        pass
    else:
        adjective_1 = input("Please input an adjective: ")
        adjective_2 = input("Please input an adjective: ")
        adjective_3 = input("Please input an adjective: ")
        noun_2 = input("Please input a noun: ")
        pass

    noun_1 = input("Please input a noun: ")

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
    noun_5 = input("Please input a noun: ")

    nouns = [noun_1, noun_2, noun_3, noun_4, noun_5]
    adjectives = [adjective_1, adjective_2, adjective_3]
    parts_of_body = [part_of_body_1, part_of_body_2]
    verbs = [verb_1, verb_2]
    colors = [color_1, color_2]
    numbers = [number_1, number_2]

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Check if the user inputed a number
    for number in numbers:
        for n in range(len(number)):
            if number[n] not in digits:
                numbers.remove(number)

    if len(numbers) == 0:
        numbers.append(0)

    if len(numbers) < 2:
        numbers.append(numbers[0])

    number_1_print, number_2_print = choices(numbers, k=len(numbers))
    adjective_1_print, adjective_2_print, adjective_3_print = choices(
        adjectives, k=len(adjectives))
    noun_1_print, noun_2_print, noun_3_print, noun_4_print, noun_5_print = choices(
        nouns, k=len(nouns))
    part_of_body_1_print, part_of_body_2_print = choices(
        parts_of_body, k=len(parts_of_body))
    verb_1_print, verb_2_print = choices(verbs, k=len(verbs))
    color_1_print, color_2_print = choices(colors, k=len(verbs))

    # function to add a preposition before adjectives
    def add_preposition(word):
        vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
        if word[0] in vowels:
            word = "an " + word
        else:
            word = "a " + word
        return word

    # A function to make random words plural
    def make_plural_words(word):
        if word[-1] == 's' or word[-1] == 'z' or word[-1] == 'x' or word[-2:] == 'ss' or word[-2:] == 'sh' or word[-2:] == 'ch':
            word += 'es'
        else:
            word += 's'
        return word

    adjective_1_print = add_preposition(adjective_1_print)
    mode_of_transportation = add_preposition(mode_of_transportation)
    noun_1_print = make_plural_words(noun_1_print)
    noun_3_print = add_preposition(noun_3_print)
    part_of_body_1_print = make_plural_words(part_of_body_1_print)
    if int(number_1_print) > 1:
        time_measure = make_plural_words(time_measure)
    if int(number_2_print) > 1:
        noun_2_print = make_plural_words(noun_2_print)

    story_1 = f'''It was about {number_1_print} {time_measure} ago when I arrived at the hospital in {mode_of_transportation}.
                The hospital is {adjective_1_print} place, there are a lot of {adjective_2_print} {noun_1_print} here. There are nurses here who have 
                {color_1_print} {part_of_body_1_print}. If someone wants to come into my room I told them that they have to {verb_1_print} first.
                I’ve decorated my room with {number_2_print} {noun_2_print}. Today I talked to a doctor and they were wearing {noun_3_print} on their 
                {part_of_body_1_print}. I heard that all doctors {verb_2_print} {noun_4_print} every day for breakfast. The most {adjective_3_print}
                thing about being in the hospital is the {silly_word} {noun_5_print}!'''

    story_2 = f'''This weekend I am going camping with ( Proper Noun (Person’s Name)).
                I packed my lantern, sleeping bag, and {noun_1_print}. 
                I am so (Adjective (Feeling)) to {verb_1_print} in a tent.
                I am (Adjective (Feeling) 2) we might see a(n) (Animal), I hear they’re kind of dangerous. 
                While we’re camping, we are going to hike, fish, and {verb_2_print}. 
                I have heard that the {color_1_print} lake is great for ( Verb (ending in ing) ).
                Then we will (Adverb (ending in ly)) hike through the forest for {number_1_print} {time_measure}. 
                If I see a {color_2_print} (Animal) while hiking, I am going to bring it home as a pet! At night we will tell {number_2_print}
                {silly_word} stories and roast {noun_1_print} around the campfire!!'''

    story_3 = f''' Dear (Proper Noun (Person’s Name) ), I am writing to you from {adjective_1_print} castle in an enchanted forest.
                I found myself here one day after going for a ride on a {color_1_print} (Animal) in (Place). 
                There are {adjective_2_print} (Magical Creature (Plural)) and {adjective_3_print} (Magical Creature (Plural)2) here!
                In the ( Room in a House) there is a pool full of {noun_1_print}.
                I fall asleep each night on a {noun_2_print} of (Noun(Plural)3) and dream of (Adjective4) ( Noun (Plural)4). 
                It feels as though I have lived here for {number_1_print} {time_measure}. 
                I hope one day you can visit, although the only way to get here now is (Verb (ending in ing)) on a (Adjective5) {noun_5_print}!!'''

    print(story_1)
