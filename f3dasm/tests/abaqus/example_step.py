'''
Created on 2020-04-08 15:42:58
Last modified on 2020-09-30 11:37:54

@author: L. F. Pereira (lfpereira@fe.up.pt)

Main goal
---------
Show how to create step using the classes defined in abaqus.modelling
'''


# imports

# abaqus
from abaqus import mdb, backwardCompatibility

# third-party
from f3dasm.abaqus.modelling.step import BuckleStep


# initialization

backwardCompatibility.setValues(reportDeprecated=False)

model_name = 'TEST-STEPS'
job_name = 'Sim_' + model_name
job_description = ''

# define materials
step_name = 'TEST_STEP'


# create model

model = mdb.Model(name=model_name)

if 'Model-1' in mdb.models.keys():
    del mdb.models['Model-1']


# create step

new_step = BuckleStep(step_name)
new_step.create_step(model)
