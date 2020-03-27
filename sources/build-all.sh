# Lazy script that will trigger all three fonts to build.
# Assumes that paths to designspace files haven't changed.
#  
# USAGE (on the command line):
#
# chmod +x sources/build-all.sh            # first time: you must give permissions to run
# sources/build-all.sh                     # run

sources/build.sh "sources/Tilt Neon/Rotated (Sparse masters)/Tilt-Neon--sparse.designspace"  # Tilt Neon
sources/build.sh "sources/Tilt Prism/Rotated 03 Combined/Tilt-Prism.designspace"     # Tilt Prism
sources/build.sh "sources/Tilt Warp/Rotated/Tilt-Warp.designspace"                   # Tilt Warp
