# Subsetting

**Strategy:**

Adopting basic strategy of Google Fonts subsetting ([example of Roboto subsets](https://fonts.googleapis.com/css?family=Roboto&display=swap)).
- `Latin Basic` follows unicodes in Roboto Latin Basic
- `Latin Ext` follows unicodes in Roboto Latin Extended (base glyphs also get included), but adds characters that are left out but available in Tilt
- `Vietnamese` follows unicodes in Roboto Vietnamese, but adds in several characters that aren't (because they're in latin-ext), but are required for Vietnamese text if latin-ext isn't called. This duplicates 8 glyphs, but makes it possible for someone to support Vietamese without necessarily including latin-ext.

The `build.sh` script uses `pyftsubset` to create these subsets, then makes folders with the subset fonts, plus starter CSS to provide users the necessary `@font-face` code, and example HTML to allow users to preview the results.

## Questions for Andy

- [ ] Do you want to split out currencies (or anything else) out further than the latin-ext font (e.g. make a currency-specific subset)? With the current approach, these are bundled in with the Latin Extended subset.

- [ ] Determine: are there any glyphs present in Tilt that are missing from the Latin-Basic and Latin-Ext character sets?

From Roboto, Latin-Ext has the following unicodes:

```
latinExtUni="U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF"
```

However, only using the unicodes above left out `№ ™ ← → ↖ ↗ ↘ ↙ ∙ ≈ ≠ ≤ ≥ ⟨ ⟩`. So, I've added these unicodes to the subset, as well.

Does it make sense to add the following characters to the latin-ext subset? Most don't seem to be included in the latin-ext subset of Roboto, but I'm unsure. I do think that probably, the fonts have most of the diacritics you want them to have, and there are few instances in which people will require composing accents on the web.

```
ʹ ʺ ʾ ʿ ˇ ˈ ˉ ˊ ˋ ˌ ˘ ˙ ˛ ˝ ̀ ́ ̂ ̃ ̄ ̆ ̇ ̈ ̉ ̊ ̋ ̌ ̏ ̑ ̒ ̛ ̣ ̤ ̦ ̧ ̨ ̮ ̱ 
```

If we really should leave these out, we should remove them from the example HTML.

- [ ] Are there any layout features you are willing to drop, to save space? If so, please update `build.sh` to remove them or ask me to do it and I can. From the `pyftsubset` docs:

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
