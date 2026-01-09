from topics.gpu import gpu_perf

gpu_utilisation = float(input('Input GPU utilisation'))

gpu_performance_stats = gpu_perf(gpu_utilisation)

gpu_performance_stats.gpu_perf_table()