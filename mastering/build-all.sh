# Lazy script that will trigger all three fonts to build.
# Assumes that paths to designspace files haven't changed.
#  
# USAGE (on the command line):
#
# chmod +x sources/build-all.sh            # first time: you must give permissions to run
# mastering/build-all.sh

mastering/build.sh "sources/Tilt Neon/Rotated/TiltNeon[HROT,VROT].designspace"                   # Tilt Neon
mastering/build.sh "sources/Tilt Prism/Rotated 03 Combined/TiltPrism[HROT,VROT].designspace"     # Tilt Prism
mastering/build.sh "sources/Tilt Warp/Rotated/TiltWarp[HROT,VROT].designspace"                   # Tilt Warp
