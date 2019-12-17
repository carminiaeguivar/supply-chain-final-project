import pandas as pd
from pyspc import *

response_time = pd.read_csv('./311_Service_Requests_Response_Time.csv')

values = response_time[['Response Time']].to_numpy()
print(values.ravel())
a = spc(values.ravel()) + xmr()
print(a)
