# !/bin/bash

#
# USAGE: 
# 
# create venv
# pip install -r req......
# 
# after giving permission with:
# chmod +x sources/mastering-scripts/build.sh
# 
# run with:
# sources/mastering-scripts/build.sh <designspace path> <--check>
#

set -e
source venv/bin/activate

# use designspace as argument
DS=$1

if [[ -z "$DS" || $DS = "--help" ]] ; then
    echo 'Add relative path to a designspace file, such as:'
    echo 'sources/mastering-scripts/build.sh "sources/Tilt Neon/Rotated/Tilt-Neon.designspace"'
    exit 2
fi

# ---------------------------------------------------------
# FontMake ------------------------------------------------

outputDir="fonts" && mkdir -p $outputDir
dsName=$(basename "$DS")
fontName=${dsName/".designspace"/""}
fontPath=$outputDir/$fontName.ttf

# fontmake -m "$DS" -o variable --output-path $fontPath

# ---------------------------------------------------------
# Make woff2 files ----------------------------------------

mkdir -p fonts/woff2

woff2_compress $fontPath

mv ${fontPath/'.ttf'/'.woff2'} fonts/woff2/$fontName.woff2

# ---------------------------------------------------------
# TODO: Subset for Latin Basic ----------------------------

subsetDir="fonts/subsets/$fontName/fonts"

mkdir -p $subsetDir

## Google Fonts Latin Basic subset
latinBasicFile="$subsetDir/$fontName--latin_basic.woff2"
latinBasicUni="U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
pyftsubset $fontPath --flavor="woff2" --output-file=$latinBasicFile --layout-features='*' --unicodes=$latinBasicUni

## Google Fonts Latin Ext subset
latinExtFile="$subsetDir/$fontName--latin_ext.woff2"
latinExtUni="U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF"
pyftsubset $fontPath --flavor="woff2" --output-file=$latinExtFile --layout-features='*' --unicodes=$latinExtUni

## Google Fonts Vietnamese subset
vietnameseFile="$subsetDir/$fontName--vietnamese.woff2"
vietnameseUni="U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+1EA0-1EF9,U+20AB"
pyftsubset $fontPath --flavor="woff2" --output-file=$vietnameseFile --layout-features='*' --unicodes=$vietnameseUni

__CSS="\
/* Latin Basic, as defined by Google Fonts */
@font-face {
  font-family: '$fontName';
  font-display: swap;
  src: url('/fonts/$latinBasicFile') format('woff2');
  unicode-range: $latinBasicUni;
}

/* Latin extended, for diacritics in font which are not included in Latin Basic */
@font-face {
  font-family: '$fontName';
  font-display: swap;
  src: url('/fonts/$latinExtUni') format('woff2');
  unicode-range: $latinExtUni;
}

/* Vietnamese glyphs not included in Latin Basic */
@font-face {
  font-family: '$fontName';
  font-display: swap;
  src: url('/fonts/$vietnameseFile') format('woff2');
  unicode-range: $vietnameseUni;
}
"

echo "$__CSS" > $outputDir/fonts.css

# ---------------------------------------------------------
# FontBakery ----------------------------------------------
# optional; not necessary to include. Use arg --check or -c to run these
# will work better if done after font is moved into google/fonts ofl sub-dir


check=$2

if [[ $check = "-c" || $check = "--check" ]] ; then
  pip install -U fontbakery # update
  echo 'Running FontBakery on outputs'
  fontbakery check-googlefonts $outputDir/$fontName.ttf --ghmarkdown sources/mastering-scripts/notes/fontbakery-checks/$fontName--$date.checks.md
fi

# TODO (see https://github.com/thundernixon/inter/blob/qa/misc/googlefonts-qa/fix-move-check.sh):
  # rename file in correct format: Tilt-Neon[HROT,VROT].ttf (etc)
  # add fixes/cleanup needed for fontbakery
  # make METADATA.pb
  # move to google/fonts repo and branch (e.g. tilt-neon) to PR
