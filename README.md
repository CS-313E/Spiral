# Spiral
You will prompt the user for the following information:

Enter dimension: 11
Enter number in spiral: 42
The first line indicates the dimension of the square spiral. This number should be an odd number. If it is not then choose the dimension to be the next higher odd number. The second number must be in the range 1 and the square of the dimension. If the second number is not in that range, print an error message Number not in Range and exit the program.
You will write the sub-grid surrounding the second number. The sub-grid is a 2-D list of size (2 x 2), (2, 3), (3, 2) or (3, 3). When you print the 2-D list each row must be on a line by itself and there must be a single white space separating each number. You do not have align the numbers.

All outputs shown are for the 11 x 11 grid. If the second number was 42, then this should be your output:

72 43 44
71 42 21
70 41 20

If the second number was 64, then this should be your output:
66 37 36
65 64 63
100 99 98

If the second number was 94, then this should be your output:
60 59 58
95 94 93

If the second number was 104, then this should be your output:
105 68
104 67
103 66

If the second number was 121, then this should be your output:
120 121
81 82
