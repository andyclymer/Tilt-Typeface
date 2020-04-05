# Tilt-Typeface

Tilt is a family of type inspired by the dimensional lettering found in storefront signage, designed by Andy Clymer. It’s comprised of three related variable font styles that you might find in a shop window — 

- **Tilt Neon** mimics the construction of neon tube lettering,
- **Tilt Prism** is based on prismatic lettering, cast or cut in a material,
- **Tilt Warp** resembles peeling vinyl stickers.

![Tilt family overview](/images/TiltFamilyOverview.png?raw=true "Tilt family overview")

All three are based around the same letter model of a sign painter’s geometric sans serif, similar to the typefaces Futura or Avant Garde, but with the kinds of details you might expect to see when the letter is built up with a brush. 

The three styles are designed and built as variable fonts. Instead of using variation axes that you would expect to find, such as “Weight” and “Width”, these typefaces allow users to rotate the orientation of their glyphs with “Horizontal Rotation” and “Vertical Rotation” axes. The rotation is limited to ±45° so that the letterforms never rotate past a readable range.

![Tilt Neon](/images/Big-Neon-Abc.gif?raw=true "Tilt Neon")
![Tilt Prism](/images/Big-Prism-Abc.gif?raw=true "Tilt Prism")
![Tilt Warp](/images/Big-Warp-Abc.gif?raw=true "Tilt Warp")

![Tilt Overview](/images/SampleLines.png?raw=true "Tilt Overview")

## Character Set

All three styles have been drawn to the large “Google Latin Plus” character set, with the exception that the extended set of fractions have been left out. This character set includes support for Vietnamese along with Central and Eastern European languages. The “Prism” style has drawn to have small caps in place of its lowercase letters, but otherwise maintains full language support. PDFs showing full glyph overviews can be found in the [Specimen](/specimen) directory of this repo:

- [Tilt-Neon Glyph Overvew.pdf](specimen/Tilt-Neon%20Glyph%20Overview.pdf)
- [Tilt-Prism Glyph Overvew.pdf](specimen/Tilt-Prism%20Glyph%20Overview.pdf)
- [Tilt-Warp Glyph Overvew.pdf](specimen/Tilt-Warp%20Glyph%20Overview.pdf)

## OpenType Features 

The “Stylistic Alternates” OpenType features can substitute in alternate forms of the lowrcase "a", "t" and "u" in the Neon and Warp styles, and all three styles have a set of pictograms and arrows that can be called out with the text replacement “Discretionary Ligatures” feature.

A full outline of the OpenType features can be found in the [OpenType Feature Overview.pdf](specimen/OpenType%20Feature%20Overview.pdf)

![Feature Sample](/images/FeatureSample.png?raw=true "Feature Sample")

## Variable Axes

| Axis | Tag | Range | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| Horizontal Rotation | `HROT` | -45 to 45 | 0 | Horizontal rotation, in degrees |
| Vertical Rotation | `VROT` | -45 to 45 | 0 | Vertical rotation, in degrees |

![Variable Sample](/images/VarSample.png?raw=true "Variable Sample")

## License

The Tilt project is licensed under the [SIL Open Font License v1.1](OFL.txt). This is a free software license that permits you to use the font software under a set of conditions. Please refer to the full text of the license for details about the permissions, conditions, and disclaimers.

