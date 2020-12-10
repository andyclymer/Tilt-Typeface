# !/bin/bash

#
# USAGE: 
# 
# create venv
# pip install -r req......
# 
# after giving permission with:
# chmod +x mastering/build.sh
# 
# run with:
# mastering/build.sh <designspace path> <--check>
#

set -e
source venv/bin/activate

# use designspace as argument
DS=$1

if [[ -z "$DS" || $DS = "--help" ]] ; then
    echo 'Add relative path to a designspace file, such as:'
    echo 'mastering/build.sh "sources/Tilt Neon/Rotated/Tilt-Neon.designspace"'
    exit 2
fi

# ---------------------------------------------------------
# FontMake ------------------------------------------------

outputDir="fonts"
mkdir -p "fonts/TTF"
dsName=$(basename "$DS")
fontName=${dsName/".designspace"/""}
fontPath="$outputDir/TTF/$fontName.ttf"
stylespacePath=$(dirname "$DS")/Tilt.stylespace
rm -f $fontPath

fontmake -m "$DS" -o variable --output-path $fontPath
statmake --designspace "$DS" --stylespace "$stylespacePath" $fontPath

gftools fix-nonhinting $fontPath $fontPath.fix
mv $fontPath.fix $fontPath
rm $outputDir/TTF/*backup*.ttf
gftools fix-dsig $fontPath -a -f

# # ---------------------------------------------------------
# # Make woff2 files ----------------------------------------

# mkdir -p fonts/WOFF2

# woff2_compress $fontPath

# mv ${fontPath/'.ttf'/'.woff2'} fonts/woff2/$fontName.woff2

# # ---------------------------------------------------------
# # TODO: Subset for Latin Basic ----------------------------

# subsetDir="$outputDir/WOFF2/Subsets/$fontName"

# mkdir -p $subsetDir/fonts

# ## Google Fonts Latin Basic subset
# latinBasicFile="$fontName--latin_basic.woff2"
# latinBasicUni="U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
# arrowsAndIcons="U+2190, U+2196, U+2191, U+2197, U+2192, U+2198, U+2193, U+2199, U+263a, U+2639, U+2661, U+2606, U+1f3b1, U+1f3b3, U+1f511, U+2702, U+1f45e, U+1f4f7, U+1f355, U+1f377, U+1f3b5, U+1f9fa"
# pyftsubset $fontPath --flavor="woff2" --output-file=$subsetDir/fonts/$latinBasicFile --layout-features='*' --unicodes="$latinBasicUni,$arrowsAndIcons"

# ## Google Fonts Latin Ext subset
# latinExtFile="$fontName--latin_ext.woff2"
# latinExtUni="U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF,U+2116,U+2122,U+2190,U+2192,U+2196,U+2197,U+2198,U+2199,U+2219,U+2248,U+2260,U+2264,U+2265,U+27e8,U+27e9"
# pyftsubset $fontPath --flavor="woff2" --output-file=$subsetDir/fonts/$latinExtFile --layout-features='*' --unicodes=$latinExtUni
# # pyftsubset $fontPath --flavor="woff2" --output-file=$subsetDir/fonts/$latinExtFile --layout-features='*' --unicodes-file="sources/mastering/data/latin-ext_unique-glyphs.nam" ### problem: how do we get the appropriate unicode values for the CSS?

# # sources/mastering/data/latin-ext_unique-glyphs.nam

# ## Google Fonts Vietnamese subset
# vietnameseFile="$fontName--vietnamese.woff2"
# vietnameseUni="U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+1EA0-1EF9,U+20AB"
# pyftsubset $fontPath --flavor="woff2" --output-file=$subsetDir/fonts/$vietnameseFile --layout-features='*' --unicodes=$vietnameseUni

# __CSS="\
# /* Latin Basic, as defined by Google Fonts */
# @font-face {
#   font-family: '$fontName';
#   font-display: swap;
#   src: url('fonts/$latinBasicFile') format('woff2');
#   unicode-range: $latinBasicUni;
# }

# /* Latin extended, for diacritics in font which are not included in Latin Basic */
# @font-face {
#   font-family: '$fontName';
#   font-display: swap;
#   src: url('fonts/$latinExtFile') format('woff2');
#   unicode-range: $latinExtUni;
# }

# /* Vietnamese glyphs not included in Latin Basic */
# @font-face {
#   font-family: '$fontName';
#   font-display: swap;
#   src: url('fonts/$vietnameseFile') format('woff2');
#   unicode-range: $vietnameseUni;
# }
# "

