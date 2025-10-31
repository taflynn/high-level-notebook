import matplotlib.pyplot as plt
class core_perf:
    def __init__(self, max_perf, obs_perf):
        '''Raw core performance data'''
        self.max_perf = max_perf
        self.obs_perf = obs_perf
        
        self.perf_prop = self.obs_perf/self.max_perf
        self.core_metric = self.perf_prop

    def core_perf_table(self):
        '''Generates a traffic-light table for the core performance metric'''
        data = [[''],[''],['']]
        row_headings = [r'$C_{\mathrm{peak}} \geq 0.8$', 
                        r'0.8 > $C_{\mathrm{peak}} \geq 0.6$', 
                        r'$0.6 > C_{\mathrm{peak}}$']
        column_headings = [r'Core performance metric']

        perf_str = [r'$C_{\mathrm{peak}} =$' + f'{self.perf_prop:.3f}']
        
        if self.perf_prop >= 0.8:
            data[0] = perf_str
        elif self.perf_prop >= 0.6:
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