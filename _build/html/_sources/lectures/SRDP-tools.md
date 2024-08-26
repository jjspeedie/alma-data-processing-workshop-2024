# SRDP Tools for ALMA data (and beyond!)

What is SRDP? It's an observatory effort to make ALMA data easier to use. Leverage things like the pipeline and the cluster at NRAO. Provides users the compute and workflows to do most of the heavy processing, so you only need to take what you need. Basically, just want to make things easier for you.

Selfcal has been included in AUDI since June 2023 (hif_selfcal).

## Auto-selfcal: Evaluating success

## Auto-selfcal: Available versions

Stand-alone:

* pip installable! Not yet, but soon (few months).

## Future development

* Eb to EB alignment pre-selfcal.

* Multi-configuration support

Note: manual self-cal could yield better results sometimes. But, significant improvements probably not likely.

## Summary: ALMA SRDP Capabilities

Self-cal has been a big focus over the last couple years and happy with it. You can use it in the AUDI service.

Note: No NRAO SRDP services are available through the ALMA archive. Only the NRAO archive.

There's ways to access the NRAO archive in a scripted manner.

# Live Demos

## NRAO archive data.nrao.edu

Interface is a bit simpler than ALMA archive.

The text search bar searches for absolutely everything; but you can also search in a controlled manner.

Then look at the buttons; can click on what's in the MOUS. Can click the button "Download Restored MS".

Sometimes it's not restorable; that'll be the case when something manual had to be done to a dataset. Other times it means there was a problem adjusting the calibrations. The fraction of non-restorable: 5-10% (more as you go back). Also do not let you restore TP data.

## AUDI demo

How many requests do you get per day? A few per week. But several per day for the calibrated MS downloads.


# for your workshop

The TW Hya MS will not work for auto-selfcal, the MS is missing the meta data.

2017.1.00857.S program; AS 205A

https://www.cv.nrao.edu/~jtobin/weblog-2017.1.00857.S/html/index.html (this is an example weblog for the whole AUDI process)










<!-- sys.exit() -->
