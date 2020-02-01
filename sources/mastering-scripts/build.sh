# !/bin/bash

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

outputDir="fonts"
dsName=$(basename "$DS")
fontName=${dsName/".designspace"/""}

timestamp() {
  date +"%Y_%m_%d-%H_%M"
}

date=$(timestamp)

fontmake -m "$DS" -o variable --output-path $outputDir/$fontName--$date.ttf