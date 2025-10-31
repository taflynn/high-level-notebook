import pandas as pd
import plotly.express as px
class summary:
    def __init__(self, core_perf_stats, intra_node_perf_stats, inter_node_perf_stats, gpu_perf_stats, io_perf_stats):

        self.core_perf_stats = core_perf_stats
        self.intra_node_perf_stats = intra_node_perf_stats
        self.inter_node_perf_stats = inter_node_perf_stats
        self.gpu_perf_stats = gpu_perf_stats
        self.io_perf_stats = io_perf_stats
    
    def summary_figure(self):
        '''Generates a radar figure of the five performance metrics'''
        
        data = pd.DataFrame(dict(
            proportions = [self.core_perf_stats.core_metric,
                           self.intra_node_perf_stats.intra_node_prop_60,
                           self.inter_node_perf_stats.inter_node_prop_60,
                           self.gpu_perf_stats.gpu_metric,
                           self.io_perf_stats.io_metric],
            rubrics = ['Core','Intra node','Inter node', 'GPU', 'I/O']
        ))
        
        fig = px.line_polar(data, 
                            r='proportions',
                            theta='rubrics',
                            line_close=True,
                            range_r = (0, 1),
                            width = 1000, height = 700)
        
        fig.update_traces(fill='toself')
        fig.show()