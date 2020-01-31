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

All three styles have been drawn to the “Google Latin Core Plus” character set, leaving out only a handful of fractions and symbols. The “Prism” style has small caps in place of its lowercase letters. The plan for February is to draw an additional collection of arrows and symbols.

## Current status

*As of January 31st, 2020 —*

The principle design of all three styles is complete, and the work on extending the language support from "Google Latin Core" to "Google Latin Expert" is nearly complete. In the next stage, the kerning will be revisited with the new larger character set, and an extended set of symbols, dingbats and arrows will be drawn.

| Neon | |
| :--- | :--- |
| Core character set | The full “Google Latin Expert” character set is nearly complete |
| Drawing quality | All glyphs are in their fully final 3D state, except a few remaining accented glyphs |
| Extended language support | Nearly complete |
| Extended symbols and dingbats | Not yet begun |
| Kerning | Nearly complete, kerning for extended Latin glyphs will be revisited |
| Manufacturing | Not yet begun. File sizes still need to be optimized (most glyphs use more masters than needed) |

| Prism | |
| :--- | :--- |
| Core character set | The full “Google Latin Expert” character set is complete, including small capitals in place of the lowercase |
| Drawing quality | All glyphs are in their fully final 3D state |
| Extended language support | Complete |
| Extended symbols and dingbats | Not yet begun |
| Kerning | Nearly complete, kerning for extended Latin glyphs will be revisited |
| Manufacturing | Not yet begun. File sizes still need to be optimized (most glyphs use more masters than needed) |

| Warp | |
| :--- | :--- |
| Core character set | The full “Google Latin Expert” character set is complete |
| Drawing quality | All glyphs are in their fully final 3D state |
| Extended language support |Complete |
| Extended symbols and dingbats | Not yet begun |
| Kerning | Nearly complete, kerning for extended Latin glyphs will be revisited |
| Manufacturing | Not yet begun |


## Variable Axes

| Axis | Tag | Range | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| Horizontal Rotation | `HROT` | -45 to 45 | 0 | Gives the appearance of horizontal rotation, in degrees |
| Vertical Rotation | `VROT` | -45 to 45 | 0 | Gives the appearance of vertical rotation, in degrees |
