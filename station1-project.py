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
        color_1 = input("Please input a color: ")
        part_of_body_1 = input("Please input a body part: ")
        verb_2 = input("Please input a verb: ")
        adjective_3 = input("Please input an adjective: ")
        noun_2 = input("Please input a noun: ")
        mode_of_transportation = input(
            "Please input a mode of transportation: ")
        noun_3 = input("Please input a noun: ")
        part_of_body_2 = input("Please input a body part: ")
        number_2 = input("Please input a number: ")
        silly_word = input("Please input a silly word: ")
        noun_4 = input("Please input a noun: ")
        noun_5 = input("Please input a noun: ")
        pass
    elif template == 2:
        person_name = input("Please input a person's name: ")
        verb_1 = input("Please input a verb: ")
        color_1 = input("Please input a color: ")
        verb_2 = input("Please input a verb: ")
        adverb_ly = input("Please input an adverb with ending -ly: ")
        feeling_1 = input("Please input a feeling: ")
        color_2 = input("Please input a color: ")
        number_2 = input("Please input a number: ")
        verb_ing = input("Please input a verb ending with -ing: ")
        silly_word = input("Please input a silly word: ")
        feeling_2 = input("Please input a feeling: ")
        animal = input("Please input an animal: ")
        pass
    elif template == 3:
        person_name = input("Please input a person's name: ")
        adjective_1 = input("Please input an adjective: ")
        adjective_2 = input("Please input an adjective: ")
        mag_creature_1 = input("Please input a magical creature: ")
        verb_ing = input("Please input a verb ending with -ing: ")
        adjective_3 = input("Please input an adjective: ")
        adjective_4 = input("Please input an adjective: ")
        place = input("Please input a place: ")
        adjective_5 = input("Please input an adjective: ")
        noun_2 = input("Please input a noun: ")
        noun_4 = input("Please input a noun: ")
        mag_creature_2 = input("Please input a magical creature: ")
        noun_5 = input("Please input a noun: ")
        room = input("Please input a room in the house: ")
        animal = input("Please input an animal: ")
        pass

    noun_1 = input("Please input a noun: ")

    number_1 = input("Please input a number: ")
    time_measure = input("Please input a measure of time: ")

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

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
    if int(number_1) > 1:
        time_measure = make_plural_words(time_measure)

    if template == 1:
        noun_1 = make_plural_words(noun_1)
        adjective_1 = add_preposition(adjective_1)
        part_of_body_1 = make_plural_words(part_of_body_1)
        mode_of_transportation = add_preposition(mode_of_transportation)
        noun_3 = add_preposition(noun_3)
        if int(number_2) > 1:
            noun_2 = make_plural_words(noun_2)
        story_1 = f'''It was about {number_1} {time_measure} ago when I arrived at the hospital in {mode_of_transportation}.
               The hospital is {adjective_1} place, there are a lot of {adjective_2} {noun_1} here. There are nurses here who have
               {color_1} {part_of_body_1}. If someone wants to come into my room I told them that they have to {verb_1} first.
               I’ve decorated my room with {number_2} {noun_2}. Today I talked to a doctor and they were wearing {noun_3} on their
               {part_of_body_1}. I heard that all doctors {verb_2} {noun_4} every day for breakfast. The most {adjective_3}
               thing about being in the hospital is the {silly_word} {noun_5}!'''

    elif template == 2:
        animal = add_preposition(animal)
        story_2 = f'''This weekend I am going camping with {person_name}.
               I packed my lantern, sleeping bag, and {noun_1}.
               I am so {feeling_1} to {verb_1} in a tent.
               I am {feeling_2} we might see {animal}, I hear they’re kind of dangerous.
               While we’re camping, we are going to hike, fish, and {verb_2}.
               I have heard that the {color_1} lake is great for {verb_ing}.
               Then we will {adverb_ly} hike through the forest for {number_1} {time_measure}.
               If I see a {color_2} {animal} while hiking, I am going to bring it home as a pet! At night we will tell {number_2}
               {silly_word} stories and roast {noun_1} around the campfire!!'''

    else:
        animal = add_preposition(animal)
        mag_creature_1 = make_plural_words(mag_creature_1)
        mag_creature_2 = make_plural_words(mag_creature_2)
        noun_3 = make_plural_words(noun_3)
        noun_4 = make_plural_words(noun_4)
        noun_2 = add_preposition(noun_2)
        story_3 = f''' Dear {person_name}, I am writing to you from {adjective_1} castle in an enchanted forest.
               I found myself here one day after going for a ride on a {color_1} {animal} in {place}.
               There are {adjective_2} {mag_creature_1} and {adjective_3} {mag_creature_2} here!
               In the {room} there is a pool full of {noun_1}.
               I fall asleep each night on {noun_2} of {noun_3} and dream of {adjective_4} {noun_4}.
               It feels as though I have lived here for {number_1} {time_measure}.
               I hope one day you can visit, although the only way to get here now is {verb_ing} on a {adjective_4} {noun_5}!!'''

    if template == 1:
        print(story_1)

    elif template == 2:
        print(story_2)

    else:
        print(story_3)
