<a></a>

# **Hangman**

<img src="docs/screens.png">

Hangman is an old school favorite, a word game where the goal is simply to find the missing word.

You will be presented with a number of blank spaces representing the missing letters you need to find.

Use the keyboard to guess a letter (I recommend starting with vowels).

If your chosen letter exists in the answer, then all places in the answer where that letter appear will be revealed.

After you've revealed several letters, you may be able to guess what the answer is and fill in the remaining letters.

Be warned, every time you guess a letter wrong you lose a life and the hangman begins to appear, piece by piece. There are 6 body parts to apprear before you run out of chances.

Solve the puzzle before the hangman dies.

It has 2 python files, run.py and word.py. 

run.py has the all the functionality code for the game and word.py has a list of words, from which a random word is chosen by computer.

**GitHub repository** can be found by clicking <a href="https://github.com/kazcare/hangman" target="_blank" rel="noopener">**here**.</a> and the deployed **live link** for the website can be found by clicking <a href="https://han-man.herokuapp.com/" target="_blank" rel="noopener">**here**.</a>    

<a></a>

## Table of contents 
* [Hangman](#hangman)
    * [Flow Chart](#flow-chart)
    * [User Experience](#user-experience)
        * [Project Goals](#project-goals)
        * [User Stories](#user-stories)
        * [Colored Text](#colored-text)
        * [Main Features](#main-features)
            * [Technology Used](#technology-used)
            * [Languages](#languages)
    * [Testing](#testing)
        * [Validation Testing](#validation-testing)
        * [Bugs](#bugs)
            * [Bugs Fixed](#bug-fixed)
    * [Coding Environment](#coding-environment)
    * [Deployment](#deployment)
    * [Credits](#credits)

<a></a>

## Flow Chart

<img src="docs/flowchart.png">

Planning of this project was based on the flow charts using the platform Lucid Charts.

[Back to Top](#table-of-contents)
<a></a>

## User experience
### Project Goals

- It should give user an option to retry after every game
- It should clearly shows user's progress throwout the game with different images and number of attempts left.
- It should validate the user entry, it should only be a single alphabetic character.


[Back to Top](#table-of-contents)
<a></a>

### User Stories

- As a player, I want the game to ask user's name before start of the game.
- As a player, I want the game to show me instructions at the start of the game.
- As a player, I want the game to show me progress in the game by showing hangman images.
- As a player, I want the game to show my progress by letting me know the number of attempts remaining.
- As a player, after every game, I want app to give me option to either replay or end the game.
- As a player, I want the game to give me warning if I accidently enter an invalid character and should not count it as an attempt to guess the word.

[Back to Top](#table-of-contents)
<a></a>

### Coloured Text

I used a simple colour scheme to improve the overall user experience and make it easy to understand color-coded messages.
- The colour red ("\033[0;31m) was used for wrong guesses.
- The colour yellow ("\033[0;33m) was used for invalid entries.
- The colour green ("\033[0;32m) was used for correct guesses.
- The colour blue ("\033[0;34m) was used for input lines.

[Back to Top](#table-of-contents)
<a></a>

### Main Feature

- **Title/ Welcome message**
    - It contains title with welcome message

<img src="docs/title.png">

- **Username**
    - In the start of the game it asks user to enter a name so user can be greeted by user's chosen name. Name has to be entered in alphabetic notation

<img src="docs/username.png">

- **Instructions**
    - After validating the name, game displays the instructions to play the game.

<img src="docs/instructions.png">

- **Start of the game**
    - Game loads under the instructions
    - Asks user to input any letter to guess the word
    - It is colour coded in blue

<img src="docs/start.png">

- **Invalid Guess**
    - It warns user if a non-alphabetic character is keyed in
    - It is colour coded in yellow

<img src="docs/invalid.png">

- **Wrong Guess**
    - It lets user know that the guessed letter is not in the word
    - Hangman image shows the next stage and number of attempts remaining underneath it
    - It is displayed in red colour

<img src="docs/wrong.png">

- **Correct guess**
    - Informs user that the guessed letter is in the word
    - It shows the letter on it's position in the word
    - this message shows in green colour

<img src="docs/correct.png">

- **Win**
    - When the whole word is guessed by the user, it congratulates the user on guessing the word
    - It is green colour coded

<img src="docs/win.png">

- **Lose**
    - If user is not successful guessing the word after 6 wrong attempts, the game is over
    - It tells user that it was not a successful attempt
    - User get a message with the correct word
    - User get message in red colour

<img src="docs/lose.png">

- **Play again**
    - At the end of every game it asks user to play again
    - If user press y new game starts with a different word
    - If user press n game ends
    - It displays in blue

<img src="docs/again.png">

- **Thank user**
    - At the end if user decides not to play anymore, game thanks user for playing the game

<img src="docs/thank.png">


[Back to Top](#table-of-contents)
<a></a>

#### **Technology Used**

- GitPod was used for writing code, committing, and then pushing to GitHub.
- Github was used to store the project after pushing.
- Lucid Charts was used to create and design the flow chart used in the logical design of this project.
- PEP8 online check was used to validate the python code.
- Heroku was used to deploy the application.

#### **Languages**

- Python

[Back to Top](#table-of-contents)
<a></a>

## Testing

#### **Username Validation**
    - Username is checked if only the alphabets are entered. Numbers and other symbols are not allowed in the username field.
    
<img src="docs/username-validation.png">    

#### **Data Validation**
    - Guessed letter is checked to verify if it is alphabetic character.
    - None other characters are allowed.

<img src="docs/invalid1.png">
<img src="docs/invalid2.png">

#### **Entry Validation**
    - informs user if same letter is being guessed in the previous attempts.

<img src="docs/re-entry.png">

#### **Empty Field Validation**
    - It informs user if nothing is entered by error.
    - It does not cost user any attempts.

<img src="docs/empty.png">

#### **Progress Validation**
    - Every incorrect guess decreases the number of attempts remaining
    - It is shown with the next stage of Hangman image
<img src="docs/progress.png">

#### **Replay Validation**
    - It gives user an option to start the game again with newly selected word
<img src="docs/again.png">

#### **Thank user validation**
    - It thanks user after user decides to leave the game by not replaying it.
<img src="docs/thank.png">

[Back to Top](#table-of-contents)
<a></a>

### **Validation Testing**

#### **Initial Validation Testing**

<img src="docs/initial.png">

#### **Final Validation Testing**

<img src="docs/final.png">

[Back to Top](#table-of-contents)
<a></a>

### Bugs
#### Bugs Fixed

1- Game was only showing the image to let user know the progress, which could be hard for some user to understand how many attempts were remaing. 
- Added a message with number of attempts remaining.

2- When game ask user to replay, if user presses 'Y' to replay it would start game again but if user picks 'N' for not to replay, it didn't do anything. It was confusing. 
- Now a message appears thanking user to taking time to play the game.

3- Single quotes are used for print commands.
- Had to use double quote for the following command, as "didn't" wouldn't work with single quotes.
- print(f"{RED_COLOR}The word was {word}. You didn't win it this time.")

[Back to Top](#table-of-contents)
<a></a>

## Coding Environment

I used Gitpod IDE to code my project. 

* Following procedures are to be followed to get to the Gitpod IDE.

    1. Firstly you need to login to your GitHub account.

    2. Create a new repository by clicking green "New" button on the right hand side.

    3. Once the repository is created, click the repository to open it.

    4. Once it is opened, click the green "Gitpod" button on the top right hand side to create a Gitpod workspace. It takes some time to create it.
        
* Note: Once the Gitpod workspace is created for certain repository, do not click the green Gitpod button again, as it will create another workspace for the same repository. Everytime after the Gitpod workspace is created, access it by clicking <a href="https://gitpod.io/workspaces" target="_blank" rel="noopener">gitpod.io/workspaces</a>.

    5. In the Gitpod IDE there are three main sections: 
        - On the left hand side there is an explorer that shows the list of the files and folders in the project. 
        - The right hand side is divided into two portions vertically. 
        - Bigger portion on the top is for write codes and the bottom is to write commands for the Gitpod IDE.

    6. Every change made to the any file and folder in the project has to be sent to GitHub, otherwise the deployed project will not show those changes.

    7. To send the changes to GitHub following three steps to be followed:
        - First, changes are to be added by giving command 'git add filename' or use 'git add .' for adding all the changes to more than one item in the project. 
        - Once these changes are added, a commit command to be entered by giving command 'git commit -m "message regarding changes made since last commit" '. 
        - After the commit command 'git push' command is to be entered to push all the chages to the deployed project.

[Back to Top](#table-of-contents)
<a></a>

## Deployment

This application has been deployed using Heroku by following these steps:

Heroku was used to deploy the application.

- Before the application deployed, you must commit changes and push them to GitHub.
- Go to the <a href="https://www.heroku.com" target="_blank" rel="noopener">Heroku's website</a>.
- Create an account or select log in if you have an account already.
- From the Heroku dashboard, click on "Create new app".
- Enter the "App name" and "Choose a region" before clicking on "Create app".
- Go to "Config Vars" under the "Settings" tab.
- Click on "Reveals Config Vars" and add the KEY: CREDS and the VALUE stored in creds.json file if needed.
- Add the Config Var, KEY: PORT and VALUE: 8000.
- Go to "Buildpacks" section and click "Add buildpack".
- Select "python" and click "Save changes"
- Add "nodejs" buildpack as well using the same process.
- Go to "Deployment method", under the "Deploy" tab select "GitHub" and click on "Connect to GitHub".
- Go to "Connect to GitHub" section and "Search" the repository to be deployed.
- Click "Connect" next the repository name.
- Choose "Automatic deploys" or "Manual deploys" to deploy your application.

    
[Back to Top](#table-of-contents)
<a></a>

## Credits

- I would like to inform you all that this project (Hangman) is built for educational purpose only. I have rendered the following items and information from different resources. I would like to thank all of these resources for helping me completing my project.
- Idea and main coding skeleton was inspired by <a href="https://www.youtube.com/watch?v=m4nEnsavl6w" target="_blank" rel="noopener"> Kite </a>Developement Community Youtube video.
- <a href="https://www.w3schools.com//" target="_blank" rel="noopener">W3Schools</a> was used as a resource for solving syntax errors.
- I referenced <a href="https://ozzmaker.com/add-colour-to-text-in-python/" target="_blank" rel="noopener">ozzmaker.com</a> and <a href="https://stackabuse.com/how-to-print-colored-text-in-python/" target="_blank" rel="noopener">stackabuse.com</a> for using coloured text.
- Copied some text from the <a href="https://thewordsearch.com/" target="_blank" rel="noopener">thewordsearch.com</a> to use in the README.md.

[Back to Top](#table-of-contents)
