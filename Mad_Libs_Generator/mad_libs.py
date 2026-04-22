import random
def madlibs():
    
    print("Welcome to the Terminal Mad Libs Generator!")
    print("Here you can provide words along with your own story or the termninal will generate a story for you!")
    print("Please provide the following words to build your story:\n")
    
    adjective1 = input("Enter an adjective: ")
    tech_buzzword = input("Enter a tech buzzword (e.g., neural network, blockchain): ")
    plural_noun = input("Enter a plural noun: ")
    verb_infinitive = input("Enter a verb (infinitive, e.g., to run, to hack): ")
    anime_character = input("Enter an anime character's name: ")
    emotion = input("Enter an emotion: ")
    
        
        
        
    story = (
            f"In a highly {adjective1} near-future, society relies entirely on a massive {tech_buzzword} "
            f"to manage the city's {plural_noun}. The system operated flawlessly until {anime_character} "
            f"decided {verb_infinitive} the central mainframe. The lead developers were filled with {emotion} "
            f"as the terminal output turned completely red!"
        )
    story_1 = (
        f"At the biggest pop-culture convention of the year, {anime_character} was chosen to unveil the "
        f"highly anticipated {adjective1} {tech_buzzword}. However, the crowd of cosplayers dropped "
        f"their {plural_noun} in shock when {anime_character} decided {verb_infinitive} on stage instead "
        f"of giving the presentation, leaving the organizers overwhelmed with {emotion}."
    )
    story_2 = (
        f"The laboratory was completely silent except for the humming of the new {tech_buzzword}. "
        f"It was originally designed to sort {plural_noun}, but it somehow became incredibly {adjective1} "
        f"overnight. Driven by pure {emotion}, {anime_character} had to break into the facility "
        f"{verb_infinitive} before the machine took over the internet."
    )
    story_3 = (
        f"The investors stared blankly as {anime_character} pitched the most {adjective1} idea of the "
        f"decade: a {tech_buzzword} designed exclusively for tracking {plural_noun}. The ultimate goal "
        f"was {verb_infinitive} the entire industry overnight. The boardroom was filled with {emotion} "
        f"when the live prototype actually worked."
    )
    story_4 = (
        f"While trapped inside a glitching virtual reality server, {anime_character} discovered a hidden "
        f"{tech_buzzword} that continuously spawned giant, {adjective1} {plural_noun}. The only way to "
        f"escape the simulation was {verb_infinitive} through the firewall. When they finally logged out, "
        f"they collapsed in a puddle of {emotion}."
    )
    story_5 = (
        f"Ancient legends say that whoever possesses the {adjective1} {tech_buzzword} will rule over "
        f"all the {plural_noun} in the land. {anime_character} embarked on a dangerous journey "
        f"{verb_infinitive} the ancient artifact, facing numerous trials along the way. Upon finally "
        f"touching it, a massive surge of {emotion} washed over them."
    )
        
      

    stories = [story,story_1, story_2, story_3, story_4, story_5]
    final_story = random.choice(stories)  
        
    print("\n" + "="*60)
    print(" YOUR GENERATED STORY ")
    print("="*60)
    print(final_story)
    print("="*60 + "\n")
    
    
    
    


if __name__ == "__main__":
    madlibs()