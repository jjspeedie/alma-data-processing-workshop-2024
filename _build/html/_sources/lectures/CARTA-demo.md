# Visualization of ALMA Archive Data Products with CARTA

## John Hibbard

### CARTA basics

Great website and documentation; a lot of the functionality has demo videos. Also has helpdesk support.

Current release is v4.1 but it's v4.0 with bugfixes (so really v4.0). You get that version (v4.0) in the ALMA archive as well.

CARTA was originally developed as a NA ALMA Development Study (Cycle 1), then Project (Cycle 2), then taken over by IDIA in 2018, and ASIAA. It had to become more substantial with proper project management, to support the large observatories with long timescale and eventually replace the CASA viewer. So it's professionally managed now.

### Current CARTA Key Features (V4.0)

List of functionality.

In the future: RGB support, 3D volume rendering (!!). Really grown (originally DS9 knock off).

Yellow link in slides shows new feature highlights.

### More information

Online documentation, with many mini-videos.

From 2022, Kuo-Sang Wang (project scientist) did ALMA iTrain. See Youtube. European ARC nodes, in-depth training videos. Number 12.

### CARTA Operation Modes

CARTA separates the backend (where the data is), and just broadcasts a SUSBET of the data. You're just broadcasting the cutout of the screen; very responsive between backend and front end. No lag. There's also an electronic stand-alone app (what you have). The frontend is where the GPU acceleration is happening, hence why it's so fast.

Implemented in both ALMA and NRAO archive. The CARTA backend is running where the data is (on the archive); the frontend is your browser.

CARTA will eventually replace most CASA viewer functions (except visibility viewing or interactive cleaning).

### CARTA Demo v4.0 (v4.1 stand-alone)

Note you can't save anything you do with CARTA on the ALMA archive.

Demo in the ALMA archive.

* The preview button is available ever since the REL project. At least back to 2015 (cycle 3). Amendment: Actually it goes back to 2012. Note you have to line a spectral line first.

* Open up a CARTA session for GM Aur DSHARP program. 13CO(2-1) cube. First switch layout: View> Layouts> Existing Layouts> JEHview (cube analysis).

* Now open SPW 37 (12CO 2-1). Do the layouts thing again. Note: Do File > Append > 12CO.

* Then append 2017.1.01151.S program aggregate continuum in Band 4. Do that by first having the cubes open. Then go to download manager. Then append it to the window (it should appear in the list).
Select tt0 fits (band 4); if it has to do a Taylor expansion to get the continuum; so tt0.

* First match in Image List.

* You can change the title of the cubes to be more intuitive, under "Title" under Global. And the title colour. Though when you save the workspace these don't get saved.

* Z Profile: Click checkbox next to "Image", shows all the spectra. Instead of making a region, you can hold "F" and click and that has the same effect as making a Region point.

* Contour configuration: Scaling can be logarithmic. Colour can be colormapped.

* Regions: Make a circular one. You can change the names of the Regions. Double click on the Region; and enter region name. Change its colour and thickness.

* Docking and undocking. Drag and drop your widgets, etc.

* Can hide the toolbar if it gets in the way.

* Make moments. That's a function of the Z-profile. Click the gear, it gets you extra functionality. The range should be -5 to 15 km/s. The coordinate should be radio velocity (km/s). Mask is also important. Cool feature: if you slide your cursor on the colour bar, you can use this to figure out your level; at the bottom right, it tells you what the level is. 5e-3 is a good rough level. Register it by matching.

* Encircle the emission using a polygon; call that region "Total". Now you can go to the Z profile and color the spectra if you like.

* Multiple regions: Look at 12CO 2-1 and look at the redshifted/blueshifted regions individually. Then you can see the different apertures. Statistics: rms (for line-free); Flux Density (for our cases).

* Line fitting: Function of the Z-profile. Next to Moments, fdo Fitting. Can click auto-detect. Can make it 2 components. Can also drag and draw your own box. Cursor. Then click "Fit". Can also ask it to plot residuals.

* Saving worksapces: Open>Save Workspace. Somehow there are cookies as well; but not all bits are saved. BUT YOU HAVE TO HAVE THE SAME CUBES LOADED.

* LOADING INTO THE FRONTEND: You do that purely by clicking the CARTA button on the archive.

### Desktop version.

New: You can type in a path. It remembers the last place you went.

Filter (search bar); unix pattern, fuzzy search, etc.

10000hr_uvbinfig.image.

Online Catalog Query: SIMBAD or VIzer. Use VizieR. Search "starbust". Galaxies. Click inside "Please select catalog tables", then there's all the matches. You want number 4. Now you have a catalog window. This is all using CHILES layout. Search radius was 0.5 deg.

Catalog selector target: Will show you where in the table that value is.

Spectral line query.

You can Smooth spectra too; Hanning smoothing etc.

You can also do 2D scatter. There's a section of the user guide that shows this.


### One cube, but multiple transitions

HC3N, 12CO18O, 13CO, etc. All these transitions in a single cube.

Go Image List Settings > Rest Frequency > then change the rest frequency for each cube. Load the same cube four times by doing Append. Then change your Z-profile to velocity. Make sure to move in velocity not channel number. Cube: X87d_X289_NGC253_sci.spw2.cube.I.pbcor.fits. Can also save subcubes.

Triangle region gives you angular measurements. Annotations > Compass, Vector, Arrows, etc.


* Position velocity (active). Make average width big (in pixels). Preview rebin does 1 pixel. Do "preview", and you can shift and rotate until you think you have the right cut. Then when happy, click generate. Now it can be annotated, registered, etc and save as a fits file.





### Workspace sharing (slide 7)

Demo. It's functional for you saving your work and continuing; but not fully functional. Currently you can only share URL with remote collaborators if you have a site-deployment version (like at your institution - only if you have that.)






Also, Kuo-Song made the data from the M51 catalog demo in the Users Guide available at:
https://drive.google.com/drive/folders/1VmTwKBjMOxckN_-XvJSLGprxP-X1lnyL?usp=sharing







<!-- sys.exit() -->
