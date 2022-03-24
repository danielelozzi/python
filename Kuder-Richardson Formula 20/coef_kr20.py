def coef_kr20(df, columns):
    #KR-20 = (k / (k-1)) * (1 – Σpjqj / σ2)
    #where:

    #k: Total number of questions
    #pj: Proportion of individuals who answered question j correctly
    #qj: Proportion of individuals who answered question j incorrectly
    #σ2: Variance of scores for all individuals who took the test
    #The value for KR-20 ranges from 0 to 1, with higher values indicating higher reliability.
    
    import numpy as np
    import pandas as pd
    
    df = df[columns]
    df = df.dropna()
    n = df.shape[0]
    k = len(columns)
    pq=0
    tot = []
    for j in range(k):
        pj = df[columns[j]].loc[(df[columns[j]]==1)].count()/n
        qj = df[columns[j]].loc[(df[columns[j]]==0)].count()/n
        pq+=(pj*qj)

    for j in range(n):
        tot_j = df.iloc[j,:].sum()
        tot.append(tot_j)
    var = np.array(tot).var(ddof=1) # sample variance with DF = 1
    kr20 = (k/(k-1))*(1-(pq/var))
    
    return kr20
