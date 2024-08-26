# Navigating the ALMA IF Pipeline + Weblog (Ed Starr )

(There is a SD/single-dish pipeline as well)

## Reference Material

Videos: EU ARC Network "ALMA Weblog Inspection", and i-Train

## CASA Pipelines

What is a pipeline? High-level look; a series of CASA tasks for calibrating raw data and imaging the corrected data. A recipe. Different recipe for IF and SD, and ALMA and VLA and VLASS.

The easiest way for a user to run it: pipescript.py (execfile).

The tasks all start with H (heuristics). IF means interferometry. A means ALMA. SD means single dish.

SOUS/GOUS/MOUS breakdown; the pipeline is run on the MOUS level.

## Overview of the IF Calibration Steps

1. System temperature (Tsys vs. frequency)

2. Antenna position

3. Water vapor

4. Bandpass (per channel)

5. Flux (per SPW)

6. Gain

7. Renorm

Imaging:

8. Continuum detection, fitting and subtraction

9. Continuum images per SPW

10. Agregate continuum image for all SPWs combined

11. Cube images for lines

12. Self-calibration (NEW AS OF CYCLE 10)

13. Repeat all imaging if self-cal was beneficial


## What is a Weblog?

A follow-along.

QA2 report. These come straight from the archive (CASA 5.4).


Very nice follow along. Tab by tab. Scan lengths in Weblog.

### hif_importdata

Want the calibrator to be within a couple days.

### hifa_flagdata

### h_tsyscal and hifa_tsysflag

The pipeline is great at flagging. Vampire teeth is correlator issue. Edge channels is common.

tsyscal is BEFORE flagging; tsysflag is AFTER flagging.

### hifa_wvrgcalflag

Want reg and green to be tight along zero.

### hifa_bandpass

The main page shows plots from reference antenna only, so recommend clicking through to get per spw, per antenna, etc. Best idea: filter by SPW (should look similar for all antennas).

Missed a lot of this.

### hifa_spwphaseup

Everything is below green line of 30 degrees which is fantastic; red is after applying them, green is before.

### higa_gfluxscale

Comparing flux calibrator to the flux calibrator in the catalog.


### higa_timegaincal

NOT the corrected data; these are the solutions, they're doing what they're supposed to do (correcting the data).

Split into two parts: phase vs. time and amp vs. time. They'll be applied to the data.

Then the second part are diagnostic and not applied to the data.

### hif_applycal

The actual science target data; applies all the calibration tables.

Amplitude vs. time gives you the antenna-based breakdown.

Sometimes bandpass amplitude vs. time will fall off like waterfall (often cannot be fixed, due to weather).

### Retrieve plotting commands

Very useful.

### Typical issues in amp vs. time // phase vs. time

### Typical issues in amp vs. freq

Overall nice collection. Whenever you have frequency on the x-axis, it might be a time-based effect.

### Typical issues in target data

Anything that looks fuzzy.

### hif_makeimages (cals)

Iteration 1 is lean image, iteration 0 is dirty.

### Check rouse Imaging

What is it? Used to assess calibration quality on a source other than a target. It's a point-like target source that you apply your calibration solutions to, in order to check that they worked. Always a point source, usually dimmer than a calibrator.

### Renorm (skipped)

Due to strong line emission detected in auto-correlation.

Used to be a big deal, now fixed, totally effective.

### hif_findcont

Conservative, not updated, doesn't rely on uvcontsub.

### hif_makeimlist and hif_makeimages

These imaging commands can be copy and pasted and used as a script, just like the other tasks.

Regular cal and selfcal.

Can get image stats. Sensitivity rms is what's used for QA process.

### hif_selfcal

Per solint, summary...

### Looking Ahead

Big change in Cycle 11: B2B calibration. Also: self-cal improvements.







# Re-running the Imaging Pipeline (Tristan Ashton)

Get images that conform to your science goals.

## Outline

1. Obtain the calibrated measurement set (scriptForPI, piperestorescript, SRDP)

2. How to re-run the calibration pipeline

3. How to run the imagine pipeline

## Directory structure (delivered data)

Product: data delivery products (what pipeline created).

"Raw" (has the raw data) and "calibration" (tables) but no "calibratED". So you have to put those together.

Easiest way to do that: scriptForPI ("script" directory).


### Using piperestorescript.py

It's the thing that's called by scriptForPI. You don't need to worry about it.


### NRAO SRDP/AUDI

Will get a whole talk on it by John tomorrow.

### How to re-run the calibration pipeline if needed

casa_pipescript.py is for re-running the pipeline entirely. Why would you want to do this?
* Add flags
* Update fluxes
* Update baselines
* Use a new version of the pipeline
* Add or remove an ASDM
* Change reference antennas

### Pipeline helper text files

flux.csv, jyperk.csv, etc... They exist, and these are the things you'd edit for any of the listed purposes.

### Re-running the calibration

Set up your directory... almascience.nrao.edu/processing/science-pipeline. Then running it is as simple as running pipescript.py.

Each of the lines correspond to the tasks in the weblog. Here's where each of the helper txt files get used (the corresponding functions).

There's the calibration half and after there's the imaging half. The imaging half is what we'll talk about next. If you're only re-doing the calibration, it's recommended to comment-out the imaging half (all of them). If you comment out anything in the calibration step, it will break.

### How to run the imaging pipeline

See CASAGuide: Cycle 10 imaging pipeline re-processing. Can also see the same but for manually calibrated data (went through slightly different process).

Why would you want to re-image and let the pipeline do it for you? List given there.

### Restore Calibration and Prepare for Re-imaging

Move to directory with calibrated data, make tweaks to any helper files (pipescipt.py has calibration portion commented out); then start casa --pipeline, then do execfile('casa_pipescript.py'). Recommendation here is to use the latest version of CASA.

Example CASA imaging pipeline script. Ignore all the context lines. What you want to look at is the content of the "try" block.

imageprecheck chooses your robust parameter value for you; so if you want a specific robust value, don't use the imageprecheck task.

Bonus: Every time you run pipescript, a new weblog is always created!!

### scriptForReprocessing

This is something new that has been added into the added-value data delivereies; only the NA PI's get this, starting in Cycle 9, no other nodes/ARCS/regions do this.

Main delivery is: calibrated_final.tgz. This is individual calibrated ASDMs along with some of the ...

If you run scriptForReprocessing yourself, it will recreate identical images as from the original pipeline run.

Honestly sounds like a really useful thing. Knowlwedge base articles: NA added value data products.










<!-- sys.exit() -->
