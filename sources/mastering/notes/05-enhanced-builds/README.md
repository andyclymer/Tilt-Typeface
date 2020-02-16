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
  - [ ] add in subsetting step
    - [ ] make it tweakable
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
  - self-hosting-subsets
    - [follow example of Google Fonts in CSS for latin-basic, latin-ext, and vietnamese, e.g. at https://fonts.sandbox.google.com/css2?family=Recursive:ital,slnt,wght,CASL,MONO@0..1,-15..0,300..1000,0..1,0..1&display=swap&subset=latin-ext,vietnamese]
```

*(pause at Feb 12, 13:20)*