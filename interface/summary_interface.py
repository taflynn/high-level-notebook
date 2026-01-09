from topics.summary import summary_perf

summary_performance_stats = summary_perf(core_performance_stats,
                                    intra_node_performance_stats,
                                    inter_node_performance_stats,
                                    gpu_performance_stats,
                                    io_performance_stats)