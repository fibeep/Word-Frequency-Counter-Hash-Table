# Word Frequency Counter
------------------
# Description:
> For this project, I made a word frequency counter.
> A user inputs the name of the text file into the terminal and 
> the program parses through the file and returns how many times 
> each word appears throughout the text.

By using a hashtable with chaining, we store each word as node containing (word, count) in a linked list.
The count value is updated every time the same word is encountered. Whenever a new word appears, the hash function
determines it's place in the array of linked lists and places it accordingly.

### Technical Details:
**Written Python**
**Makes use of hash table chaining**