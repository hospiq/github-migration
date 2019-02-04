#!/usr/bin/env python
# coding: utf-8
# In[1]:
import numpy as np
import pandas as pd
# In[2]:
df3 = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
df3.to_feather('data.pickle')
# In[ ]:
