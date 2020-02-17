# Subsetting

**Strategy:**

Adopting basic strategy of Google Fonts subsetting ([example of Roboto subsets](https://fonts.googleapis.com/css?family=Roboto&display=swap)).

## To-do tasks for Andy (probably)

- [ ] do you want to split out currencies further? E.g. make a currency-specific subset? With the current approach, these will be bundled in with the Latin Extended subset

- [ ] determine what glyphs are missing from the "Latin Ext" subset but are present in Tilt (alternatively, Stephen could probably write a script to do this). Update the following line in `build.sh`:

```
latinExtUni="U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF"
```

- [ ] Are there any layout features you are willing to drop? If so, please update `build.sh` to remove them. From the `pyftsubset` docs:

```
  --layout-features[+|-]=<feature>[,<feature>...]
      Specify (=), add to (+=) or exclude from (-=) the comma-separated
      set of OpenType layout feature tags that will be preserved.
      Glyph variants used by the preserved features are added to the
      specified subset glyph set. By default, 'calt', 'ccmp', 'clig', 'curs',
      'dnom', 'frac', 'kern', 'liga', 'locl', 'mark', 'mkmk', 'numr', 'rclt',
      'rlig', 'rvrn', and all features required for script shaping are
      preserved. To see the full list, try '--layout-features=?'.
      Use '*' to keep all features.
      Multiple --layout-features options can be provided if necessary.
      Examples:
        --layout-features+=onum,pnum,ss01
            * Keep the default set of features and 'onum', 'pnum', 'ss01'.
        --layout-features-='mark','mkmk'
            * Keep the default set of features but drop 'mark' and 'mkmk'.
        --layout-features='kern'
            * Only keep the 'kern' feature, drop all others.
        --layout-features=''
            * Drop all features.
        --layout-features='*'
            * Keep all features.
        --layout-features+=aalt --layout-features-=vrt2
            * Keep default set of features plus 'aalt', but drop 'vrt2'.
```

- [ ] Should we add a character map to the `index.html` subset examples? If so, we'll have to come up with a good way to get a string of characters included.