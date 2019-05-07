import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('./accuracy_table.csv')
# print(data.head())
X = data.values[:, 0]

Y = data.values[:, 1]
X_pos = np.arange(len(X))
# ===================
# > REDUCE STRING <<<<
# ===================


def reduce_string(X):
    X = X[0:3] + "..." + X[-3:]
    return X


for i in range(len(X)):
    X[i] = reduce_string(X[i])
X = tuple(X)
#  ==================
#  REPLACE NAN VALUE
#  =================


def replace_nan(data):
    for i in range(len(data)):
        if np.isnan(data[i]):
            data[i] = 0
    return Y


temp = []
for i in range(1, 11):
    Y = data.values[:, i]
    Y = replace_nan(Y)
    temp.append(Y)


# /===========VISUALISATION=============

# plt.figure(figsize=(10, 20))

plt.subplot(2, 2, 1)
bars = plt.bar(X_pos, temp[0], align='center', color='g')
plt.xticks(X_pos, X, rotation=90)
# plt.xlabel("Learning algorithm", fontsize=15)

plt.ylabel('Accuracy %', fontsize=15)
plt.title('AP', fontsize=15)
plt.ylim(np.min(temp[0]), np.max(temp[0]) + 0.1)

plt.subplot(2, 2, 2)
bars = plt.bar(X_pos, temp[1], align='center', color='r')
plt.xticks(X_pos, X, rotation=90)
# plt.xlabel("Learning algorithm", fontsize=15)
# plt.ylabel('Accuracy %', fontsize=15)
plt.title('MagicTelescope', fontsize=15)
plt.ylim(np.min(temp[1]), np.max(temp[1]) + 0.1)

plt.subplot(2, 2, 3)
bars = plt.bar(X_pos, temp[2], align='center', color='k')
plt.xticks(X_pos, X, rotation=90)
# plt.xlabel("Learning algorithm", fontsize=15)
plt.ylabel('Accuracy %', fontsize=15)
plt.title('Abalone', fontsize=15)
plt.ylim(np.min(temp[2]), np.max(temp[2]) + 0.1)

plt.subplot(2, 2, 4)
bars = plt.bar(X_pos, temp[3], align='center')
plt.xticks(X_pos, X, rotation=90)
# plt.xlabel("Learning algorithm", fontsize=15)
# plt.ylabel('Accuracy %', fontsize=15)
plt.title('Anneal', fontsize=15)
plt.ylim(np.min(temp[3]), np.max(temp[3]) + 0.1)

plt.suptitle('Accuracy of attribute', fontsize=30)
plt.tight_layout() ## Tight layout often produces nice results
# x_label = ['AP','MagicTelescope','abalone','anneal','ar1','arrhythmia','audiology','autos','badges2','balance-scale']

# for i in range(8):
#     plt.subplot(5, 2, i + 1)
#     plt.bar(X_pos, temp[i], align='center', color='g')
#     plt.tick_params(bottom=False, top=False, labelbottom=False)
#     plt.xticks(X_pos, X, rotation=90)
#     plt.title(x_label[i], fontsize=15)
#     plt.ylim(np.min(temp[i]), np.max(temp[i]) + 0.1)

# for i in range(8,10):
#     plt.subplot(5, 2, i + 1)
#     plt.bar(X_pos, temp[i], align='center')
#     plt.title(x_label[i], fontsize=15)
#     plt.ylim(np.min(temp[i]), np.max(temp[i]) + 0.1)
#     plt.xticks(X_pos, X, rotation=90)
# plt.suptitle('Accuracy of attribute', fontsize=30)
# plt.tight_layout() ## Tight layout often produces nice results


plt.show()
