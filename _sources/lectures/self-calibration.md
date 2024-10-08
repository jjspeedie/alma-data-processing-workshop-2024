# Self Calibration (Dominic & Michael)

A quick review of calibration: Distinguish between antenna-based and baseline-based sources of corruption. Also we bracket the science observations with phase calibrator scans and so we miss things in time.

Phase vs. UVdist: What is special about the calibrators?

* Bright at relevant wavelengths (high SNR)
* Close to science target
* Not variable in time (no "short" term variability)
* Point source (preferred)
* Well known flux and structure
* No spectral features (for bandpass calibrators)

"Not a calibrator!" - Transition to self-cal. That's the segue to self-cal, anything can be a calibrator, including the science target itself.

SNR for self-calibration (slide 18)
SNR>3 ina  solution time less than the time for significant phase variations for all baselines TO A SINGLE ANTENNA.

LINK TO CRYSTAL BROGAN'S SELF CAL MEMO. https://arxiv.org/abs/1805.05266

SNR for self calibration. Amplitude self-cal.

Outline of self calibration process (blue text boxes).

## Automated self-cal

Currently designed for individual points of continuum observations. Doesn't handle lines well.

* No specta line self-cal
* No mosacis
* No ALMA data older than Cycle 3
* Limited support for other telescopes


Self calibration resources:

* ALMA self-cal tutorial (CASAgauides)
* VLA self-cal tutorial
* Self Calibration pipeline preview



Slide 16 is a VLA image, with auto-self cal.





<!-- sys.exit() -->
