# #1

# import pandas as pd
# file = 'NISPUF17.csv'
# df = pd.read_csv(file, sep=',')
# print(df)
# children_count=df
# df['EDUC1']= df['EDUC1'].replace([1,2,3,4],['<12','12','>12','CG'], regex= True)
# print(df['EDUC1'].unique())

# #count_less_12_a= int(df['EDUC1'].where(df['EDUC1']=='<12').count())
# #print(count_less_12_a)

# data_1 = df.groupby('EDUC1')['EDUC1'].count()
# # d = {data_1.index[0]: float(data_1[0])/children_count,
# #      data_1.index[1]: float(data_1[1])/children_count,
# #      data_1.index[2]: float(data_1[2])/children_count,
# #      data_1.index[3]: float(data_1[3])/children_count,
# #     }
# print(data_1)

# #2

# import pandas as pd
# file = 'NISPUF17.csv'
# def  average_influenza_doses(file):
#     df = pd.read_csv('file', sep=',')
#     df = df.dropna(subset='P_NUMFLU')
#     df['CBF_01'] = df ['CBF_01'].replace([1,2], ['yes','no'] )
# df = pd.read_csv(file, sep=',')



#3

import pandas as pd
file = 'NISPUF17.csv'

def chickenpox_by_sex(file):
    df = pd.read_csv(file, sep=',')
    print(df['HAD_CPOX'].unique())
chickenpox_by_sex(file)