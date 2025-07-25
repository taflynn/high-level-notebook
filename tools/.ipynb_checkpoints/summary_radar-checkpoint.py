import pandas as pd
import plotly.express as px
class summary:
    def __init__(self,core_perf,intra_node_perf):
        self.core_proportion = core_perf.core_proportion
        self.intraNode_proportion = intra_node_perf.intraNode_proportion
    def draw_radar(self):
        ''' Draw the Radar Diagram '''
        ### TEMPORARY PLACEHOLDER VARIABLES ###
        interNode_proportion = 0.7
        IO_proportion = 0.5
        GPU_porporion = 0.3
        
        # diagram variables
        width = 1000
        height = 700
        
        # define data to draw diagram
        data = pd.DataFrame(dict(
            proportions = [self.core_proportion, self.intraNode_proportion, interNode_proportion, IO_proportion, GPU_porporion],
            rubrics = ['Core','Intra node','Inter node',
                   'I/O', 'GPU']))
        
        # declare diagram
        fig = px.line_polar(data, r='proportions',
                            theta='rubrics',
                            line_close=True,
                            range_r = (0,1),
                            width = width, height = height)
        
        # draw diagram
        fig.update_traces(fill='toself')
        fig.show()