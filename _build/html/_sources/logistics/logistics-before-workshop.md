# Before the workshop

This page describes important pre-workshop tasks that will help you have a productive workshop experience.


## Watch some Primer Videos

Please watch the following videos from the **ALMA Primer Video Series** before the start of the workshop:

* ALMA Primer Series: <a href="https://youtu.be/5RA9klRpvfY?si=xL5XMt3PyXJAtkPp" target="_blank">Introduction to Calibration</a>
* ALMA Primer Series: <a href="https://www.youtube.com/watch?v=fF3KetPUyFE" target="_blank">Introduction to CLEAN</a>
* ALMA Primer Series: <a href="https://www.youtube.com/watch?v=50ouWFLOWaw" target="_blank">CLEAN Masking</a>

<!-- * ALMA Primer Series: Introduction to Calibration https://youtu.be/5RA9klRpvfY?si=xL5XMt3PyXJAtkPp
* ALMA Primer Series: Introduction to CLEAN https://www.youtube.com/watch?v=fF3KetPUyFE
* ALMA Primer Series: CLEAN Masking https://www.youtube.com/watch?v=50ouWFLOWaw -->

You may also have fun experimenting with generating interferometric images using the NRAO's **Interferometry Explained** web-based tool:
<a href="https://public.nrao.edu/interferometry-explained/" target="_blank">https://public.nrao.edu/interferometry-explained/</a>

## Install CASA

We'll have some hands-on experience working with ALMA data during the tutorials. Please **install CASA**, the main software used to work with ALMA data. You will need CASA **version 6.6.4** or lower (but not lower than 6.5.*). Use the following dropdown menu to navigate to the right build for your operating system:

````{dropdown} Mac OSX11
Go to: <a href="https://alma-dl.mtk.nao.ac.jp/ftp/casa/distro/casa/release/osx11/" target="_blank">https://alma-dl.mtk.nao.ac.jp/ftp/casa/distro/casa/release/osx11/</a>

<img src="./images/osx11.png" alt="osx11" class="mb-1" width="100%">
````
```{dropdown} Mac OSX12
Go to: <a href="https://alma-dl.mtk.nao.ac.jp/ftp/casa/distro/casa/release/osx12/" target="_blank">https://alma-dl.mtk.nao.ac.jp/ftp/casa/distro/casa/release/osx12/</a>

<img src="./images/osx12.png" alt="osx12" class="mb-1" width="100%">
```
```{dropdown} Mac OSX13
Go to: <a href="https://alma-dl.mtk.nao.ac.jp/ftp/casa/distro/casa/release/osx13/" target="_blank">https://alma-dl.mtk.nao.ac.jp/ftp/casa/distro/casa/release/osx13/</a>

<img src="./images/osx13.png" alt="osx11" class="mb-1" width="100%">
```
```{dropdown} Mac OSX14
Go to: <a href="https://alma-dl.mtk.nao.ac.jp/ftp/casa/distro/casa/release/osx14/" target="_blank">https://alma-dl.mtk.nao.ac.jp/ftp/casa/distro/casa/release/osx14/</a>

<img src="./images/osx14.png" alt="osx14" class="mb-1" width="100%">
```
```{dropdown} Mac OSX10.15
Go to: <a href="https://alma-dl.mtk.nao.ac.jp/ftp/casa/distro/casa/release/osx1015/" target="_blank">https://alma-dl.mtk.nao.ac.jp/ftp/casa/distro/casa/release/osx1015/</a>

<img src="./images/osx1015.png" alt="osx1015" class="mb-1" width="100%">
```
```{dropdown} Linux (RedHat) rhel
Go to: <a href="https://alma-dl.mtk.nao.ac.jp/ftp/casa/distro/casa/release/rhel/" target="_blank">https://alma-dl.mtk.nao.ac.jp/ftp/casa/distro/casa/release/rhel/</a>

<img src="./images/rhel.png" alt="rhel" class="mb-1" width="100%">
```

<!-- <a href="https://alma-dl.mtk.nao.ac.jp/ftp/casa/distro/casa/release/" target="_blank">https://alma-dl.mtk.nao.ac.jp/ftp/casa/distro/casa/release/</a> -->


<!-- * CASA 6.6.4 (General Use): <a href="https://casa.nrao.edu/casa_obtaining.shtml" target="_blank">https://casa.nrao.edu/casa_obtaining.shtml</a> -->

<!-- Note that CASA requires a Linux-based environment to run. If you have a Mac OSX or a linux machine (ubuntu, etc), you should have no problems. If you have a PC, you will need to download some type of linux OS - I personally use WSL (Windows Subsystem for Linux) with Ubuntu installed, through the MobaXTerm tool.  -->

### Check CASA installation

Please **check that you can start CASA** before the first day of the workshop. In a terminal (linux command line), type:

```bash
casa
```

<!-- If you have downloaded CASA v6.6.5, then you may meet the following error on the first startup:

```
casaconfig is trying to download data to /Users/jspeedie/.casa/data (measurespath)
but the directory does not exist.
To allow casa to download ~1GB of data to this path, please create this directory and re-start CASA.
```

Simply make the directory it needs:

```
mkdir ~/.casa/data
```

And then launch CASA again:

```bash
casa
```

More information can be found <a href="https://casadocs.readthedocs.io/en/stable/notebooks/external-data.html" target="_blank">here</a>.  -->

Upon a successful launch, you will see a number of initialization messages, a list of available tasks, and, finally, a Python command line prompt:

```bash
CASA <1>:
```

To exit CASA, simply type:

```bash
CASA <1>: exit
```

More details and tips can be found at: <a href="https://casaguides.nrao.edu/index.php/Getting_Started_in_CASA" target="_blank">Getting Started in CASA</a>.


## Download ALMA tutorial datasets

**Download the ALMA datasets** we will be working with:

1. TW Hya calibrated measurement set (435 MB): <a href="https://bulk.cv.nrao.edu/almadata/public/ALMA_firstlooks/twhya_calibrated.ms.tar" target="_blank">Click to download twhya_calibrated.ms.tar</a>

2. TW Hya self-calibrated measurement set (435 MB): <a href="https://bulk.cv.nrao.edu/almadata/public/ALMA_firstlooks/twhya_selfcal.ms.tar" target="_blank">Click to download twhya_selfcal.ms.tar</a>

<!-- If you wish, you can untar these datasets ahead of time:

```bash
tar -xvzf twhya_calibrated.ms.tar
```
or
```bash
tar -xvzf twhya_selfcal.ms.tar
```

A directory should be created called ``twhya_calibrated.ms`` or ``twhya_selfcal.ms``. This directory is the measurement set.
 -->

## Install CARTA

We will use CARTA for ALMA data visualization. **Please install CARTA v4.1:** <a href="https://cartavis.org/#download" target="_blank">https://cartavis.org/#download</a>

## On the day

On the day of the workshop, **make sure to bring with you**:

* Laptop and charger.

If you encounter any issues or have any questions, don't hesitate to get in touch! Contact Jess at jspeedie@uvic.ca
