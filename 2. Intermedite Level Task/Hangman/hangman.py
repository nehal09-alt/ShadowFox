import random 

words = ["ShadowFox" , "China" ,"AI", "Modi" , "People" , "Internship", 'Anthem', 'India' ,'Asia' , 'Europe', 'America', 'Apple',
          'Orange' , 'Lion' , 'tiger' , 'youtube' , 'Google' , 'Meta', 'Display' , 'Zebra', 'Game' , 'University']

hangman_structure = [
    '''     
    ''',
    '''          O      
    ''',
    '''          O 
          | 
    ''',
    '''          O
         /|
    ''',
    '''           O
          /|\\
    ''',
    '''           O
          /|\\
          /
    ''',
    '''           O
          /|\\
          / \\
    ''',    
]
def hangmman ():
    word = random.choice(words).upper()
    word_length = len(word)
    display = ['_']*word_length
    guessed =set()
    lives = 6 

    print("\nWelcome to Hangman Game ... ")
    print(" ".join(display))
    print(f"lives : {lives}")
    

    while lives > 0 and  '_' in display :
        guess = input("\nGuess a letter : ").upper().strip()


        if len(guess) != 1 or not guess.isalpha():
            print("Enter a Single letter!  ")
            continue 
        if guess in guessed :
            print("Already Guessed that Letter!")
            continue 

        guessed.add(guess)

        if guess in word :
            for i in range(word_length):
                if word[i]==guess:
                    display[i]=guess
            print(" ".join(display))
        else :
            lives -=1
            print(f"Wrong! Lives left: {lives}") 
        print(hangman_structure[6-lives])
    if '_' not in display :
        print("\n You Win ! the word was : " , word )
    else:
        print("\n Game Over! The word was : ", word )

while True :
    hangmman()
    replay = input("\n Play again (y/n) : ").lower()
    if replay != 'y':
        print("Thank for playing!")
        break