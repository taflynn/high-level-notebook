import matplotlib.pyplot as plt
class gpu_perf:
    def __init__(self, gpu_util):
        '''Raw GPU performance data'''
        
        self.gpu_util = gpu_util

        self.gpu_metric = self.gpu_util
   
    def gpu_perf_table(self):
        '''Generates a traffic-light table for the GPU performance metric'''
        
        data = [[''],[''],['']]
        column_headings = [r'GPU performance metric']
        row_headings = [r'$C_{\mathrm{util}} \geq 0.8$', 
                        r'0.8 > $C_{\mathrm{util}} \geq 0.6$', 
                        r'$0.6 > C_{\mathrm{util}}$']

        perf_str = [r'$C_{\mathrm{util}} \approx$' + f'{self.gpu_util:.3f}']
        
        if self.gpu_util >= 0.8:
            data[0] = perf_str
        elif self.gpu_util >= 0.6:
            data[1] = perf_str
        else:
            data[2] = perf_str
        
        fig, ax = plt.subplots()
        ax.set_axis_off()
        
        cell_colours = [['#0fa83480'], ['#ffc84480'], ['#e3555580']]

        plt.rcParams.update({'font.size': 18}) 

        table = plt.table(cellText = data,
                          rowLabels = row_headings,
                          colLabels = column_headings,
                          loc = 'center',
                          colLoc = 'center',
                          cellLoc = 'center',
                          rowLoc = 'center',
                          cellColours = cell_colours)

        table.scale(1.5,3)
        plt.show()