# LameCubeSolver
A Cube Solver that cannot see the shortest path in most cases.

## Inspiration
Humans, enven the speedcubers, solve the Rubik's cube in ways that are different from optimal solutions found by computer algorithms. One key difference is, humans split the task of solving the cube by stages/milestones, most naturally by layers that been restored/solved. In contrast, for computer algorithms, all the states of the cube are equal, except the initial state and the goal state.
We would argue that, it is this ability to decomposing an ultimate goal into mail stones that enables human brain, with limited working memory and speed, to solve something as complex as the Rubik's cube.
Now, we would like to simulate this process with an algorithm and generalize the approach.
## Goals
1. Given well known mailstones in a Rubik's cube, finding the path between any initial state to the next mailstone, till the cube is solved.
2. Identify action combinations that achieve the goal from one mailstone to the next, together with the cost(steps of primitive actions) and side effects(other pieces get moved).
3. Finding optimal solutions of a cube using the action combinations identified by 2.
4. Come up with different definition of mailstones.


## Useful Links
https://github.com/benbotto/rubiks-cube-cracker - C++ Optimal Cube Solver using Korf algorithm, basically IDA* with a heuristic function that employes a pattern database.

https://github.com/abau171/cubetree - Korf in python.

https://github.com/pglass/cube - Cuber Solver that follows the standard cube manual.

https://github.com/geof90/rubiks - A web based simulator.

https://github.com/hkociemba/CubeExplorer - CubeExplorer, has basically all the things we wanted, except the layer by layer part. We will use this as our simulator.

## Ideas
1. How to define stages in a hierachical planning in general.

Humans intuitively define the mile stones towards a goal.
In the case of Rubik's Cube, it can be measured as how well-scrambled the cube is.
In this sense, the entropy is a good measure here. Though some configuraiton looks very well-ordered, for example only 2 edged pieces were swaps, may needs as many as 16 steps to solve. But human approach rarely end up with the shortest path anyway.

2. The Entrop of a Rubik's cube.
The most straight-forward way of defining the cube's entropy would be to go through each of the 54 stickers. If it is in place, that is a 1/6 probability; If it is not, that is a 5/6 probability. The entropy would be:

Sum54( p * log(p) )

However, that is a poor definition because the distribution of colors is actually not unified. After all, corner pieces will always be corner cases, edge pieces will always be edge pieces, center pieces will not move (in our setup). So, 8 corner pieces, each can be in each 3 orientations, that's 24 possibilities. 12 edges, each can be orientated in 2 ways, that's 24 possibilities. So the entropy of a given cube is:
Sum8( p1 * log(p1) ) + Sum12( p2 * log(p2) )
p1 is the possibility of a corner piece, if it's in the right place and right orientation, then that's 1/24. Otherwise, that's 23/24.
p2 is the possibility of a edge piece, if it's is in the right place and right orientation, then that's 1/24. Otherwise, that's 23/24.

3. How to solve between stages.

In theory, we can always rely on a search. However, given a branching factor of 11, and we know that evern some simple deviation from a goal state may needs more than 10 steps, simple search is not the optimal solution.
A better approach is, to have a pattern database so that once a pattern is spotted, we know the manuver needed - This is basically Korf algorith.
An ideal solution could be, to use matrix decomposition. Any scramble of a cube can be described by a matrix equation. 

(x1, y1, z1)                                              (x1', y1', z1') 

(x2, y2, z2)             (     )                          (x2', y2', z2')

(x3, y3, z3)             (     )            =             (x3', y3', z3')

...                      (     )                          ...

(x20, y20, z20)                                           (x20', y20', z20')


Each row is represents a cubie (12 edges and 8 corners).
The matrix is the product of multiple rotation matrix correspondent to the primitive actions.
Now the task is to decomposing the matrix into a series of primitive rotation matrics.
! Not sure that's possible though.

## Interesting findings
1. Any combination of actions, repeatedly applied to a cube, will bring the cube back to its original configuration.

R'LUUDDFB'R'U"L'F' - 336 =2^4 × 3 × 7

F'U'B'UUDFBBL'F'D' - 630, with 90 as a minor period. 630 = 2 x 3^2 x 5 x 7

U'R' - 105 = 3 x 5 x 7

RUF - 80 = 2^4 x 5

RUFR' - 105 = 3 x 5 x 7

L'DFDR'U'D'FUD'FDLDDR'LLD'BBD - 66 = 2 x 3 x 11

FFUFD - 40 = 2^3 x 5

FFUFL - 420 = 2^2 x 3 x 5 x 7

RDBFUL - 36 = 2^2 x 3^3

RDBFU - 36 = 2^2 x 3^3

RDBFFU - 90 = 2 x 3^2 x 5

UFDBRB'RD'F'U'B'R'BR' - 2 = 2 这个动作组合将两个edge互换，而且是互换两个edge的最优解。

RDFUDB - 84 = 2^2 x 3 x 7
UURBULU'FUUF'L'U'B'UR' - 2 = 2 这个动作将两对Eduge互换
RFRU'R'D'LDRUBUUD'L'D'LBU'L - 66 = 2 x 3 x 11
RB'R'FB'RRU'R'U'D'R'LDR'DF'LD'L' - 336 = 2^4 x 3 x 7
R' D' L U R D L' U' L' D L R D L B' B' F' L U R U' - 24 = 2^3 x 3
F L R D' R F' U R D R' D B' L' R' B' L' B L' F U R U' - 48 = 2^4 x 3
