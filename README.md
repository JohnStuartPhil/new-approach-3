# Capitals Quiz 
Capitals Quiz is a Python terminal quiz, which runs in the Code Institute mock terminal on Heroku.

It is a multiple choice game where the user has to decide between a choice of cities in a particular given country, which one the capital is. 

[Here is the live version of the project](https://johns-capitals-quiz-91df1cc5b9af.herokuapp.com/)

![Website displayed on multiple screens](assets/imagesforreadme/screenshots.PNG)

## How to play 
The player is asked what the capital is of a total of 10 countries across the course of the game and are given a selection of 3 potential cities in that country. The 3 cities listed as A, B and C. One of the answers shall be the capital and therefore the correct answer while the other two options shall be incorrect answers. When the player answers correctly, they are awarded 1 point for each correct answer thus being able to obtain a maximum of 10 points. 

Features: 

Instructions on how to paly the game.

![Instructions](assets/imagesforreadme/instructions.PNG)

The question is asked.

![The question](assets/imagesforreadme/question.PNG)

If the player selects the correct option, the player is notified of this, is given a score of 1 for that question and then the next question is generated. 

There is a 2 second pause, the previous question dissapears then the next question appears on the screen.

![Correct answer](assets/imagesforreadme/correctanswer.PNG)

If the player selects the incorrect option, the player is notified of this, is advised that the score remains as it previously was and the next question is generated. 

![Incorrect answer](assets/imagesforreadme/incorrectanswer.PNG)

If the player selects anything other than A, B or C, the player is notified that what they have selected is not an option and is asked to select A, B or C again until they select A, B or C. The choice of A, B or C can be selected in either upper case or lower case.

![Not selected a/A, b/B nor c/C](assets/imagesforreadme/notanoption.PNG)

Similarly, if the player doesn't select anything and just presses Enter, the player is notified that what they have selected is not an option and is asked to select A, B or C again until they select A, B or C. 

![Only pressed Enter](assets/imagesforreadme/alsonotanoption.PNG)

At the end of the quiz, the player is given their final score out of 10

![At the end of the quiz](assets/imagesforreadme/endofquiz.PNG)

If the player plays again, the three cities are not necessarily listed in the same order each time. 

Below is an example where the correct answer is listed as A:

![Example where the correct answer is listed as A](assets/imagesforreadme/random1.PNG)

Below is an example where the correct answer is listed as C:

![Example where the correct answer is listed as A](assets/imagesforreadme/random2.PNG)

## Testing 
The project has been manually tested by doing the following: 
-   Passed the code through a PEP8 linter and confirmed there are no problems
-   Given invalid inputs (including selecting nothing and just pressing return) 
-   Tested in the local terminal and the Code Institute Heroku terminal 

Tests carried out:

| Test  | Section  | Action  | Result  | Pass/Fail  |
|---|---|---|---|---|
| 1  |  Question | Entered the correct option in lower case  | Advised that the correct option was entered and gave one point  | Pass  |
| 2  |  Question | Entered one of the incorrect options in lower case | Advised that the correct option was not entered and advised that the points remained as they were before  | Pass  |
| 3  |  Question | Entered the other incorrect option in lower case | Advised that the correct option was not entered and advised that the points remained as they were before  |  Pass |
| 4  |  Question | Entered the correct option in upper case  | Advised that the correct option was entered and gave one point  | Pass  |
| 5  |  Question | Entered one of the incorrect options in upper case | Advised that the correct option was not entered and advised that the points remained as they were before  | Pass  |
| 6  |  Question | Entered the other incorrect option in upper case | Advised that the correct option was not entered and advised that the points remained as they were before  |  Pass |
|  7 |  Question  | Entered a character other than a/A, b/B or c/C   | Advised that what was entered was not a valid option and was prompted to enter A, B or C  |  Pass |
| 8  |  Question  | Entered multiple charachetrs including aa, bb, cc  | Advised that what was entered was not a valid option and was prompted to enter A, B or C  | Pass  |
| 9  |  Question  | Pressed Enter without entering any characters  | Advised that what was entered was not a valid option and was prompted to enter A, B or C  | Pass  |
| 10 | Question   | Repeated entering an invalid input multiple times  | Contnued to advise that what was entered was not a valid option and was prompted to enter A, B or C   |  Pass |

## Bugs 
When testing in PEP8, multiple lines of code brought up the error 'line too long (xx > 79 characters)'.

Most of these lines going over column 80 contained a string of text.

These lines were shortend to below column 80 by using two methods:

The first method was to split the original print statement into two print() lines and adjoin them using the ', end=" "' method. 

This is what the code looked like before the error was fixed:

![Code before error fixed](assets/imagesforreadme/before1.PNG)

This is what the code looked like after the error has been fixed:

![Code after error fixed using =end" " method](assets/imagesforreadme/after1.PNG)


The second method was to create a variable and allocate the text to it then create a second line of code with the print() statement featuring an f-string and insert the variable into that.

This is what the code looked like before the error was fixed:

![More code before error fixed](assets/imagesforreadme/before2.PNG)

This is what the code looked like after the error has been fixed:

![Code after error fixed using variable and f-string method](assets/imagesforreadme/after2.PNG)

## Validator 
-   PEP8 
    -   No errors were returned from PEP8online.com

![Screenshot of passing PEP8](assets/imagesforreadme/noerrorspep.PNG)

## Deployment 
This project was deployed using Code Institute’s mock terminal for Heroku
-   Steps for deployment: 
    -   Fork or clone this repository 
    -   Create a new Heroku app
    -   Add Config Var with the key of PORT and the value of 8000
	-   Set the build backs to Python and Node JS in that order
    -	Link the Heroku app to the repository
    -   Click on Deploy

## Credits 
-   Code Institute for the deployment terminal 
-   Patrick Rich for the video 'Beautiful Terminal Styling in Python With Rich' which was used to help with the colors and styling
-   The aforementioned Patrick Rich video can be found on [YouTube](https://www.youtube.com/watch?v=4zbehnz-8QU)
-   Code to clear the terminal from [Slack](https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python)

## Thanks to
-   Mentor: Matthew Bodden 