# # the string of characters is generated via sources/mastering/print-chars-from-font.py, then copied in
# __HTML="\
# <!DOCTYPE html>
# <html lang='en'>
# 	<head>
# 		<meta charset='UTF-8'>
# 		<meta name='viewport' content='width=device-width, initial-scale=1.0'>
# 		<title>$fontName Subset</title>
# 		<link rel='stylesheet' href='fonts.css'>
# 		<style>
# 			* {
# 				font-family: $fontName, sans-serif;
# 				font-weight: 400;
# 			}
# 			p {
# 				font-size: 24px;
# 				word-break: break-all;
# 				line-height: 1.75;
# 				letter-spacing: 0.3em;
# 			}
# 		</style>
# 	</head>
# 	<body>
# 		<h1>
# 			$fontName
# 		</h1>
# 		<p>
# 			! \" # $ % & \' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \\ ] ^ _ \` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~   ¡ ¢ £ ¤ ¥ ¦ § ¨ © ª « ¬ ­ ® ¯ ° ± ² ³ ´ µ ¶ · ¸ ¹ º » ¼ ½ ¾ ¿ À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï Ð Ñ Ò Ó Ô Õ Ö × Ø Ù Ú Û Ü Ý Þ ß à á â ã ä å æ ç è é ê ë ì í î ï ð ñ ò ó ô õ ö ÷ ø ù ú û ü ý þ ÿ Ā ā Ă ă Ą Ć ć Ĉ ĉ Ċ ċ Č č Ď ď Đ Ē ē Ĕ ĕ Ė ė Ę ę Ě ě Ĝ ĝ Ğ ğ Ġ ġ Ģ ģ Ĥ ĥ Ĩ ĩ Ī ī Ĭ ĭ İ ı Ĵ ĵ Ķ ķ Ĺ ĺ Ļ ļ Ľ ľ Ń ń Ņ ņ Ň ň Ō ō Ŏ ŏ Ő ő Œ œ Ŕ ŕ Ŗ ŗ Ř ř Ś ś Ŝ ŝ Ş ş Š š Ţ ţ Ť ť Ũ ũ Ū ū Ŭ ŭ Ů ů Ű ű Ŵ ŵ Ŷ ŷ Ÿ Ź ź Ż ż Ž ž ƒ Ơ ơ Ư ư Ǆ ǅ ǆ Ǉ ǈ ǉ Ǌ ǋ ǌ Ǧ ǧ Ǻ ǻ Ǽ ǽ Ǿ ǿ Ȁ ȁ Ȃ ȃ Ȅ ȅ Ȇ ȇ Ȉ ȉ Ȋ ȋ Ȍ ȍ Ȏ ȏ Ȑ ȑ Ȓ ȓ Ȕ ȕ Ȗ ȗ Ș ș Ț ț Ȩ ȩ Ȫ ȫ Ȭ ȭ Ȱ ȱ Ȳ ȳ ʹ ʺ ʻ ʼ ʾ ʿ ˆ ˇ ˈ ˉ ˊ ˋ ˌ ˘ ˙ ˚ ˛ ˜ ˝ ̀ ́ ̂ ̃ ̄ ̆ ̇ ̈ ̉ ̊ ̋ ̌ ̏ ̑ ̒ ̛ ̣ ̤ ̦ ̧ ̨ ̮ ̱ Ḉ ḉ Ḍ ḍ Ḏ ḏ Ḕ ḕ Ḗ ḗ Ḝ ḝ Ḡ ḡ Ḥ ḥ Ḫ ḫ Ḯ ḯ Ḷ ḷ Ḻ ḻ Ṃ ṃ Ṅ ṅ Ṇ ṇ Ṉ ṉ Ṍ ṍ Ṏ ṏ Ṑ ṑ Ṓ ṓ Ṛ ṛ Ṟ ṟ Ṡ ṡ Ṣ ṣ Ṥ ṥ Ṧ ṧ Ṩ ṩ Ṭ ṭ Ṯ ṯ Ṹ ṹ Ṻ ṻ Ẁ ẁ Ẃ ẃ Ẅ ẅ Ẏ ẏ Ẓ ẓ ẗ Ạ ạ Ả ả Ấ ấ Ầ ầ Ẩ ẩ Ẫ ẫ Ậ ậ Ắ ắ Ằ ằ Ẳ ẳ Ẵ ẵ Ặ ặ Ẹ ẹ Ẻ ẻ Ẽ ẽ Ế ế Ề ề Ể ể Ễ ễ Ệ ệ Ỉ ỉ Ị ị Ọ ọ Ỏ ỏ Ố ố Ồ ồ Ổ ổ Ỗ ỗ Ộ ộ Ớ ớ Ờ ờ Ở ở Ỡ ỡ Ợ ợ Ụ ụ Ủ ủ Ứ ứ Ừ ừ Ử ử Ữ ữ Ự ự Ỳ ỳ Ỵ ỵ Ỷ ỷ Ỹ ỹ         ​ ‐ ‒ – — ― ‘ ’ ‚ “ ” „ † ‡ • … ‰ ′ ″ ‹ › ⁄ ⁒ ⁴ ₡ ₣ ₤ ₦ ₧ ₩ ₫ € ₭ ₱ ₲ ₵ ₹ ₺ ₼ ₽ № ™ ← ↑ → ↓ ↖ ↗ ↘ ↙ − ∕ ∙ ≈ ≠ ≤ ≥ ⟨ ⟩
# 		</p>
# 	</body>
# </html>
# "

# echo "$__CSS" > $subsetDir/fonts.css
# echo "$__HTML" > $subsetDir/index.html
# cp -f mastering/data/subset-usage.md fonts/subsets/README.md

# # ---------------------------------------------------------
# # FontBakery ----------------------------------------------
# # optional; not necessary to include. Use arg --check or -c to run these
# # will work better if done after font is moved into google/fonts ofl sub-dir


# check=$2

# if [[ $check = "-c" || $check = "--check" ]] ; then
#   pip install -U fontbakery # update
#   echo 'Running FontBakery on outputs'
#   fontbakery check-googlefonts $outputDir/$fontName.ttf --ghmarkdown mastering/notes/fontbakery-checks/$fontName--$date.checks.md
# fi

# # TODO: make "deploy to GF" script (see https://github.com/thundernixon/inter/blob/qa/misc/googlefonts-qa/fix-move-check.sh):
#   # rename file in correct format: Tilt-Neon[HROT,VROT].ttf (etc)
#   # add fixes/cleanup needed for fontbakery
#   # make METADATA.pb
#   # move to google/fonts repo and branch (e.g. tilt-neon) to PR
