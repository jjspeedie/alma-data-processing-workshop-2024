# ALMAGuides: a first look at imaging and at spectral line imaging

In the Astrocloud link, see Holly's uploads in the First Look folder. There's a suggested speech document, and some non-interactive version for those who can't use the interactive version on their laptop.

All of this content is a condensed version of the First Look (TW Hya) CASAGuide page.

## Goal of these tutorials

Continuum images and line cubes using tclean. Understand some key parameters (arguments) of tclean.

## First look at imaging

Slides on what tclean is doing, spatial filtering, deconvolution algorithms, etc.

## Using CASA tasks and getting oriented

All in one command (PREFERRED) - don't even bother with inp.

Q: Should you do interactive clean? Or it's being phased out?

A: imview is needed for interactive tclean; which does not work on MacOS14. Something called "iClean" is coming. Also depends on your data; for 12m data you can use auto-multithresh. For 7m data sometimes it cleans the sidelobes.

## Inspecting your data

Check the uvcoverage. Check the baseline coverage. Do both with plotms.

Some imsizes are more efficient: (1) square, not rectangular; (2) power of 2. tclean will make a suggestion. Analysisutils will also make a suggestion (imadvise).

# First look at imaging: the science target

Use split to channel average and reduce the size of the dataset.



Blue arrow in imview will let it go until completion.

If you get a square FOV out, it's because of a image mask error. 







<!-- sys.exit() -->
