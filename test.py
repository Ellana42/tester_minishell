# TODO print expected output
# TODO launch with valgrind
# TODO check leaks output
# TODO print leaks output
import math
import os

import pandas as pd
from termcolor import colored

tests = pd.read_csv("tests.csv", index_col=0)
test_material = tests[["entry", "output"]]
print(test_material)

path_exec = "./minishell/srcs/parsing/a.out"


def test_valgrind(test):
    command = f'colour-valgrind {path_exec} "{entry}"'
    stream = os.popen(command)
    output = stream.read()
    if "no leaks are possible" in output:
        print(colored("NO LEAKS", "green"))
    else:
        print(colored("HAS LEAKS", "red"))


expected_output = ""
start = 86
for i, test in test_material.iterrows():
    if i >= start:
        print(50 * "-" + f" {i}")
        entry = test["entry"][3:].replace("$", "\\$").replace('"', '\\"')
        if type(test["output"]) == str:
            expected_output = test["output"]
        command = f'{path_exec} "{entry}"'
        # print(f"The command : {command}")
        stream = os.popen(command)
        output = stream.read()
        print(colored(20 * ">", "magenta"))
        print(colored(output, "magenta"))
        print(colored(20 * ">", "magenta"))
        print(colored(expected_output, "blue"))
        test_valgrind(test)
        input()
