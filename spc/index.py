import pandas as pd
from pyspc import *

response_time = pd.read_csv('./311_Service_Requests_Response_Time.csv')

values = response_time[['Response Time']].to_numpy()
one_d_array = values.ravel()
print('Dataset size: %d' % one_d_array.shape)
a = spc(one_d_array) + xmr() + rules()
print(a)
