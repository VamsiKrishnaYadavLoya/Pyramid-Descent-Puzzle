# Pyramid-Descent-Puzzle
Problem Statement: A Pyramid Descent Puzzle consists of a pyramid of positive integers. To solve the puzzle, you must find a path that traverses the pyramid from top to bottom visiting numbers whose product is a given target value. Each step in the path must go down one row, and go either one step to the left or one step to the right.

For example, suppose the pyramid below has a target value of 2.

1		
2		3	
4		1		1
A solver for this puzzle should output LR, indicating that the correct path starts from the 1 on top, goes Left to the 2 on the second row, then goes Right to the 1 in the center of the bottom row. (Note in particular that the successful path cannot go through the 1 at the end of the bottom row.) This gives the path shown in red below:

1		
2		3	
4		1		1
In your language of choice, write a solver that can solve any pyramid descent puzzle. Your solver can assume that every input pyramid has a first row with one number and every row thereafter has one more number than the row above. Each row is aligned such that the center of the row aligns with the midline of the pyramid (as shown in the samples above and below).

Below is a sample pyramid with target 720 along with the sample program input and output for this puzzle.

2				
4		3			
3		2		6		
2		9		5		2	
10		5		2		15		5
Input file: input.txt

# Pyramid Descent Puzzle Solver

This Python script solves the Pyramid Descent Puzzle by finding a path from the top of the pyramid to the bottom where the product of the numbers in the path equals a given target.

## Usage

1. Create an input file with the following format:
   - First line: target product.
   - Subsequent lines: rows of the pyramid, with numbers separated by commas.

Example (`input.txt`):


2. Run the script with your input file:

python pyramid_descent.py input.txt

Path: LRLL
