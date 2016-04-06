# Finding Ocurrences


## Preface
Do not use any extended functionality of the framework to solve this problem. (For example, if using C# don't use the string methods of IndexOf, substring, regular expression classes, LINQ etc). The test should take no longer than an hour for you to complete, please submit the working source code to solve the problem along with any supporting code that you might have used in testing.

## Problem:

We need a way of finding all the occurrences of a particular set of characters in a string. It should 
• Accept two strings as input. One called 'textToSearch' and one called 'subtext'
• The solution should match the subtext against the textToSearch, outputting the positions of the beginning of each match for the subtext within the textToSearch.
• Multiple matches are possible
• Matching is case insensitive
• If no matches have been found, no output is generated

## Sample Acceptance Criteria

### Text:
textToSearch = "Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!"

### Subtext and Expected Result
Peter	"1, 20, 75" 
peter	"1, 20, 75" 
pick	"30, 58" 
pi	"30, 37, 43, 51, 58" 
z	"No Output" 
Peterz	“No Output”



# Run
To run unit test suite, install 'nose', eg. using 'pip': 

    pip install -r ./requirements.txt
    
Run tests:

    nosetests -v


# Author
Jose Bermudez

[www.josebermudez.co.uk](http://www.josebermudez.co.uk)

[info@josebermudez.co.uk](mailto: info@josebermudez.co.uk)