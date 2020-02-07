# !/bin/bash

#
# USAGE: 
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

timestamp() {
  date +"%Y_%m_%d-%H_%M"
}

date=$(timestamp)

fontmake -m "$DS" -o variable --output-path $outputDir/$fontName\[HROT,VROT\].ttf


# ---------------------------------------------------------
# FontBakery ----------------------------------------------
# optional; not necessary to include. Use arg --check or -c to run these
# will work better if done after font is moved into google/fonts ofl sub-dir


check=$2

if [[ $check = "-c" || $check = "--check" ]] ; then
  pip install -U fontbakery # update
  echo 'Running FontBakery on outputs'
  fontbakery check-googlefonts $outputDir/$fontName*HROT*VROT*.ttf --ghmarkdown sources/mastering-scripts/notes/fontbakery-checks/$fontName--$date.checks.md
fi

# TODO (see https://github.com/thundernixon/inter/blob/qa/misc/googlefonts-qa/fix-move-check.sh):
  # rename file in correct format: Tilt-Neon[HROT,VROT].ttf (etc)
  # add fixes/cleanup needed for fontbakery
  # make METADATA.pb
  # move to google/fonts repo and branch (e.g. tilt-neon) to PR
