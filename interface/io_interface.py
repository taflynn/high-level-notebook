from topics.io import io_perf

read_proportion = float(input('Input proportion of runtime in reads:'))

write_proportion =  float(input('Input proportion of runtime in writes:'))

io_performance_stats = io_perf(write_proportion, read_proportion)

io_performance_stats.io_perf_table()