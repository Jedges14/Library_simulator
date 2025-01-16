# Wizard Librarian
CMSC 150-[01/04] - Fall 2024 - Project 4

## Introduction
You are writing an automated librarian program for wizards. You have 101 books[^1] with their associated authors in your catalog. The wizards have asked that this librarian can sort and retrieve books on request using a "magic" menu. This project will use every Python concept you've learned so far in this class.

[^1]: Books and authors list (except for one) provided by ChatGPT

## Topics Covered
- file I/O
- search algorithms
- try / except
- sorting on multiple properties
- user input
- string manipulation
- event-driven user menus
- pseudocode implementation
- recursion
- generators
- (all previous topics)


## Instructions

The following subsections detail the requirements for this assignment. It's recommended to implement them in the order listed.

### Import/Export the Books

Import the book list from a specified file. You will need these for the Sort process (see "Sort the Books" below) and the Search process (see "Search the Books".)

Use a try-except statement to check if the book file exists. If not, default to importing the `wizard_books.txt` file and print a message. If that file doesn't exist, return an empty list and print another message.

Export the sorted books to a different file name in the same directory (see "Sort the Books" for more details.) Make sure it is in the EXACT same format as when it was read in.

### Create User Menu

Design a user menu that takes in commands to navigate to the submenus and process requests. Give the user the command options in square brackets ([]). If the user enters an incorrect command, repeat the prompt. If the user enters a keyword `back` return to the previous submenu.

Implement the following menu pseudocode for the program:
1. Ask the user what they would like to do (sort, search, exit).

2. If the user selects sort, ask how they would like the program to be sorted (title or author). If they type "back", GOTO 1.

    2.1. Upon completion of the sort, state the name of the file it was exported to, other information (see subsection Sort the Books) and GOTO 1

3. If the user selects search, ask how they are searching (title, author, or either). If they type "back", GOTO 1.
    
    3.1. Ask the user for the keyword(s) they want to search for. If they type "back", GOTO 3.
        
    3.2 Upon completion of the search, and after the information is shown, GOTO 3.1

4. If the user selects exit, exit the program with a goodbye message.


### Sort the Books

