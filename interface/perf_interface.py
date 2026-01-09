from topics.core import core_perf
from topics.intra_node import intra_node_perf
from topics.inter_node import inter_node_perf
from topics.gpu import gpu_perf
from topics.io import io_perf
from topics.summary_lists import summary_perf

import pandas

performance_topics = {
    'labels': [],
    "values": []
}

core_prompt = input('Core analysis (Y/N)?')

if core_prompt == 'Y':
    maximum_performance = float(input('Input maximum theoretical FLOPS'))
    measured_performance = float(input('Input maximum measured FLOPS'))

    core_performance_stats = core_perf(maximum_performance, measured_performance)

    core_performance_stats.core_perf_table()
    
    performance_topics['labels'].append('Core')
    performance_topics['values'].append(core_performance_stats.core_metric)

intra_prompt = input('Intra-node analysis (Y/N)?')

if intra_prompt == 'Y':
    strong_scale_path = input('Input path to strong scaling csv file')

    df = pandas.read_csv(strong_scale_path, header=None)
    time = list(df[df.columns[1]])

    number_of_cores = list(df[df.columns[0]]) 

    if input('Is there an explicit serial time (Y/N)?') == 'Y':
        serial_time = float(input('Input serial time'))
    else:
        serial_time = time[0]

    intra_node_performance_stats= intra_node_perf(serial_time, number_of_cores, time)

    intra_node_performance_stats.parallel_efficiency_figure()
    intra_node_performance_stats.runtimes_figure()
    intra_node_performance_stats.intra_node_perf_table()
    
    performance_topics['labels'].append('Intra-node')
    performance_topics['values'].append(float(intra_node_performance_stats.intra_node_prop_60))

inter_prompt = input('Inter-node analysis (Y/N)?')

if inter_prompt == 'Y':
    weak_scale_path = input('Input path to weak scaling csv file')

    df = pandas.read_csv(weak_scale_path, header=None)
    inter_node_runtimes = list(df[df.columns[1]])

    node_count = list(df[df.columns[0]]) 

    if input('Is there an explicit serial time (Y/N)?') == 'Y':
        inter_node_serial_time = float(input('Input serial time'))
    else:
        inter_node_serial_time = inter_node_runtimes[0]

    inter_node_performance_stats = inter_node_perf(inter_node_serial_time, node_count, inter_node_runtimes)

    inter_node_performance_stats.parallel_efficiency_figure()
    inter_node_performance_stats.runtimes_figure()
    inter_node_performance_stats.inter_node_perf_table()    

    performance_topics['labels'].append('Inter-node')
    performance_topics['values'].append(float(inter_node_performance_stats.inter_node_prop_60))    

gpu_prompt = input('GPU analysis (Y/N)?')    

if gpu_prompt == 'Y':
    gpu_utilisation = float(input('Input GPU utilisation'))

    gpu_performance_stats = gpu_perf(gpu_utilisation)

    gpu_performance_stats.gpu_perf_table()

    performance_topics['labels'].append('GPU')
    performance_topics['values'].append(gpu_performance_stats.gpu_metric)

io_prompt = input('I/O analysis (Y/N)?')

if io_prompt == 'Y':
    read_proportion = float(input('Input proportion of runtime in reads:'))
    write_proportion =  float(input('Input proportion of runtime in writes:'))

    io_performance_stats = io_perf(write_proportion, read_proportion)

    io_performance_stats.io_perf_table()
    
    performance_topics['labels'].append('I/O')
    performance_topics['values'].append(io_performance_stats.io_metric)

print(performance_topics)

summary_performance_stats = summary_perf(performance_topics)

summary_performance_stats.summary_figure()

print("report complete!")