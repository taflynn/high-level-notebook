import matplotlib.pyplot as plt

class io_perf():
    def __init__(self, write_runtime_prop, read_runtime_prop):
        '''Raw I/O performance data'''

        self.write_runtime = write_runtime_prop
        self.read_runtime = read_runtime_prop
        
        self.io_prop = 1 - (self.write_runtime + self.read_runtime)

        self.io_metric = self.io_prop
    
    def io_perf_table(self):
        '''Generates a traffic-light table for the I/O performance metric'''
        data = [[''], [''], ['']]
        column_headings = [r'I/O metrics']
        row_headings = [r'$C_{\mathrm{I/O}} \geq 0.8$',
                        r'$0.6 \leq C_{\mathrm{I/O}} < 0.8$',
                        r'$C_{\mathrm{I/O}} < 0.6$']

        perf_str = [r'$C_{\mathrm{I/O}} \approx$' + f'{self.io_prop:.3f}']
        
        if self.io_prop >= 0.8:
            data[0] = perf_str
        elif self.io_prop < 0.8 and self.io_prop >= 0.6:
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