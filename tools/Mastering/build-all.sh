# Lazy script that will trigger all three fonts to build.
# Assumes that paths to designspace files haven't changed.
#  
# USAGE (on the command line):
#
# chmod +x sources/build-all.sh            # first time: you must give permissions to run
# sources/build-all.sh                     # run

tools/mastering/build.sh "sources/Tilt Neon/Rotated/Tilt-Neon.designspace"                   # Tilt Neon
tools/mastering/build.sh "sources/Tilt Prism/Rotated 03 Combined/Tilt-Prism.designspace"     # Tilt Prism
tools/mastering/build.sh "sources/Tilt Warp/Rotated/Tilt-Warp.designspace"                   # Tilt Warp
