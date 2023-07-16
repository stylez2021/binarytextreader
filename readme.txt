Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample.
You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random,
the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering
the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized
more exotic forms that the ore can become, but you haven't seen all of them.

Write a function solution(m) that takes an array of array of
nonnegative ints representing how many times that state has gone to the next state and return an array of ints for "each terminal state" giving the exact
probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form.
The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state.
That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during
the calculation, as long as the fraction is simplified regularly.

Trying to follow along:
[0, 2, 1, 0, 0],  #s0   goes to s1 or s2, but with higher probabiliy for s1
[0, 0, 0, 3, 4],  #s1   can become s3 or s4 but higher prob for s4
[0, 0, 0, 0, 0],  #s2   is terminal
[0, 0, 0, 0, 0],  #s3   is terminal
[0, 0, 0, 0, 0]   #s4   is terminal

Pap tries math:
s0 -> s1 
s0 has probabiliy 0
s1 2 goes there?
s2 1 goes there?
s3 3 goes there?
s4 4 goes there?

# ok so it looks like we're only returning arrays that are terminal (re "each terminal state") ok that explains the 0 in the breakdown example.
# Output:    [7, 6, 8, 21]


For example, consider the matrix m:
[
[0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
[4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
[0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
[0,0,0,0,0,0],  # s3 is terminal
[0,0,0,0,0,0],  # s4 is terminal
[0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].