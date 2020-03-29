# Mastering

First things first, you must have the project on your computer and navigate to it. Replace `<things_in_angle_brackets>` with relevant text.

```bash
cd <path/to/folder/for/font_projects> # Navigate to a folder that you work on type in. This should not be synced to Dropbox, etc, due to UFO sources in the project.
git clone <repo_URL>                  # git clone the URL for this repo
cd Tilt-Typeface                      # Navigate into this repo.
```

The build process is run the production build from the top-level directory of the `Tilt-Typeface`, for ease. It is primarily activated with the `build.sh` script.

### Install dependencies

If you are running the build for the first time, you must first install dependencies, set up a virtual environment, and give the build script permissions to run.

```bash
python3 -m venv ./venv                             # sets up a virtual environment in a folder called venv
source venv/bin/activate                           # activates the venv so installed dependencies are contained within it
pip install -r sources/mastering/requirements.txt  # installs requirements for build
chmod +x sources/build.sh                          # gives build.sh permissions to execute
```

### Build

Change directories so that you're at the root level of this repo, and run the build script —

```bash
sources/build.sh "<path_to_designspace>"
```

**Note:** below are the relevant commands for each of the main fonts:

```bash
sources/build.sh "sources/Tilt Neon/Rotated (Sparse masters)/Tilt-Neon.designspace"  # Tilt Neon
sources/build.sh "sources/Tilt Prism/Rotated 03 Combined/Tilt-Prism.designspace"     # Tilt Prism
sources/build.sh "sources/Tilt Warp/Rotated/Tilt-Warp.designspace"                   # Tilt Warp
```
