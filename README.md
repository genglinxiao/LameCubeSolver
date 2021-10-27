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
