# Advance builds for Google Fonts PR & GitHub releases

*(start at Feb 12, 11:50)*

## Enhanced build, to-do items

- [x] send todo items for descriptions
- [x] send Andy example of subset script
- [x] make recomendation on where to keep descriptions, etc
- [x] write build instructions
- [ ] adjust build script
  - [x] make files with easy file names
  - [x] make woff2
  - [x] merge in update from fix-neon-sparse branch
  - [ ] add in subsetting step
    - [ ] make it tweakable
    - [ ] also include CSS
    - [ ] also include HTML with example?
    - [ ] include basic instructions for use
  - [ ] check back on fontbakery to-dos at sources/mastering-scripts/notes/03-fontbakery-checks/README.md
  - [ ] test whether features are importing correctly
    - [ ] if not, add this step to build
- [ ] Make secondary pull-request script
  - [ ] add `\[HROT,VROT\].ttf` to filenames
  - [ ] create METADATA.pb
  - [ ] copy from main TTF folder, update filenames to GF standard
  - [ ] add any fixes here that you don't want in main build (some TBD)
  - [ ] move files to google/fonts clone, update, have option to push


## Folder structure for `fonts`

```
fonts/
  - googlefonts-api-prep/
    - README.md
    - Tilt-Neon
      - description.html
      - METADATA.pb
      - OFL.txt
      - Tilt-Neon[HROT,VROT].ttf
    - Tilt-Prism
      - description.html
      - METADATA.pb
      - OFL.txt
      - Tilt-Prism[HROT,VROT].ttf
    - Tild-Warp
      - description.html
      - METADATA.pb
      - OFL.txt
      - Tilt-Warp[HROT,VROT].ttf
  - ttf/
    - README.md
    - OFL.txt
    - Tilt-Neon.ttf
    - Tilt-Prism.ttf
    - Tilt-Warm.ttf
  - woff2/
    - OFL.txt
    - README.md
    - Tilt-Neon.woff2
    - Tilt-Prism.woff2
    - Tilt-Warm.woff2
  - subsets
    - README.md      # explain purpose & how-to-use – write at sources/mastering/data/subset-usage.md and copy
    - Tilt-Neon
      - index.html   # very simple example to show glyphs (maybe in a character map?). Include layout CSS here.
      - fonts.css    # provide @font-face CSS
      - fonts
        - Tilt-Neon--latin_basic.woff2
        - Tilt-Neon--latin_ext.woff2
        - Tilt-Neon--vietnamese.woff2
    - Tilt-Prism
      - [repeat from example above]
    - Tilt-Warp
      - [repeat from example above]
```

*(pause at Feb 12, 13:20)*