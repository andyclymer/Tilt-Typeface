# Testing sparse master setup

*(Start at 22:00, feb 2)*

I planned to use suggestions here, from anthrotype: https://github.com/googlefonts/fontmake/issues/607#issuecomment-560443119

> Try to add a "com.github.googlei18n.ufo2ft.featureWriters" key to the sparse UFO's lib.plist containing an empty array of feature writers. This will override the ufo2ft's default list of writers (i.e. KernFeatureWriter and MarkFeatureWriter) for that specific UFO. An empty array means "do not generate any automatic features". Since the sparse UFO will not contain any features.fea of its own, the generated master TTFs will also not contain any OTL tables.

However, the current designspace at `sources/Tilt Neon/Rotated (Sparse master test)` builds with FontMake just fine as-is. ~~I need to ask Andy whether these are actually sparse masters.~~ Actually, it's very obvious that some of them are sparse masters:

![](assets/2020-02-02-22-17-26.png)

So, maybe whatever Andy did to prep these files already is as much as is needed?

*(Pause at 22:18, feb 2)*