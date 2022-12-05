# %%
import numpy as np
import pandas as pd

# %%
test_df = pd.read_csv("minishell_tests.csv")
print(test_df)

# %%
print()

# %%
test_df = test_df.drop(index=range(23)).drop(columns=test_df.columns[0])

# %%
test_df = test_df.rename(
    columns={
        "Unnamed: 1": "entry",
        "Unnamed: 2": "mandatory",
        "Unnamed: 3": "to_drop",
        "Unnamed: 4": "to_drop1",
        "Unnamed: 5": "to_drop2",
        "Unnamed: 6": "to_drop3",
        "Unnamed: 7": "output",
        "Unnamed: 8": "last_exit",
        "Unnamed: 9": "notes",
    }
)


# %%
test_df = test_df.drop(columns=["to_drop", "to_drop1", "to_drop2", "to_drop3"])

# %%
test_df["mandatory"] = (
    test_df["mandatory"].replace({"NON GERE": 0, np.nan: 1}).astype(int)
)

# %%
tests = test_df[test_df["mandatory"] == 1].drop(columns=["mandatory"])

# %%
tests

# %%
tests.to_csv("tests.csv")
