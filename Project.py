import plotly.figure_factory as ff
import plotly.graph_objects as go 
import pandas as pd 
import csv 
import statistics
df = pd.read_csv('prodata.csv')
height = df['reading score'].to_list()
mean = statistics.mean(height)
median = statistics.median(height)
mode = statistics.mode(height)
st_div = statistics.stdev(height)
fstd_start,fstd_stop = mean - st_div, mean + st_div
sstd_start,sstd_stop = mean - 2*(st_div), mean + 2*(st_div)
tstd_start,tstd_stop = mean - 3*(st_div), mean + 3*(st_div)
Height1 = [result for result in height if result>fstd_start and result<fstd_stop]
Height2 = [result for result in height if result>sstd_start and result<sstd_stop]
Height3 = [result for result in height if result>tstd_start and result<tstd_stop]
print(len(Height1)*100.0/len(height))
print(len(Height2)*100.0/len(height))
print(len(Height3)*100.0/len(height))
graph = ff.create_distplot([height],['height'],show_hist=False)
graph.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='Mean'))
graph.add_trace(go.Scatter(x=[fstd_start,fstd_start],y=[0,0.17],mode='lines',name='First standard deviation'))
graph.add_trace(go.Scatter(x=[fstd_stop,fstd_stop],y=[0,0.17],mode='lines',name='First standard deviation'))
graph.add_trace(go.Scatter(x=[sstd_start,sstd_start],y=[0,0.17],mode='lines',name='Second standard deviation'))
graph.add_trace(go.Scatter(x=[sstd_stop,sstd_stop],y=[0,0.17],mode='lines',name='Second standard deviation'))
graph.add_trace(go.Scatter(x=[tstd_start,tstd_start],y=[0,0.17],mode='lines',name='Third standard deviation'))
graph.add_trace(go.Scatter(x=[tstd_stop,tstd_stop],y=[0,0.17],mode='lines',name='Third standard deviation'))
graph.show()