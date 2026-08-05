# Human Benchmark Bot
Completes the typing, reaction, and aim tests for the human benchmark.

## Setup
Download the zip file and run the code in an IDE like VSC

Install required libraries in the terminal

```bash
pip install -r requirements.txt
```

On lines 36-37 you may need to change the variables depending on your monitor size
Use the "testing" case in Instructions to make sure the screenshot actually captures the window and the mouse stays on the browser.

## Instructions
When running the program you can type a string which corresponds to the test you are running

testing -> takes a screenshot saved to screenshot.png and moves mouse for testing if your variables are setup properly

typing -> opens a new window and performs the typing test

reaction -> type anything into the terminal to begin detecting

aim -> will begin looking at the screen to find targets and click them
