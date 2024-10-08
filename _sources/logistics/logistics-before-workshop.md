# Before the workshop

This page describes important pre-workshop tasks that will help you have a productive workshop experience.


## Primer Videos

Please watch the following videos from the **ALMA Primer Video Series** before the start of the workshop:

* ALMA Primer Series: <a href="https://youtu.be/5RA9klRpvfY?si=xL5XMt3PyXJAtkPp" target="_blank">Introduction to Calibration</a>
* ALMA Primer Series: <a href="https://www.youtube.com/watch?v=fF3KetPUyFE" target="_blank">Introduction to CLEAN</a>
* ALMA Primer Series: <a href="https://www.youtube.com/watch?v=50ouWFLOWaw" target="_blank">CLEAN Masking</a>

<!-- * ALMA Primer Series: Introduction to Calibration https://youtu.be/5RA9klRpvfY?si=xL5XMt3PyXJAtkPp
* ALMA Primer Series: Introduction to CLEAN https://www.youtube.com/watch?v=fF3KetPUyFE
* ALMA Primer Series: CLEAN Masking https://www.youtube.com/watch?v=50ouWFLOWaw -->

## Necessary software: CASA & CARTA

1. We'll have hands-on experience working with ALMA data during the tutorials. Please **install the software** we will be working with:

* CASA 6.6.5 (General Use): <a href="https://casa.nrao.edu/casa_obtaining.shtml" target="_blank">https://casa.nrao.edu/casa_obtaining.shtml</a>

* CARTA v4.1: <a href="https://cartavis.org/#download" target="_blank">https://cartavis.org/#download</a>

<!-- Note that CASA requires a Linux-based environment to run. If you have a Mac OSX or a linux machine (ubuntu, etc), you should have no problems. If you have a PC, you will need to download some type of linux OS - I personally use WSL (Windows Subsystem for Linux) with Ubuntu installed, through the MobaXTerm tool.  -->


2. Please **check that you can start CASA** before the first day of the workshop. In a terminal (linux command line), type:

```bash
casa
```

CASA is built in iPython, and you will see a number of initialization messages, a list of available tasks, and, finally, a Python command line prompt:

```bash
CASA <1>:
```

To exit CASA, simply type:

```bash
CASA <1>: exit
```

More details and tips can be found here: <a href="https://casaguides.nrao.edu/index.php/Getting_Started_in_CASA" target="_blank">Getting Started in CASA</a>.


## ALMA tutorial datasets

**Download the ALMA datasets** we will be working with:

1. TW Hya calibrated continuum measurement set (435 MB): <a href="https://bulk.cv.nrao.edu/almadata/public/ALMA_firstlooks/twhya_calibrated.ms.tar" target="_blank">Click to download twhya_calibrated.ms.tar</a>

Untar this dataset ahead of time:

```bash
tar -xvzf twhya_calibrated.ms.tar
```

A directory should be created called ``twhya_calibrated.ms``. This directory is the measurement set.

2. TW Hya self-calibrated line measurement set (435 MB): <a href="https://bulk.cv.nrao.edu/almadata/public/ALMA_firstlooks/twhya_selfcal.ms.tar" target="_blank">Click to download twhya_selfcal.ms.tar</a>

Untar this dataset too:

```bash
tar -xvzf twhya_selfcal.ms.tar
```

A directory should be created called ``twhya_selfcal.ms``. This directory is the measurement set.

## On the day

On the day of the workshop, **make sure to bring with you**:

* Laptop and charger.
