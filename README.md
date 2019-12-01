# Tilt-Typeface

Tilt is a family of type inspired by the dimensional lettering found in storefront signage, designed by Andy Clymer. It’s comprised of three separate subfamilies of type, drawn in styles that you might find in a storefront — 

- **Tilt Neon**, inspired by the twists and turns of neon signs,
- **Tilt Prism**, taking from prismatic lettering cast or cut in a material), and,
- **Tilt Warp**, which started as a sketch of the peeling vinyl stickers more commonly found today.

![Tilt family overview](/images/Tilt-Family.png?raw=true "Tilt family overview")

All three are based around the same letter model of a sign painter’s geometric sans serif, similar to the typefaces Futura or Avant Garde, but with the kinds of details you might expect when the letter is built up with a brush. 

The three styles are designed and built as variable fonts, however instead of using common axes such as “Weight” and “Width”, these typefaces will allow users to rotate the orientation of their glyphs with “Horizontal Rotation” and “Vertical Rotation” axes. The rotation is limited to ±45° so that the letterforms never rotate past a range of readibility.

![Tilt family overview rotated](/images/Tilt-Family-Rotated.png?raw=true "Tilt family overview, rotated")

Additionally, three companion “Shadow” styles are being built for layering, to give another opportunity for designers to make use of the dimensionality of the letterforms without having to make use of animation.

![Tilt Neon](/images/Neon-Aa-Big.gif?raw=true "Tilt Neon")
![Tilt Prism](/images/Prism-Aa-Big.gif?raw=true "Tilt Prism")
![Tilt Warp](/images/Warp-Aa-Big.gif?raw=true "Tilt Warp")

## Design Scope

All three styles have been drawn to the “Google Latin Core” character set, with plans to expand to “Google Latin Core Plus” along with a wider set of supported languages throughout the month of December. The “Prism” style will have small caps in place of its lowercase letters.

## Current status

*As of November, 2019 —*

The principle design of all three styles and manufacturing of version 1.0 is due to be completed in December, 2019. The current status and next steps are as follows:

| Neon | |
| :--- | :--- |
| Character set | The full “Google Latin Core” character set has been drawn |
| Drawing quality | Caps, lowercase, figures, and most punctuation are fully 3D, a few remaining symbols and punctuation will rotate but aren’t in their final dimensional state |
| Kerning | Very quick first pass is complete |
| Manufacturing | Not yet begun |

| Prism | |
| :--- | :--- |
| Character set | The full “Google Latin Core” character set has been drawn, including small capitals in place of the lowercase |
| Drawing quality | All glyphs are in their fully final 3D state |
| Kerning | Very quick first pass is complete |
| Manufacturing | Not yet begun |

| Warp | |
| :--- | :--- |
| Character set | The full “Google Latin Core” character set has been drawn |
| Drawing quality | All glyphs are in their fully final 3D state |
| Kerning | Very quick first pass is complete |
| Manufacturing | Not yet begun |


## Variable Axes

| Axis | Tag | Range | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| Horizontal Rotation | `HROT` | -45 to 45 | 0 | Gives the appearance of horizontal rotation, in degrees |
| Vertical Rotation | `VROT` | -45 to 45 | 0 | Gives the appearance of vertical rotation, in degrees |
