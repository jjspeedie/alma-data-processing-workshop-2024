# Tutorial 3: Automated Self-Calibration

`````{admonition} [Link to Script](./scripts/script_auto_selfcal_setup.py)
:class: tip

```
This script was written for CASA 6.6.4.34
Prepared for ALMA Data Processing Workshop @ University of Victoria
J. Speedie (jspeedie@uvic.ca) October 2024

Additional scripts needed: *.py from
https://github.com/jjtobin/auto_selfcal
```

`````

**Dataset:** TW Hya calibrated continuum measurement set (435 MB)

``twhya_calibrated.ms.tar`` (<a href="https://bulk.cv.nrao.edu/almadata/public/ALMA_firstlooks/twhya_calibrated.ms.tar" target="_blank">Download</a>)

## Download auto_selfcal scripts

`````{admonition} Additional scripts needed!

 Download ``*.py`` from https://github.com/jjtobin/auto_selfcal

* [auto_selfcal.py](./scripts/auto_selfcal-main/auto_selfcal.py) <<- Big important one
* [regenerate_weblog.py](./scripts/auto_selfcal-main/regenerate_weblog.py)
* [run_selfcal.py](./scripts/auto_selfcal-main/run_selfcal.py)
* [selfcal_helpers.py](./scripts/auto_selfcal-main/selfcal_helpers.py)
* [split_calibrated_final.py](./scripts/auto_selfcal-main/split_calibrated_final.py)
* [LICENSE](./scripts/auto_selfcal-main/LICENSE)
* [README](./scripts/auto_selfcal-main/README)

`````

Your working directory should look like:

```bash
TUTORIAL1 >> ls
auto_selfcal-main/
script_auto_selfcal_setup.py
twhya_calibrated.ms.tar
```

Untar with:

```bash
tar -xvzf twhya_calibrated.ms.tar
```



## Prepare MS for auto_selfcal

Here, we generate what the ``auto_selfcal.py`` script expects.

```python
os.system('rm -rf twhya_target.ms') # We're about to create this
```

Split out the science target:

```python
split(vis='twhya_calibrated.ms', # Old measurement set (435 MB)
      field='5', # TW Hya
      width='8', # For tutorial purposes; in practice, better not to
      outputvis='twhya_target.ms',  # New measurement set (43 MB)
      datacolumn='data')
```

Inspect the new MS:

```python
listobs(vis='twhya_target.ms',
        listfile='twhya_target_listobs.txt')
```

Exit CASA.

## Run automated self-calibration

Copy the auto_selfcal/ scripts into the same directory as ``twhya_target.ms``.

Run the ``auto_selfcal.py`` script:

```bash
casa -c auto_selfcal.py
```

Open and inspect the resulting Weblog! ``weblog/index.html``

Open & inspect resulting ``Target_TW_Hya_Band7*`` files in CARTA!

# Slides

::::{grid}
:gutter: 2

:::{grid-item-card}

<center>

<img src="./images/SRDP_autoselfcal.png" alt="SRDP_autoselfcal" class="mb-1" width="98%">

</center>
+++
<a href="https://www.canfar.net/storage/vault/file/jspeedie/2024-alma-data-processing-workshop/_tutorial3_SRDP_Automated_Self-Calibration.pdf" target="_blank">Download Slides</a>
:::

:::{grid-item}
<!-- Empty column for spacing -->
:::

::::
