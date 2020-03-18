import covid_healthsystems as covidhs

version = 'v1'
date     = '2020mar16'
folder   = f'results_{date}'
basename = f'{folder}/oregon-projections_{date}_{version}'
fn_obj   = f'{basename}.obj'
fn_fig   = f'{basename}_hs.png'

hsys = covidhs.HealthSystem(filename=fn_obj)
hsys.analyze()
hsys.plot()
