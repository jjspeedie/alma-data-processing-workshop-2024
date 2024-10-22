"""
This script was written for CASA 6.6.4.34
Source: First Look at Self Calibration (CASA Guide)
https://casaguides.nrao.edu/index.php/First_Look_at_Self_Calibration_CASA_6.5.4
Adapted for ALMA Data Processing Workshop @ University of Victoria
J. Speedie (jspeedie@uvic.ca) October 2024

Dataset: TW Hya calibrated continuum measurement set (435 MB):
twhya_calibrated.ms.tar
https://bulk.cv.nrao.edu/almadata/public/ALMA_firstlooks/twhya_calibrated.ms.tar

Untar with: tar -xvzf twhya_calibrated.ms.tar
"""
import os


"""
######################################################
######           CREATE INITIAL MODEL          #######
######################################################
"""

tclean(vis='twhya_calibrated.ms',
       imagename='first_image',
       field='5',
       spw='',
       specmode='mfs',
       deconvolver='hogbom',
       nterms=1,
       gridder='standard',
       imsize=[250,250],
       cell=['0.1arcsec'],
       weighting='natural',
       threshold='0mJy',
       niter=5000,
       interactive=True,
       savemodel='modelcolumn')

"""In the GUI, place a mask. Then click the green arrow button once. When the
GUI comes up again, click the red X button to stop deconvolution."""

"""
######################################################
######    CREATE FIRST SET OF GAIN SOLUTIONS   #######
######################################################
"""

gaincal(vis="twhya_calibrated.ms",
        caltable="phase.cal",
        field="5",
        solint="inf", # Notice this choice
        calmode="p",
        refant="DV22",
        gaintype="G")

"""
######################################################
######    APPLY FIRST SET OF GAIN SOLUTIONS    #######
######################################################
"""

applycal(vis="twhya_calibrated.ms",
         field="5",
         gaintable=["phase.cal"], # The calibration table
         interp="linear")

"""
######################################################
###### IMAGE TO EVALUATE THIS ROUND OF SELFCAL #######
######################################################
"""

tclean(vis='twhya_calibrated.ms',
       imagename='after_self_cal',
       datacolumn='corrected',
       field='5',
       spw='',
       specmode='mfs',
       deconvolver='hogbom',
       nterms=1,
       gridder='standard',
       imsize=[250,250],
       cell=['0.1arcsec'],
       weighting='natural',
       threshold='0mJy',
       interactive=True,
       niter=5000)


"""[Continue with more rounds with decreasing solint]"""



# sys.exit()
