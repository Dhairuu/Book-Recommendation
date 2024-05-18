import pandas as pd
import numpy as np

input_user_data =[]
Cosine_Matrix = []
user_data = []
data = pd.read_csv('Unique_Columns.csv')
# 824
num_columns = 824
Survey = pd.read_csv("Unique_Columns.csv", usecols=range(4,num_columns))

User_datasheet = pd.read_csv('My_Survey.csv')


User = int(input('Enter the index of User:'))
# ---------------------------------------------------------------------------------------------------------------
Empty_Data_Sheet = pd.read_csv('User_data.csv')     #,usecols=range(0,201)
User_values = []
for genre in User_datasheet:
    User_values.append([genre,User_datasheet.loc[User,genre]])
User_values = dict(User_values)
column_names =[]
for col in Empty_Data_Sheet:
    column_names.append(col)
new_row = pd.Series(0,index=column_names)
for index,col in enumerate(column_names):
    if col in User_values.keys():
        new_row.iloc[index] = User_values[str(col)]
Empty_Data_Sheet = pd.concat([Empty_Data_Sheet, new_row.to_frame().T], ignore_index=True)
# print(Empty_Data_Sheet)
# ---------------------------------------------------------------------------------------------------------------
for key in Empty_Data_Sheet:
    if key == 'Name':
        # print(Empty_Data_Sheet.iloc[0][key])
        continue
    input_user_data.append(Empty_Data_Sheet.iloc[0][key])

# print(input_user_data)
print("Input User: ",Empty_Data_Sheet.iloc[0]['Name'])
vector_a = np.array(input_user_data)
norm_a = np.linalg.norm(vector_a)

for index1,key in enumerate(Survey):
    if index1 == (len(Survey)):
        break
    # print(index1)
    for keya in Survey: 
        # if key == 'Book':
        #     continue
        # if key == 'Author':
        #     continue
        # if key == 'Genres':
        #     continue
        user_data.append(Survey.iloc[index1][keya])
    # print(user_data)
    vector_b = np.array(user_data)
    norm_b = np.linalg.norm(vector_b)
    dotproduct = np.dot(vector_a,vector_b)

    Cosine_Similarity = dotproduct/(norm_a * norm_b)
    Cosine_Matrix.append([index1,Cosine_Similarity])
    user_data.clear()

Cosine_Matrix.sort(key=lambda x: x[1],reverse=True)

# print("Cosine_Matrix: ",Cosine_Matrix)
count = 0
print('Our Suggestions:')
for value in Cosine_Matrix:
    if count == 5:
        break
    if value[0] != User:
        count = count+1
        # print(value[0])
        print(data.iloc[value[0]]['Book'])

