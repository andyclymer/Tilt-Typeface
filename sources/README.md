# Sources

The main font sources for all three Tilt styles.

## Drawing and Production Workflow Overview

The drawing and production workflow is separated into a few stages, and each stage is split out into is own folder. A typeface is usually drawn in two dimensions, ``(x, y)`` or ``(width, height)``, but at a certain stage the Tilt typefaces also get a ``z`` or ``depth`` position added to each point in the drawing. 

### Model

The process starts by drawing a flat 2D **Model** of the style. This part of the process doesn't require any special tooling or any change to the process that a type designer would be familiar with, including all the way through the steps of spacing and kerning.

### Master 

Once the model is starting to look good, glyphs can be added to a **Master** UFO, where the two-dimensional points will be given a third dimension by using the **3D Projection View** RoboFont extension which can be found in a separate [Tilt-Tool](https://github.com/andyclymer/Tilt-Tool) repo. Documentation for this tool can be found in its own repo.

### Rotated

Once depth has been added to a Master UFO, a build script from the ``/Tools/Build Rotated Sources/`` directory can be run which turns this single Master UFO into either nine or sixteen **Rotated Source** UFOs along with a ``.designSpace`` file to stitch them all together. At this point a variable font can be built that appears to rotate.

After rotating the sources, depending on how much depth was added to the drawings, some styles will need nearly no cleanup and other will need quite a lot of work to look right. The **DesignSpace Preview** tool in the **3D Projection View** extension can be used to navigate through this folder of UFOs for cleanup, and is documented separately.

After rotating, components are to be reapplied with the Glyph Builder extension, and kerning can be imported from the Model font with a script that can be found in this repo.

### Prepare for build

During the design process, names are being set with ``FontInfo.py`` script, and a quick build has been made with RoboFont's Batch extension.

### Production build

Throughout development, any process can be used to generate a variable font from the designSpace document (such a using RoboFont's "Batch" extension), but the final production build tools, and their instructions for use, can be found in the [mastering](../mastering) directory of this repo.

