import matplotlib.pyplot as plt
class gpu_perf:
    def __init__(self, gpu_utilisation, measured_memory, peak_memory):
        ''' Calculate statistics about Core Performance '''
        
        self.gpu_utilisation = gpu_utilisation
        self.measured_memory = measured_memory
        self.peak_memory = peak_memory
        
        self.memory_usage = self.measured_memory/self.peak_memory
   
    def gpu_perf_table(self):
        ''' Draw a table indicating flaws in code '''
        
        data = [['','',''],['','',''],['','','']]
        column_headings = [r'$C_{\mathrm{mem}} \geq 0.8$',r'0.8 > $C_{\mathrm{mem}} \geq 0.6$',r'$0.6 > C_{\mathrm{mem}}$']
        row_headings = [r'$C_{\mathrm{util}} \geq 0.8$',r'0.8 > $C_{\mathrm{util}} \geq 0.6$',r'$0.6 > C_{\mathrm{util}}$']
        
        fig, ax = plt.subplots()
        ax.set_axis_off()
        
        cell_colours = [['#0fa83480','#0fa83480','#ffc84480'],
                        ['#0fa83480','#ffc84480','#ffc84480'],
                        ['#e3555580','#e3555580','#e3555580']]
        
        # find cell for statistics
        A,B = (self.gpu_utilisation >= 0.8),(self.gpu_utilisation >= 0.6)
        C,D = (self.memory_usage >= 0.8),(self.memory_usage >= 0.6)
        option = (A and C)*0 + (A and D and not(C))*1 + (A and not(D))*2 + (C and not(A) and B)*3 + (not(A or C) and B and D)*4
        option += (not(A or D) and B)*5 + (C and not(B))*6 + (not(B or C) and D)*7 + (not(B or D))*8
        data[option // 3][option % 3] = r'$C_{\mathrm{mem}} \approx$' + f'{self.memory_usage:.3f}' + r', $C_{\mathrm{util}} \approx$' + f'{self.gpu_utilisation:.3f}'
        
        plt.rcParams.update({'font.size': 18}) 

        table = plt.table(cellText = data,
                          rowLabels = row_headings,
                          colLabels = column_headings,
                          loc = 'center',
                          colLoc = 'center',
                          cellLoc = 'center',
                          rowLoc = 'center',
                          cellColours = cell_colours)
        '''
        for cell in table.get_celld().values():
            cell.set_edgecolor('none')
        '''

        table.scale(1.5,3)
        plt.show()