# Subsetting

**Strategy:**

Adopting basic strategy of Google Fonts subsetting ([example of Roboto subsets](https://fonts.googleapis.com/css?family=Roboto&display=swap)).
- `Latin Basic` follows unicodes in Roboto Latin Basic
- `Latin Ext` follows unicodes in Roboto Latin Extended (base glyphs also get included), but adds characters that are left out but available in Tilt
- `Vietnamese` follows unicodes in Roboto Vietnamese, but adds in several characters that aren't (because they're in latin-ext), but are required for Vietnamese text if latin-ext isn't called. This duplicates 8 glyphs, but makes it possible for someone to support Vietamese without necessarily including latin-ext.

The `build.sh` script uses `pyftsubset` to create these subsets, then makes folders with the subset fonts, plus starter CSS to provide users the necessary `@font-face` code, and example HTML to allow users to preview the results.

## Questions for Andy

- [ ] **Do you want to split out anything beyond basic, extended, and vietnamese?**

Possibilities I can think of splitting further are:
  - `dlig` symbols from the latin-basic font (more on this below)
  - currencies from the latin-ext font

- [ ] **Are there any glyphs present in Tilt that are missing from the Latin-Basic and Latin-Ext character sets?**

From Roboto, Latin-Ext has the following unicodes:

```
latinExtUni="U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF"
```

I generated a character list of the fonts with `sources/mastering/print-chars-from-font.py`, then used this for example HTML to show how the subset fonts work. Using this approach, I found that using the unicodes from Roboto `latin-ext` left out `№ ™ ← → ↖ ↗ ↘ ↙ ∙ ≈ ≠ ≤ ≥ ⟨ ⟩`. So, I've added these unicodes to the subset, as well.

I've approached this in a way that I belive has pretty solid charset coverage without much duplication of glyphs. Still, you may be able to spot glyphs that might be missing from the subsets. If so, please let me know, and I can add these into the build.sh (you are obviously welcome to edit it, as well, but I'd like to learn if I have a blind spot in this process).

If you add new characters to the fonts, it would probably be worth running  `sources/mastering/print-chars-from-font.py` again, or otherwise updating the HTML examples and latin-ext subset code.

- [ ] **Should we include or exclude accent glyphs?**

Does it make sense to add the following characters to the latin-ext subset? Most don't seem to be included in the latin-ext subset of Roboto, but I'm unsure. I do think that probably, the fonts have most of the diacritics you want them to have, and there are few instances in which people will require composing accents on the web.

```
ʹ ʺ ʾ ʿ ˇ ˈ ˉ ˊ ˋ ˌ ˘ ˙ ˛ ˝ ̀ ́ ̂ ̃ ̄ ̆ ̇ ̈ ̉ ̊ ̋ ̌ ̏ ̑ ̒ ̛ ̣ ̤ ̦ ̧ ̨ ̮ ̱ 
```

If we really should leave these out, we should remove them from the example HTML.

- [ ] **Are there any layout features you are willing to drop, to save space?** 

Relevant excerpt from the `pyftsubset` docs:

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

One candidate for subsetting: discretionary ligatures, for special symbols. Currently, these are going into Latin-Basic, which probably isn't what many users will expect. These could either be put into another font or excluded from the subsets. This connects to the first question, on whether you'd like to split subsets any further.

![](assets/2020-02-17-18-06-44.png)