You will need to sort the books alphabetically in 2 ways: by *title* and by *author LAST NAME*. The books are listed in the file [wizard_books.txt](wizard_books.txt) first by title in double quotes (") then author name ([FIRST NAME] [LAST NAME]) separated by a dash "-". From the menu, export the title sorted version and author sorted version to 2 separate files named `wizard_books_TITLE.txt` and `wizard_books_AUTHOR.txt`respectively. The format should be the same as the original `wizard_books.txt` file.

### Search for Books

The user has 3 ways to search the books: title, author name, or either. Depending on the user selection, retrieve the book by first importing the following file:
    - "title" -> `wizard_books_TITLE.txt`
    - "author" -> `wizard_books_AUTHOR.txt`
    - "either" -> `wizard_books.txt`
Import the books based on the instructions in subsection "Import/Export the Books". 

Based on the response to the submenu (see 3 in subsection Create User Menu), search only based on the criteria specified by the user: title only, author only, or either. Print the book matches with one one each line. *If no matches are found, then print back a message stating so.*

Ignore capitalization of the keyword and allow partial matches (e.g. 'spell' as a search keyword should print books with 'Spell' and 'Spellbinder'). Include punctuation as well For example, "familiar's" should return a different book than "familiars" (see Example for more examples).


*The books printed must be in the same format as how they are saved in the catalog file regardless of the search criteria (see Example for example output).* For example, even if the search is for 'title', print both the title of the book and the author name.

## Starter Code
For this assignment, there is no starter code. The Python file [library-p4-TEMPLATE.py](library-p4-TEMPLATE.py) only has the header documentation, you will write the rest of the code. 

## Example Output
See [Library Output](library_output.txt) for an example interaction using the user menu for accessing the sort and search functionality. The different sections are annotated by hand using header comments, but the rest is from the program. The entire program output was run in one session with the 2 sorted files not yet existing.

Things to note:
- **[Lines 7-27]** Correct navigation as the user types their options and uses the `back` keyword. They can access any part of the submenu and return back to the original menu.
- **[Lines 51,188]** Invalid commands (e.g. 'idk', 'back' on the wrong menu) repeat the same menu option 
- **[Line 40]** After sorting, the program prints out where the file was saved.
- **[Lines 61,112]** If the search criteria uses 'author' and the author sorted file `wizard_books_AUTHOR.txt` was not found, it defaults to the original `wizard_books.txt`
- **[Lines 93-94]** Searches with no matches return a "NO MATCHES FOUND" message
- **[Lines 108-146]** Searches are limited only to the criteria set (i.e. 'author' only searches by the author's name even if the keyword matches the title.) Here, 'night' for 'author' criteria returns 4 results, 'night' for the 'title' criteria returns 1, and 'night' for the 'either' criteria returns 5 results.
- **[Lines 150-167]** Punctuation matters for the search criteria.
- **[Lines 164-174]** Capitalization is ignored during search and partial matches are allowed (e.g. 'wand' as a search for either returns books with 'Wands' and 'Wandwright')



## Rules
- Built-in Python libraries are allowed to be imported (e.g. math, time, sys, os) but they aren't necessary to succesfully complete the assignment. 
- External libraries -- such as those required to be installed using pip or other methods (e.g. numpy, scipy) -- are NOT allowed.
- You are allowed to use the built-in `sort` and `sorted` python functions. You may also implement your own sort function. However, no sort function from external libraries (numpy, scipy) are allowed.

- As per the syllabus, and for all assignments in this class, CODE FROM GENERATIVE AI IS PROHIBITED.  
- If you use a tutorial for implementing the parts of the code, such as but not limited to the sorting algorithm, cite your sources in the comments of the code.
- The code you turn in is your own. The code will be checked for plagiarism.

## Hints and Tips
- Turn the different subsections into their own functions with parameters for easy modularization and re-use
- For importing the specific book files, you can use recursion to default to the `wizard_books.txt` book if the sorted version files are not found.
- If you are getting a 'FileNotFound' error for even the default file `wizard_books.txt`, make sure you are calling your script in the same folder as the file (i.e. running the command `python library-p4-LASTNAME.py` and not something such as `python \some\directory\outside\library-p4-LASTNAME.py`). The code will look for the file locally.
- Break the pseudocode of the user menu up into nested conditionals and make use of local variables to keep track of where the user is in the menu.
- For the menu, test that prompt repeats itself for incorrect commands and that the user can exit the submenu.
- Make a Book class and turn the books imported from the file into Book instances for easier sorting, searching, and reformatting. Make use of getter methods and built in python methods such as `__str__()`
- Use `sorted(arr, key=lambda x:x.method_name_here())` for sorting by object property
- Remember to clean your text after importing from the file (remove new line characters, quotes, special characters, apostrophes, etc.)
- Stay consistent with your code and object formatting when passing them to functions for easier debugging.
- The first 5 lines of the sorted `wizard_books_TITLE.txt` should look like this:
    ```
    "Alchemy and Transmutation: The Advanced Guide" - Paracelsus Alchemist
    "Arcane Alchemy: Transmuting Elements" - Paracelsus Alchemist
    "Arcane Architecture: Building with Magic" - Archibald Spellbinder
    "Arcane Artifacts: A Collector's Guide" - Jasper Relic
    "Arcane Artillery: Wands and Staves" - Alaric Nightshade
    ```
- The first 5 lines of the sorted `wizard_books_AUTHOR.txt` should look like this:
    ```
    "Arcane Alchemy: Transmuting Elements" - Paracelsus Alchemist
    "Alchemy and Transmutation: The Advanced Guide" - Paracelsus Alchemist
    "Warlord's Compendium" - Kael Bloodthorn
    "The Warlock's War Manual" - Kael Bloodthorn
    "Witch's Brew: Potions for Every Occasion" - Hecate Brewster
    ```
    (Remember: it's sorted by *LAST NAME*)
- Remember the principle of Occam's razor.
- If you get stuck, don't be afraid to start over. But keep the old code for reference.

## Submission
Submit ONLY the Python file labeled `library-p4-[LASTNAME].py` (where [LASTNAME] is your last name) to Blackboard. *DO NOT submit the .txt files.* The project is **due at 12/2 11:59pm**. For each hour, `h`, that it is late, your grade is reduced by `h` points. 

*I'd recommend starting this project as early as possible. There is a lot more coding involved.*

## Rubric (100 pts)

#### General

* **[5 pts]** Correct file is turned in and is correctly named (see Submission above) with no additional files. 
* **[5 pts]** Code has header documentation -- name, date, class course name and section, and program description. 
* **[5 pts]** Program executes commands instantaneously (<1 second).

#### User Menu

* **[5 pts]** User menu navigation matches the pseudocode described.
* **[5 pts]** `back` keyword returns to previous submenu, `exit` exits the program
* **[5 pts]** Possible commands are listed for each submenu and invalid commands repeat the current submenu.

#### Sort

* **[10 pts]** Program correctly sorts `wizard_books.txt` by title on request and exports to `wizard_books_TITLE.txt`.
* **[10 pts]** Program correctly sorts `wizard_books.txt` by author last name on request and exports to `wizard_books_AUTHOR.txt`.
* **[10 pts]** Program catches a FileNotFound error if any of the 3 books are not found and continues the program. Defaults to using `wizard_books.txt` if the sorted version was requested.

#### Search

* **[10 pts]** Program searches only by title on request and returns accurate results for the input.
* **[10 pts]** Program searches only by author on request and returns accurate results for the input.
* **[10 pts]** Program searches by either title or author on request and returns accurate results for the input.
* **[10 pts]** Program returns a 'no matches' message if no matches are found for the search criteria.