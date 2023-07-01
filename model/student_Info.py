from bs4 import BeautifulSoup
import requests
import tqdm
import pandas as pd
import numpy as np

def student_info(path):
    # エクセルをデータフレームで読み込む
    df = pd.read_excel(path,dtype='str')

    # Nan列・行削除
    df.dropna(how='all', axis=1, inplace=True)
    df.dropna(how='all', axis=0, inplace=True)

    past_group_col = df.loc[:,'class01':].columns.tolist()
    
    # 0埋め二次元配列定義
    num_same_group = np.zeros((len(df),len(df)))
    np.set_printoptions(threshold=10000)
    
    # 同じグループになった回数を算出
    for past_group in past_group_col:
        for i in range(len(df)):
            for j in range(len(df)):
                if df[past_group][i] == df[past_group][j]:
                    num_same_group[i][j] += 1
    
    participate_status = np.zeros(len(df), dtype=bool)
    
    for i in range(len(df)):
        
        if df['next_ participation'][i] == 'participate':
            participate_status[i] = True
    
    return (num_same_group, participate_status)