"""
This script was written for CASA 6.6.4.34
Prepared for ALMA Data Processing Workshop @ University of Victoria
J. Speedie (jspeedie@uvic.ca) October 2024

Additional scripts needed: *.py from
https://github.com/jjtobin/auto_selfcal

Dataset: TW Hya calibrated continuum measurement set (435 MB):
twhya_calibrated.ms.tar
https://bulk.cv.nrao.edu/almadata/public/ALMA_firstlooks/twhya_calibrated.ms.tar

Untar with: tar -xvzf twhya_calibrated.ms.tar
"""
import os


"""
######################################################
######       SPLIT OUT THE SCIENCE TARGET      #######
######################################################
"""

os.system('rm -rf twhya_target.ms') # We're about to create this

split(vis='twhya_calibrated.ms', # Old measurement set (435 MB)
      field='5', # TW Hya
      width='8',
      outputvis='twhya_target.ms',  # New measurement set (43 MB)
      datacolumn='data')

listobs(vis='twhya_target.ms',
        listfile='twhya_target_listobs.txt')

"""
Then exit CASA, and run auto_selfcal:
casa -c auto_selfcal.py
"""

















# sys.exit()
