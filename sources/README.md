# Sources

The main font sources for all three Tilt styles

## Drawing and Production Workflow Overview

The drawing and production workflow is separated into a few steps, and each step is split out into is own folder. A typeface is usually drawn in two dimensions, ``(x, y)`` or ``(width, height)``, but at a certain stage the Tilt typefaces also get a ``z`` or ``depth`` position added to each point in the drawing. 

### Model

Before we get too far, the process starts with drawing a flat 2D **Model** of the style, drawn in the same manor that any other typeface would be drawn. This part of the process doesn't require any special tooling or any change to the process that a type designer would be familiar with, including all the way through the steps of spacing and kerning.

### Master 

However, once the model is starting to look good, glyphs can be added to a **Master** UFO, where the two-dimensional points will be given a third dimension by using the **3D Projection View** RoboFont extension which can be found in a separate ``Tilt-Tool`` repo. Documentation for this tool can be found in its own repo.

### Rotated

Once depth has been added to a Master UFO, a build script from the ``/Tools/Build Rotated Sources/`` directory can be run which turns this single Master UFO into either nine or sixteen **Rotated Source** UFOs along with a ``.designSpace`` file to stitch them all together. At this point a variable font can be built that appears to rotate.

After rotating the sources, some styles will need nearly no cleanup (Warp) and other will need quite a lot of work to look right (Neon). The **DesignSpace Preview** tool in the **3D Projection View** extension can be used to navigate through this folder of UFOs for cleanup, and is documented separately.

After rotating, components are reapplied with the Glyph Builder extension, and kerning is imported from the Model font with a tool that can be found in this repo.

### Build

During the design process, names are being set with ``FontInfo.py`` script, and a quick build has been made with RoboFont's Batch extension.

**Production Build**

First things first, you must have the project on your computer and navigate to it. Replace `<things_in_angle_brackets>` with relevant text.

```bash
cd <path/to/folder/for/font_projects> # Navigate to a folder that you work on type in. This should not be synced to Dropbox, etc, due to UFO sources in the project.
git clone <repo_URL>                  # git clone the URL for this repo
cd Tilt-Typeface                      # Navigate into this repo.
```

The build process is run the production build from the top-level directory of the `Tilt-Typeface`, for ease. It is primarily activated with the `build.sh` script.

0. If you are running the build for the first time, you must first install dependencies, set up a virtual environment, and give the build script permissions to run.

```bash
python3 -m venv ./venv                             # sets up a virtual environment in a folder called venv
source venv/bin/activate                           # activates the venv so installed dependencies are contained within it
pip install -r sources/mastering/requirements.txt  # installs requirements for build
chmod +x sources/build.sh                          # gives build.sh permissions to execute
```

1. Run the build script!

```bash
sources/build.sh "<path_to_designspace>"
```

**Note:** below are the relevant commands for each of the main fonts:

```bash
sources/build.sh "sources/Tilt Neon/Rotated (Sparse masters)/Tilt-Neon.designspace"  # Tilt Neon
sources/build.sh "sources/Tilt Prism/Rotated 03 Combined/Tilt-Prism.designspace"     # Tilt Prism
sources/build.sh "sources/Tilt Warp/Rotated/Tilt-Warp.designspace"                   # Tilt Warp
```
