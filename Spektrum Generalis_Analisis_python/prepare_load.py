import pandas as pd

# create function to read dataset
def readDataset(path):
    import re
    if re.findall('csv', path):
        df = pd.read_csv(path)
        return df
    elif re.findall(path, 'xlsx'):
        df = pd.read_excel(path)
        return df
    else:
        print('Directory or file not found, or maybe you need manually read using engine openpyxl')
        return None

# create function to show dataframe information
def fastDescribe(df):
    print("##################### Shape ###################")
    print(df.shape)
    print(" ")
    print("##################### Types ###################")
    print(df.dtypes)
    print(" ")
    print("##################### Head ####################")
    print(df.head(3))
    print(" ")
    print("##################### Tail ####################")
    print(df.tail(3))
    print(" ")
    print("##################### NA #####################")
    print(df.isnull().sum())
    print(" ")
    print("##################### Describe ################")
    print(df.describe())

# create function to print unique value of each column
def distincValue(df):
    list_col = df.columns.tolist()
    for item in list_col:
        un_ = df[item].unique().tolist()
        len_un = len(un_)
        round_pros = round(len_un/len(df), 5)*100
        print("****** ", item, " ******")
        print("Number of distinc: ", len_un)
        print("Percentage of distinc: ", round_pros,"%")
        print(" ")