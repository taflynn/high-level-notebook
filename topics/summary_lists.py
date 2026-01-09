import pandas as pd
import plotly.express as px
class summary_perf:
    def __init__(self, perf_metrics):

        self.perf_metrics = perf_metrics
    
    def summary_figure(self):
        '''Generates a radar figure of the five performance metrics'''
        
        data = pd.DataFrame(dict(
            proportions = self.perf_metrics["values"],
            rubrics = self.perf_metrics["labels"]
        ))
        
        fig = px.line_polar(data, 
                            r='proportions',
                            theta='rubrics',
                            line_close=True,
                            range_r = (0, 1),
                            width = 1000, height = 700)
        
        fig.update_traces(fill='toself')
        fig.show()