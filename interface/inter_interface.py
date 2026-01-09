from topics.inter_node import inter_node_perf
import pandas

weak_scale_path = input('Input path to weak scaling csv file')

df = pandas.read_csv(weak_scale_path, header=None)
inter_node_runtimes = list(df[df.columns[1]])

node_count = list(df[df.columns[0]]) 

serial_time_switch = input('Is there an explicit serial time (Y/N)?')

if serial_time_switch == 'Y':
    inter_node_serial_time = input('Input serial time')
else:
    inter_node_serial_time = inter_node_runtimes[0]

inter_node_performance_stats = inter_node_perf(inter_node_serial_time, node_count, inter_node_runtimes)

inter_node_performance_stats.parallel_efficiency_figure()
inter_node_performance_stats.runtimes_figure()
inter_node_performance_stats.inter_node_perf_table()