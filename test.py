import os

import pandas as pd
from termcolor import colored


def test_valgrind(entry):
    command = f'colour-valgrind {path_exec} "{entry}"'
    stream = os.popen(command)
    output = stream.read()
    if "no leaks are possible" in output:
        print(colored("NO LEAKS", "green"))
    else:
        print(colored("HAS LEAKS", "red"))


def full_test(test_material, start=0):
    expected_output = ""
    for i, test in test_material.iterrows():
        if i >= start:
            print(50 * "-" + f" {i}")
            entry = test["entry"][3:].replace("$", "\\$").replace('"', '\\"')
            print(colored(entry, "blue"))
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
            test_valgrind(entry)
            input()


def list_issues(test_material, start=0):
    pb_index = []
    for i, test in test_material.iterrows():
        if i >= start:
            entry = test["entry"][3:].replace("$", "\\$").replace('"', '\\"')
            if type(test["output"]) == str:
                expected_output = test["output"]
                command = f'colour-valgrind {path_exec} "{entry}"'
                stream = os.popen(command)
                output = stream.read()
                if not "no leaks are possible" in output:
                    pb_index.append(i)
    return pb_index


if __name__ == "__main__":
    tests = pd.read_csv("tests.csv", index_col=0)
    test_material = tests[["entry", "output"]]
    # print(test_material)

    path_exec = "./minishell/srcs/a.out"
    full_test(test_material, start=0)
    # issues = list_issues(test_material)
    # print(issues)
    # print(len(issues))
