import pandas as pd
import plotly.express as px
class summary:
    def __init__(self, core_perf, intra_node_perf):
        ''' Placeholder for now '''
    def draw_radar(self):
        ''' Draw the Radar Diagram '''
        ### TEMPORARY PLACEHOLDER VARIABLES ###
        core_proportion = 0.82
        intraNode_proportion = 0.9
        interNode_proportion = 0.7
        IO_proportion = 0.5
        GPU_porporion = 0.3
        
        # diagram variables
        width = 1000
        height = 700
        
        # define data to draw diagram
        data = pd.DataFrame(dict(
            proportions = [core_proportion, intraNode_proportion, interNode_proportion, IO_proportion, GPU_porporion],
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