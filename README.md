# Capitals Quiz 
Capitals Quiz is a Python terminal quiz, which runs in the Code Institute mock terminal on Heroku. 

[Here is the live version of the project](https://johns-capitals-quiz-91df1cc5b9af.herokuapp.com/)

![Website displayed on multiple screens](assets/imagesforreadme/screenshots.PNG)

## How to play 
Users are asked what the capital is of 10 countries and are given a selection of 3 potential answers, listed as A, B and C. One of the answers shall be the capital and therefore the correct answer while the other two options shall be incorrect answers. The other two options however are both cities in that particular country. 

Features: 

Instructions on how to paly the game 
![Instructions](assets/imagesforreadme/instructions.PNG)

The question is asked 

![The question](assets/imagesforreadme/question.PNG)

If the player selects the correct option, the player is notified of this, is given a score of 1 for that question and then the next question is generated. 

![Correct answer](assets/imagesforreadme/correctanswer.PNG)

-   If the player selects the incorrect option, the player is notified of this, is advised that the score remains as it previously was and the next question is generated. 

![Incorrect answer](assets/imagesforreadme/incorrectanswer.PNG)

-   If the player selects anything other than a/A, b/B or c/C, the player is notified that what they have selected is not an option and is asked to select A, B or C again until they select a/A, b/B or c/C. 

![Not selected a/A, b/B nor c/C](assets/imagesforreadme/notanoption.PNG)

-   Simiarly, if the player doesn't select anything and just presses Enter, the player is notified that what they have selected is not an option and is asked to select A, B or C again until they select a/A, b/B or c/C. 

![Only pressed Enter](assets/imagesforreadme/alsonotanoption.PNG)

At the end of the quiz
-   The player is given their final score out of 10

![At the end of the quiz](assets/imagesforreadme/endofquiz.PNG)

## Testing 
I have manually tested this project by doing the following: 
-   Passed the code through a PEP8 linter and confirmed there are no problems
-   Given invalid inputs (including selecting nothing and just pressing return) 
-   Tested in my local terminal and the Code Institute Heroku terminal 

<table of testing> 

## Bugs 
-   No bugs 

## Validator 
-   PEP8 
    -   No errors were returned from PEP8online.com

## Deployment 
This project was deployed using Code Institute’s mock terminal for Heroku
-   Steps for deployment: 
    -   Fork or clone this repository 
    -   Create a new Heroku app
	-   Set the build backs to Python and Node JS in that order
    -	Link the Heroku app to the repository
    -   Click on Deploy

## Credits 
-   Code Institute for the deployment terminal 
## Thanks to
-   Mentor: Matthew Bodden 
