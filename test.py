# l TODO launch subprocess with argument
# TODO get output
# TODO print output
# TODO print expected output
# TODO launch with valgrind
# TODO check leaks output
# TODO print leaks output
import os

import pandas as pd
from termcolor import colored

tests = pd.read_csv("tests.csv", index_col=0).drop(index=[23, 24, 25])
test_material = tests[["entry", "output"]]
print(test_material)

path_exec = "./minishell/srcs/parsing/a.out"

for i, test in test_material.iterrows():
    print(test["entry"])
    entry = test["entry"][3:]
    # expected_output = test["output"][3:]
    print(colored(entry, "blue"))
    stream = os.popen(f"{path_exec} {entry}")
    output = stream.read()
    print(colored(output, "green"))
    # print(colored(expected_output, "blue"))
    break
