# Spiral
Consider the natural numbers laid out in a square spiral, with 1 occupying the center of the spiral. The central 11 x 11 subset of that spiral is shown in the table below.

111	112	113	114	115	116	117	118	119	120	121
110	73	74	75	76	77	78	79	80	81	82
109	72	43	44	45	46	47	48	49	50	83
108	71	42	21	22	23	24	25	26	51	84
107	70	41	20	 7	 8	 9	10	27	52	85
106	69	40	19	 6	 1	 2	11	28	53	86
105	68	39	18	 5	 4	 3	12	29	54	87
104	67	38	17	16	15	14	13	30	55	88
103	66	37	36	35	34	33	32	31	56	89
102	65	64	63	62	61	60	59	58	57	90
101	100	99	98	97	96	95	94	93	92	91
This spiral has several interesting features. The southeast diagonal has several prime numbers (3, 13, 31, 57, and 91) along it. The southwest diagonal has a weaker concentration of prime numbers (5, 17, 37) along it.

To construct the spiral we start with 1 at the center, with 2 to the right, and 3 below it, 4 to the left, and so on. A part of the problem for this assignment is to figure out the rule to fill the spiral for an arbirary size. Once you have that rule you can complete the rest of the assignment.

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
