import pandas as pd

df = pd.DataFrame(
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ],
    columns=list("ABCDEFGHIJKLM"),
)

df.index = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

first_case = pd.DataFrame(
    [[1, 1, 1, 1, 1, 1]], columns=list("ABCDEF"), index=["FirstCase"]
)

all_case = pd.concat([first_case, df])


def case_finder(df):
    df_case = df.apply(lambda x: x.value_counts(), axis=1).fillna(0)
    df_case = df_case.loc[df_case[1] != 0]
    return df_case.sort_values(by=1)


def check_together(x):
    x = df.iloc[x]
    activity = all_case.loc[x.name]
    does_activity = activity.loc[activity == 1]
    return activity.name, does_activity.index


def check_in(pre, now):
    return pre.isin(now).all()


def check_odd(i):
    act = check_together(i)[0]
    who = check_together(i)[1][~check_together(i)[1].isin(check_together(i - 1)[1])]
    return act, who


df = case_finder(all_case)
total = all_case.shape[0]


all_acts = []
last_stable = []
all_case_orj = all_case.copy()
while True:
    for i in range(total):
        act, ind = check_together(i)
        if i == 0:
            print("Initiliazed!")
            all_acts.append([act, ind])
            pass
        else:
            p_act, p_ind = check_together(i - 1)
            if check_in(p_ind, ind) == True:
                print("So a new person joins us!")
                all_acts.append([act, ind])
            else:
                print("This is weird. We'll check later!")
                # act, who = check_odd(i)
                last_stable.append([i, p_ind])
                continue
        if act == "FirstCase":
            break

    if len(last_stable) == 0:
        print("Process done!")
        break
    else:
        print("Update cases!")
        ls_ind = last_stable[0]
        all_case = all_case_orj.copy()
        all_case = all_case.drop(last_stable[0][1], axis=1)
        total = all_case.shape[0]
        df = case_finder(all_case)
        last_stable = last_stable[1:]

print(all_acts)

x = pd.DataFrame(all_acts)
