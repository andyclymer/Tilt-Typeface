# Notes on initial variable font builds
Stephen Nixon (@ArrowType), 2020-01-31

*(start 12:30)*

1. Make `venv`
2. Add `requirements.txt`

First obstacle:

```
cu2qu.errors.IncompatibleFontsError: fonts contains incompatible glyphs: 'Aogonek', 'Ccedilla', 'caron', 'caroncmb', 'cedilla', 'cedillacmb', 'circumflex'
```

*(Pause 12:40)*
*(Start 5:40)*

Because this is a cu2qu conversion error, I'll check that all segments are strictly compatible.

To do so, I'll adapting a shell script to check segments in masters: `sources/mastering-scripts/check-segments-selected-masters.py`

![Segment check for Aogonek in Tilt Neon masters, showing incompatibilities](assets/2020-01-31-17-52-21.png)\

Full results:

```
type-repos/google-font-repos/Tilt-Typeface  mastering ✗                                                                                                                                                                                                                                          26m ◒  
▶ python sources/mastering-scripts/check-segments-selected-masters.py "sources/Tilt Neon/Rotated" "Aogonek Ccedilla caron caroncmb cedilla cedillacmb circumflex"
Getting UFO paths
['Aogonek', 'Ccedilla', 'caron', 'caroncmb', 'cedilla', 'cedillacmb', 'circumflex']
['SubSource-HROTx_VROTdd.ufo', 'Source-HROTd_VROTd.ufo', 'SubSource-HROTn_VROTdd.ufo', 'SubSource-HROTdd_VROTd.ufo', 'SubSource-HROTd_VROTdd.ufo', 'Source-HROTx_VROTn.ufo', 'Source-HROTx_VROTx.ufo', 'Source-HROTn_VROTd.ufo', 'Source-HROTn_VROTn.ufo', 'SubSource-HROTdd_VROTdd.ufo', 'Source-HROTn_VROTx.ufo', 'Source-HROTx_VROTd.ufo', 'Source-HROTd_VROTx.ufo', 'Source-HROTd_VROTn.ufo', 'SubSource-HROTdd_VROTn.ufo', 'SubSource-HROTdd_VROTx.ufo']


Segment types: 🥐 = curve | 📏 = line | 🚚 = move | 🥨 = qcurve

FONT                            | /Aogonek: contours & segments
------------------------------- | ------------------------------------------------------------------------------------------------
Source-HROTd_VROTd.ufo          | C00 [segs 22] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTd_VROTn.ufo          | C00 [segs 24] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐  | C01 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTd_VROTx.ufo          | C00 [segs 22] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTd.ufo          | C00 [segs 22] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTn.ufo          | C00 [segs 24] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐  | C01 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTx.ufo          | C00 [segs 22] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTd.ufo          | C00 [segs 22] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTn.ufo          | C00 [segs 24] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐  | C01 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTx.ufo          | C00 [segs 22] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTd_VROTdd.ufo      | C00 [segs 22] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTd.ufo      | C00 [segs 22] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTdd.ufo     | C00 [segs 22] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTn.ufo      | C00 [segs 24] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐  | C01 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTx.ufo      | C00 [segs 22] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTn_VROTdd.ufo      | C00 [segs 22] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTx_VROTdd.ufo      | C00 [segs 22] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 


FONT                            | /Ccedilla: contours & segments
------------------------------- | ------------------------------------------------------------------------------------------------
Source-HROTd_VROTd.ufo          | C00 [segs 12] 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTd_VROTn.ufo          | C00 [segs 12] 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTd_VROTx.ufo          | C00 [segs 12] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐  | C01 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTd.ufo          | C00 [segs 12] 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTn.ufo          | C00 [segs 12] 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTx.ufo          | C00 [segs 12] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐  | C01 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTd.ufo          | C00 [segs 12] 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 10] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTn.ufo          | C00 [segs 12] 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTx.ufo          | C00 [segs 12] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐  | C01 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTd_VROTdd.ufo      | C00 [segs 12] 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTd.ufo      | C00 [segs 12] 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTdd.ufo     | C00 [segs 12] 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTn.ufo      | C00 [segs 12] 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTx.ufo      | C00 [segs 12] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐  | C01 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTn_VROTdd.ufo      | C00 [segs 12] 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTx_VROTdd.ufo      | C00 [segs 12] 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C01 [segs 10] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 


FONT                            | /caron: contours & segments
------------------------------- | ------------------------------------------------------------------------------------------------
Source-HROTd_VROTd.ufo          | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTd_VROTn.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐  | 
Source-HROTd_VROTx.ufo          | C00 [segs 08] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTd.ufo          | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTn.ufo          | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTx.ufo          | C00 [segs 08] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTd.ufo          | C00 [segs 08] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTn.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐  | 
Source-HROTx_VROTx.ufo          | C00 [segs 08] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTd_VROTdd.ufo      | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTd.ufo      | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTdd.ufo     | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTn.ufo      | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐  | 
SubSource-HROTdd_VROTx.ufo      | C00 [segs 08] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTn_VROTdd.ufo      | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTx_VROTdd.ufo      | C00 [segs 08] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐  | 


FONT                            | /caroncmb: contours & segments
------------------------------- | ------------------------------------------------------------------------------------------------
Source-HROTd_VROTd.ufo          | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTd_VROTn.ufo          | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTd_VROTx.ufo          | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTd.ufo          | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTn.ufo          | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTx.ufo          | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTd.ufo          | C00 [segs 08] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTn.ufo          | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTx.ufo          | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTd_VROTdd.ufo      | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTd.ufo      | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTdd.ufo     | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTn.ufo      | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTx.ufo      | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTn_VROTdd.ufo      | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTx_VROTdd.ufo      | C00 [segs 08] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐  | 


FONT                            | /cedilla: contours & segments
------------------------------- | ------------------------------------------------------------------------------------------------
Source-HROTd_VROTd.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTd_VROTn.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTd_VROTx.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTd.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTn.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTx.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTd.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTn.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTx.ufo          | C00 [segs 10] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐  | 
SubSource-HROTd_VROTdd.ufo      | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTd.ufo      | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTdd.ufo     | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTn.ufo      | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTx.ufo      | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTn_VROTdd.ufo      | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTx_VROTdd.ufo      | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 


FONT                            | /cedillacmb: contours & segments
------------------------------- | ------------------------------------------------------------------------------------------------
Source-HROTd_VROTd.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTd_VROTn.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTd_VROTx.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTd.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTn.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTx.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTd.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTn.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTx.ufo          | C00 [segs 10] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐  | 
SubSource-HROTd_VROTdd.ufo      | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTd.ufo      | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTdd.ufo     | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTn.ufo      | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTx.ufo      | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTn_VROTdd.ufo      | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTx_VROTdd.ufo      | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | 


FONT                            | /circumflex: contours & segments
------------------------------- | ------------------------------------------------------------------------------------------------
Source-HROTd_VROTd.ufo          | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTd_VROTn.ufo          | C00 [segs 08] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTd_VROTx.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐  | 
Source-HROTn_VROTd.ufo          | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTn.ufo          | C00 [segs 08] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTn_VROTx.ufo          | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTd.ufo          | C00 [segs 08] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTn.ufo          | C00 [segs 08] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐  | 
Source-HROTx_VROTx.ufo          | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐  | 
SubSource-HROTd_VROTdd.ufo      | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTd.ufo      | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTdd.ufo     | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTn.ufo      | C00 [segs 08] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTdd_VROTx.ufo      | C00 [segs 08] 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐  | 
SubSource-HROTn_VROTdd.ufo      | C00 [segs 06] 🥐 🥐 🥐 🥐 🥐 🥐  | 
SubSource-HROTx_VROTdd.ufo      | C00 [segs 08] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐  | 
```