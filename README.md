# LameCubeSolver
A Cube Solver that cannot see the shortest path in most cases.

## Inspiration
Humans, enven the speedcubers, solve the Rubik's cube in ways that are different from optimal solutions found by computer algorithms. One key difference is, humans split the task of solving the cube by stages, most naturally by layers that been restored/solved. In contrast, for computer algorithms, all the states of the cube are equal, except the initial state and the goal state.
We would argue that, it is this ability to decomposing an ultimate goal into mail stones that enables human brain, with limited working memory and speed, to solve something as complex as the Rubik's cube.
Now, we would like to simulate this process with an algorithm and generalize the approach.
## Goals
1. Given well known mailstones in a Rubik's cube, finding the path between any initial state to the next mailstone, till the cube is solved.
2. Identify action combinations that achieve the goal from one mailstone to the next, together with the cost(steps of primitive actions) and side effects(other pieces get moved).
3. Finding optimal solutions of a cube using the action combinations identified by 2.
4. Come up with different definition of mailstones.
