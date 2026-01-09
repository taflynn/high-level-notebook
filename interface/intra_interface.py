from topics.intra_node import intra_node_perf
import pandas

strong_scale_path = input('Input path to strong scaling csv file')

df = pandas.read_csv(strong_scale_path, header=None)
time = list(df[df.columns[1]])

number_of_cores = list(df[df.columns[0]]) 

serial_time_switch = input('Is there an explicit serial time (Y/N)?')

if serial_time_switch == 'Y':
    serial_time = input('Input serial time')
else:
    serial_time = time[0]

intra_node_performance_stats= intra_node_perf(serial_time, number_of_cores, time)

intra_node_performance_stats.parallel_efficiency_figure()
intra_node_performance_stats.runtimes_figure()
intra_node_performance_stats.intra_node_perf_table()