# What's New with CASA and Pipeline?

## Devaky Kunneriath (new deputy sub system scientist)

First slide is basically where you can find information about CASA:

### Slide 2

* Documentation

* CASA paper you cite in your papers

* versions of CASA and Pipeline

* Heuristics paper (2023); has information you may not find in weblog

* Link to the Helpdesk

### Slide 3

CASA is software; pipeline is an algorithm that uses CASA tasks.

CASA is released once every few months; The pipeline is released once per year.

The version numbers will be updated by October 1.

### Slide 7

What's new with CASA?

Maintenance/bugfixes: (these are really just for rare, obvious cases)

* psfphasecenter now works properly

* Fixed bug in how tclean treats weights for multiple MS files

Other notable fixes... e.g. niter=0 now returns a dictionary. And a new casaconfig module that will manage the configuration and data used by CASA.


### Slide 11

What's new with the pipeline?

* PL2024 will include calibration of Band-to-band data! see hifa_diffgaincal. (Previously this was manually calibrated)

* (slide 15) Tsys flag contamination (previously identified manually). Now the ID and flagging is automated. It compares the Tsys on your bandpass calibrator (should be feature-free) with that of on source. (slide 16). This usually only matters when your source is being used for Tsys calibration instead of your phase calibrator. 

* (slide 18) Improvements to hif_findcont and hif_uvcontsub. Now cont.dat is more portable; uses real SPW IDs (previously used virtual SPW IDs).

* psfphasecenter for pipeline mosaics. Only for irregular mosaic shapes.

* (slide 20) hif_selfcal; fixed issue there. hif_renorm, corrections are not applied as calibration tables.

* (slide 21) hif_makeimages; the labels "regcal" and "selfcal" are now reordered; if selfcal is applied, now line images are just made one.

### You can re-image your data using ALMA pipeline tasks!

Re-image using Imaging Pipeline Reprocessing Tool. Benefit: You can leverage the pipeline heuristics, and all the diagnostic plots.


### What's ahead for ALMA?

WSU.

In preparation for that, CASA and pipeline are focused on: Improving performance, automation, QA scoring, flagging, and basically try to avoid any need for manual.

RADPS-ALMA will replace CASA and pipeline. (Radio Astronomy Data Processing System; Amanda Kepley).













<!-- sys.exit() -->
