import pandas as pd

def read_data():
    df = pd.DataFrame({'first_name': ['sachin', 'rahul', 'saurav'],
                       'last_name': ['tendulkar', 'dravid', 'gangully']})
    return df

def pre_process(dframe, col_name):
    dframe[col_name] = dframe[col_name].apply(lambda val: str(val).capitalize())
    return dframe