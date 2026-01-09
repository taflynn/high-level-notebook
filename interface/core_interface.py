from topics.core import core_perf

maximum_performance = float(input('Input maximum theoretical FLOPS'))
measured_performance = float(input('Input maximum measured FLOPS'))

core_performance_stats = core_perf(maximum_performance, measured_performance)

core_performance_stats.core_perf_table()