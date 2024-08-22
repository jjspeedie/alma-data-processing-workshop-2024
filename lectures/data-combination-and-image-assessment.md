# Data Combination and Image Assessment with ALMA (Sarah Wood)

A really hot topic right now.

ALMA is three arrays in one.

Where the antennas came from, Morita array, the different baselines.

Highlighting cycle 11 configurations.

Table 7.5 of the ALMA Technical Handbook. You can't just combine things willy nilly, they need to be overlapped.

Why would we want to combine configurations? The "short-spacing" problem.

Zero-spacing problem (Koda+2019).

Plunkett et al. (2023): Used PHANGS skymodel and M100 (cycle 0 real data).


## Considerations

1. Overlapping baselines.

2. Weights. That's where the integration time differences come into play.

3. rms, similar idea.

4. Dynamic range...

## Combination methods

We'll use feather, it's the currently recommended version. It's well known. Next is sdint, but is not out of experimental phase yet.

### Sdint-imaging CASA docs page

For comparison to feather. Feather paper: Bill Cotton et al. 2017 in PASP, Fourier Plane something something. Not jointly deconvolving.

## Data Combination (hands on portion)

M100 data CASAGuide (Band 3 combine 6.5.4). Baseline subtracted (.bl) is like trendline subtracted.

How do we get an image that has all the data AND all the flux?


```python
os.system('rm -rf M100_*m.ms.listobs')
listobs('M100_Band3_12m_CalibratedData.ms',listfile='M100_12m.ms.listobs')
listobs('M100_Band3_7m_CalibratedData.ms',listfile='M100_7m.ms.listobs')
```
Strange that they have different spectral setups; likely because SV data.

CHECK THE WEIGHTS. We will skip this today. Check the CASA guides and there's also a memo. As of CASA 4.2.2 has solidified. The rms ~ 1/sigma**2. See the page called "data weights".

Split out CO SPWs.


```python
os.system('rm -rf M100_12m_CO.ms')
split(vis='M100_Band3_12m_CalibratedData.ms',
      outputvis='M100_12m_CO.ms',spw='0',field='M100',
      datacolumn='data',keepflags=False)
os.system('rm -rf M100_7m_CO.ms')
split(vis='M100_Band3_7m_CalibratedData.ms',
      outputvis='M100_7m_CO.ms',spw='3,5',field='M100',
      datacolumn='data',keepflags=False)
```
This step is not really needed; you can just go ahead and use the tclean with different spws.


```python
os.system('rm -rf M100_combine_CO.ms')
concat(vis=['M100_12m_CO.ms','M100_7m_CO.ms'],
       concatvis='M100_combine_CO.ms')
```
Concatenate the data. Now we should have a MS that has 3 SPWs.


```python
os.system('rm -rf ' + 'M100_combine12+7_CO_cube' + '.*')
tclean(vis='M100_combine_CO.ms',
    imagename='M100_combine12+7_CO_cube',
    gridder='mosaic',
    pbmask=0.2,
    imsize=800,
    cell='0.5arcsec',
    weighting='briggsbwtaper',
    robust=0.5,
    phasecenter='J2000 12h22m54.9 +15d49m15',
    specmode='cube',
    width='5km/s',
    start='1400km/s',
    nchan=70,
    restfreq='115.271201800GHz',
    outframe='LSRK',
    restoringbeam='common',
    mosweight=True,
    niter=10000,
    threshold='0.03mJy',
    usemask='auto-multithresh',
    sidelobethreshold=2.0,
    noisethreshold=4.25,
    minbeamfrac=0.3,
    lownoisethreshold=1.5,
    negativethreshold=0.0,
    growiterations=75,
    interactive=False,
    pbcor=True)
```












Erica: GPT memo https://ui.adsabs.harvard.edu/abs/2019AAS...23335403H/abstract
https://library.nrao.edu/public/memos/gbt/GBT_300.pdf




















<!-- sys.exit() -->
