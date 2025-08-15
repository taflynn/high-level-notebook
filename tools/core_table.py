import matplotlib.pyplot as plt
class core_perf:
    def __init__(self, peak_perf_single_core,measured_average_perf,target_bw_per_core,measured_avg_bw_requirements):
        ''' Calculate statistics about Core Performance '''
        self.peak_perf_single_core = peak_perf_single_core
        self.measured_average_perf = measured_average_perf
        self.target_bw_per_core = target_bw_per_core
        self.measured_avg_bw_requirements = measured_avg_bw_requirements
        self.bw_proportion = measured_avg_bw_requirements / target_bw_per_core
        self.performance_proportion = measured_average_perf / peak_perf_single_core
        self.core_proportion = min(self.bw_proportion, self.performance_proportion)

    def core_perf_table(self):
        ''' Draw a table indicating flaws in code '''
        data = [['','',''],['','',''],['','','']]
        column_headings = [r'$C_{\mathrm{bw}} \geq 0.8$',r'0.8 > $C_{\mathrm{bw}} \geq 0.6$',r'$0.6 > C_{\mathrm{bw}}$']
        row_headings = [r'$C_{\mathrm{peak}} \geq 0.8$',r'0.8 > $C_{\mathrm{peak}} \geq 0.6$',r'$0.6 > C_{\mathrm{peak}}$']
        
        fig, ax = plt.subplots()
        ax.set_axis_off()
        
        cell_colours = [['#0fa83480','#0fa83480','#ffc84480'],
                        ['#0fa83480','#ffc84480','#ffc84480'],
                        ['#e3555580','#e3555580','#e3555580']]
        
        # find cell for statistics
        A,B = (self.performance_proportion >= 0.8),(self.performance_proportion >= 0.6)
        C,D = (self.bw_proportion >= 0.8),(self.bw_proportion >= 0.6)
        option = (A and C)*0 + (A and D and not(C))*1 + (A and not(D))*2 + (C and not(A) and B)*3 + (not(A or C) and B and D)*4
        option += (not(A or D) and B)*5 + (C and not(B))*6 + (not(B or C) and D)*7 + (not(B or D))*8
        data[option // 3][option % 3] = r'$C_{\mathrm{bw}} =$' + f'{self.bw_proportion:.2f}' + r', $C_{\mathrm{peak}} =$' + f'{self.performance_proportion:.2f}'
        
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