import csv
import pandas as pd

data =  pd.read_csv('Data.csv')

# print data.loc[[2]][190.0]
def calcCallsCach(CallSrike, CallsClose):
    CallStrike = row['Strike']
    CallsClosePrice = row[6]
    CloseDiff = CallsClosePrice - CallSrike
    CallsValue =  row['CallsOI'] * 100
    if CloseDiff < 0:
        CloseValue = 0
    else:
        CloseValue = CallsValue * CallsValue
    return CloseValue
    
    # print ("data.loc['Strike']=",data.loc[[CallSrike]], " CallsClose=",data.loc[[CallSrike]][str(CallsClose)] )


# ######################## Main ########################
if __name__ == '__main__':

    StrikeList = list( data['Strike'] )
    # for row in data.itertuples():
    for row in data.iterrows():
        print (row)
        raw_input("Press Enter to continue...")



# if ColumnStrike - CallsOIofColumnStrike < 0 then Return ( 0 * CallOI * 100) Else Return


# strikeList = data['Strike']

# print strikeList.head()
#
# for strike in strikeList:
#     print
