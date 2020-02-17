# Self-hosting subset fonts

Fonts are subset with the expectation that multiple font files will be used along with the CSS property `unicode-range` to specify unicodes present in each file. This enables a website visitor to download only the fonts needed to display text on a given site.

To support only "Latin Basic" characters, you can use just the `latin_basic` font file. However, to use "Latin Extended" characters, you should use *both* `latin_basic` *and* `latin_ext` font files. For Vietnamese, you must use `latin_basic` *and* `vietnamese` subsets at minimum, but may wish to also use `latin_ext`.

Files are provided along with example CSS to provide an example of how this works.