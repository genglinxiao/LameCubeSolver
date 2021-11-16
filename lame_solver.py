from queue import PriorityQueue
from cube import Cube
import random
import time
from solve import Solver
from optimize import optimize_moves
import cProfile

SOLVED_CUBE_STR = "OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR"
# MOVES = ["L", "R", "U", "D", "F", "B", "M", "E", "S"]
MOVES = ["L", "R", "U", "D", "F", "B", "Li", "Ri", "Ui", "Di", "Fi", "Bi"]


class LameSolver:
    def __init__(self, cube):
        self.cube = cube
        self.open_list = PriorityQueue()
        self.moves = []

        pass

    def search(self, goal_range, allowed_actions):
        self.open_list = PriorityQueue()
        self.moves = []
        self.open_list.put((0, (self.cube, self.moves, 0)))

        solved = False

        cube_tried = [self.cube]

        while not self.open_list.empty():
            (cube, action_taken, cost_so_far) = self.open_list.get()[1]

            # print(len(self.open_list))
            if cube.heuristic_score_by_layer(goal_range) == 0:
                solved = True
                self.moves = action_taken
                self.cube=cube
                break

            for act in allowed_actions:
                new_cube = Cube(cube)
                my_actions = action_taken.copy()
                my_actions.append(act)
                new_cube = new_cube.sequence(act)
                new_cost = cost_so_far + 1
                if new_cube not in cube_tried:
                    cube_tried.append(new_cube)
                    priority = new_cost + new_cube.heuristic_score_by_layer(goal_range) / 8
                    self.open_list.put((priority, (new_cube, my_actions, new_cost)))

        return solved

    def solve(self):
        if self.search(1, MOVES):
            print(self.moves)
            if self.search(2, MOVES):
                print(self.moves)
                if self.search(3, MOVES):
                    print(self.moves)


def random_cube():
    """
    :return: A new scrambled Cube
    """
    scramble_moves = " ".join(random.choices(MOVES, k=200))
    a = Cube(SOLVED_CUBE_STR)
    a.sequence(scramble_moves)
    return a


def run():
    successes = 0
    failures = 0

    avg_opt_moves = 0.0
    avg_moves = 0.0
    avg_time = 0.0
    while True:
        C = random_cube()
        solver = Solver(C)

        start = time.time()
        solver.solve()
        duration = time.time() - start

        if C.is_solved():
            opt_moves = optimize_moves(solver.moves)
            successes += 1
            avg_moves = (avg_moves * (successes - 1) + len(solver.moves)) / float(successes)
            avg_time = (avg_time * (successes - 1) + duration) / float(successes)
            avg_opt_moves = (avg_opt_moves * (successes - 1) + len(opt_moves)) / float(successes)
        else:
            failures += 1
            print(f"Failed ({successes + failures}): {C.flat_str()}")

        total = successes + failures
        if total == 1 or total % 100 == 0:
            pass_percentage = 100 * successes / total
            print(f"{total}: {successes} successes ({pass_percentage:0.3f}% passing)"
                  f" avg_moves={avg_moves:0.3f} avg_opt_moves={avg_opt_moves:0.3f}"
                  f" avg_time={avg_time:0.3f}s")


if __name__ == '__main__':
    DEBUG = True
    # run()

    # for i in range(1, 100):
    #     a = random_cube()
    #
    #     solver = Solver(a)
    #     solver.solve()
    #     print(len(solver.moves), solver.moves)
    #     pass

    # a=random_cube()
    # b=random_cube()
    # a<b

    a = Cube(SOLVED_CUBE_STR)
    a.sequence("F R B U R Bi U")
    # a = random_cube()
    solver = LameSolver(a)
    cProfile.run("solver.solve()")
    #solver.solve()
    # solver.solve()
    print(solver.moves)
