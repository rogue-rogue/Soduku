<h1> Little soduku game </h1>

Tried this game before, trying it again now. 

<h2> Project phases </h2> 
1. Finalize python interactive shell version with seed boards already prepared
2. Prepare user friendly front end. A brief google suggests that I will need to use a framework to link python and CSS as they are not naturally compatible (in the ammer than CSS and HTML are). 
3. Write algorithm to generate boards at a set difficulty. This will need a fair bit of focus on algorithms. Make sure I include an input for user difficulty (aka how many numbers are left on the board). 

<h2> Board Setup </h2> 
- 3x3 grid of subgrids. Subgrids are 3x3 cells. 
- Each row, column and subgrid contains numbers 1-9 (inclusive). 
- There are usually 4 levels: Beginner – Intermediate – Advanced – Expert. Colloquially, the fewest numbers you can start with is 17, so that's expert territory. 

<h2> Gameplay </h2> 
1. Generate a complete soduku puzzle which complies with layout rules. 
2. Select a level. 
3. Prepare a playable copy by removing the amount of numbers dictated by the level. The remaining numbers are the seed numbers and cannot be modified by the user. 
5. Take a turn
6. Optional: Check is your turn was correct
7. Repeat 3 (and possibly 4) until grid is full 
8. Game is won or lost 

A turn consists of either: 
1. Removing a user placed number from row/column location 
2. Adding a user placed number to an empty cell 
3. 1 and 2

<h2> Notes on generator algo </h2> 
I read some stuff here about creating the generator alogrithm: https://www.101computing.net/sudoku-generator-algorithm/ 
"create an algorithm to be used by a puzzle setter to produce a well-posed Sudoku grid: a grid with a unique solution. "
Ill come back to this later
