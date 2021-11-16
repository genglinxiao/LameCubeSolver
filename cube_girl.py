import cube
import sqlite3

from itertools import chain, combinations


con = sqlite3.connect('cube_experience.db')

SOLVED_CUBE_STR = "OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR"
MOVES = ["L", "R", "U", "D", "F", "B", "Li", "Ri", "Ui", "Di", "Fi", "Bi"]

a = cube.Cube(SOLVED_CUBE_STR)

'''
Given each maneuver, we have a consequence, and a unaffected area.
Given each maneuver, there are symmetrical maneuvers:
 - mirror symmetry, left to right, or back to front, or up to down, turns change from Clock-wise to counter clock-wise. In total 8 symmetries.
 - rotation symmetry. rotation by the x axis, by the y axis, and by the z axis. In total 24 symmetries
The symmetries can be combined, which results in 24x8 = 192 symmetries.

'''
mirror_symmetries = ["LR", "BF", "UD"]
rotation_axis = ["x", "y", "z"]
rotation_step = [0, 1, 2, 3, 4, 5, 6, 7]

x_face_queue = ['U', 'F', 'D', 'B']
y_face_queue = ['F', 'R', 'B', 'L']
z_face_queue = ['U', 'L', 'D', 'R']


def mirror_symmetry(seq, sym):
    action_list = seq.split()
    ta = []
    if sym == 'LR':
        for action in action_list:
            alt = ""
            if action[0] == "L":
                alt = "R"
            elif action[0] == "R":
                alt = "L"
            else:
                alt = action[0]
            if len(action) == 1:
                alt += "i"
            ta.append(alt)
    if sym == 'BF':
        for action in action_list:
            alt = ""
            if action[0] == "B":
                alt = "F"
            elif action[0] == "F":
                alt = "B"
            else:
                alt = action[0]
            if len(action) == 1:
                alt += "i"
            ta.append(alt)

    if sym == 'UD':
        for action in action_list:
            alt = ""
            if action[0] == "U":
                alt = "D"
            elif action[0] == "D":
                alt = "U"
            else:
                act = action[0]
            if len(action) == 1:
                alt += "i"

            ta.append(alt)

    return " ".join(ta)


def rotation_symmetry(seq, sym):
    axis = sym[0]
    step = int(sym[1])
    if step>3:
        step=-step
    alt = []
    for action in seq.split():
        if axis == 'x':
            if action[0] in x_face_queue:
                alt_a = action.replace(action[0], x_face_queue[(x_face_queue.index(action[0]) + step) % 4])
            else:
                alt_a = action
        if axis == 'y':
            if action[0] in y_face_queue:
                alt_a = action.replace(action[0], y_face_queue[(y_face_queue.index(action[0]) + step) % 4])
            else:
                alt_a = action
        if axis == 'z':
            if action[0] in z_face_queue:
                alt_a = action.replace(action[0], z_face_queue[(z_face_queue.index(action[0]) + step) % 4])
            else:
                alt_a = action
        alt.append(alt_a)
    return " ".join(alt)



def powerset(iterable):
    "list(powerset([1,2,3])) --> [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

if __name__ == '__main__':
    print(mirror_symmetry("Li U L", 'LR'))
    print(rotation_symmetry("R Ui Ri", 'y1'))
    print(rotation_symmetry("R Ui Ri", 'y2'))
    print(rotation_symmetry("R Ui Ri", 'y3'))




