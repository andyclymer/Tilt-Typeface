# Notes on initial variable font builds
Stephen Nixon (@ArrowType), 2020-01-31

*(start 12:30)*

1. Make `venv`
2. Add `requirements.txt`
3. Make basic `build.sh` shell script for fontmake + file sorting

### Tilt Neon

Trying to build `sources/Tilt Neon/Rotated/Tilt-Neon.designspace`.

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

### Tilt Prism

Trying to build `sources/Tilt Prism/Rotated 03 Combined/Tilt-Prism.designspace`.

```
cu2qu.errors.IncompatibleFontsError: fonts contains incompatible glyphs: 's'
```

Segments:

```

FONT                            | /s: contours & segments
------------------------------- | ------------------------------------------------------------------------------------------------
Source-HROTd_VROTd.ufo          | C00 [segs 24] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏  | C01 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C02 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C03 [segs 19] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐  | C04 [segs 19] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 📏 📏 🥐 🥐 🥐 🥐 🥐 🥐 📏  | 
Source-HROTd_VROTn.ufo          | C00 [segs 24] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏  | C01 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C02 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C03 [segs 19] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C04 [segs 19] 🥐 📏 🥐 📏 🥐 🥐 🥐 🥐 🥐 📏 📏 📏 🥐 🥐 🥐 🥐 🥐 🥐 📏  | 
Source-HROTd_VROTx.ufo          | C00 [segs 24] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏  | C01 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C02 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C03 [segs 19] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐  | C04 [segs 19] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 📏 📏 🥐 🥐 🥐 🥐 🥐 🥐 📏  | 
Source-HROTn_VROTd.ufo          | C00 [segs 24] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏  | C01 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C02 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C03 [segs 19] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐  | C04 [segs 19] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 📏 📏 🥐 🥐 🥐 🥐 🥐 🥐 📏  | 
Source-HROTn_VROTn.ufo          | C00 [segs 24] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏  | C01 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C02 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C03 [segs 19] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C04 [segs 19] 🥐 📏 🥐 📏 🥐 🥐 🥐 🥐 🥐 📏 📏 📏 🥐 🥐 🥐 🥐 🥐 🥐 📏  | 
Source-HROTn_VROTx.ufo          | C00 [segs 24] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏  | C01 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C02 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C03 [segs 19] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐  | C04 [segs 19] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 📏 📏 🥐 🥐 🥐 🥐 🥐 🥐 📏  | 
Source-HROTx_VROTd.ufo          | C00 [segs 24] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏  | C01 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C02 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C03 [segs 19] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐  | C04 [segs 19] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 📏 📏 🥐 🥐 🥐 🥐 🥐 🥐 📏  | 
Source-HROTx_VROTn.ufo          | C00 [segs 24] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏  | C01 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C02 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C03 [segs 19] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐  | C04 [segs 19] 🥐 📏 🥐 📏 🥐 🥐 🥐 🥐 🥐 📏 📏 📏 🥐 🥐 🥐 🥐 🥐 🥐 📏  | 
Source-HROTx_VROTx.ufo          | C00 [segs 24] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏  | C01 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C02 [segs 08] 📏 🥐 📏 📏 📏 🥐 📏 📏  | C03 [segs 19] 🥐 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 📏 🥐 🥐 🥐  | C04 [segs 19] 🥐 📏 🥐 🥐 🥐 🥐 🥐 🥐 🥐 📏 📏 📏 🥐 🥐 🥐 🥐 🥐 🥐 📏  | 
```

### Tilt Warp

Trying to build with `sources/Tilt Warp/Rotated/Tilt-Warp.designspace`. And it works!

Two warnings to look into, in each master:

```
WARNING:ufo2ft.fontInfoData:Underline thickness not set in UFO, defaulting to UPM * 0.05
WARNING:ufo2ft.fontInfoData:Underline position not set in UFO, defaulting to UPM * -0.075
WARNING:ufo2ft.fontInfoData:Underline thickness not set in UFO, defaulting to UPM * 0.05
```

```
WARNING:ufo2ft.featureWriters.markFeatureWriter.MarkFeatureWriter:duplicate anchor 'above' in glyph 'aogonek.alt'
WARNING:ufo2ft.featureWriters.markFeatureWriter.MarkFeatureWriter:duplicate anchor 'below' in glyph 'aogonek.alt'
```

- [ ] set underline & strikethrough values (probably, these should be the same between all fonts, because software seems to only take one value for variable fonts, in my recent experience)
- [ ] check for duplicate anchors in 'aogonek.alt'

![GIF of working variable font for Tilt Warp](assets/Kapture 2020-01-31 at 18.43.53.gif)


**Questions for Andy:**
- Do you happen to have a guess at how RoboFont batch can build VFs if FontMake can't? Is it making OTFs, or somehow auto-fixing segments?
- Check that you are trying to build from the correct designspace files.
  -  `sources/Tilt Neon/Rotated/Tilt-Neon.designspace`
  -  `sources/Tilt Prism/Rotated 03 Combined/Tilt-Prism.designspace`
  -  `sources/Tilt Warp/Rotated/Tilt-Warp.designspace`

*(Pause at 6:45)*