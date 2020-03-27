"""
	Tag sparse masters for FontMake and remove files that will block them from working.
	(Removes groups.plist, kerning.plist, and features.fea)

	USAGE:

	python <path>/PrepSparseMaster.py -d <path_to_dir_with_sparse_masters>

	NOTE: assumes sparse masters include "SubSource" in their UFO filename.
"""

import fire
import os
import defcon


def prepSparseMaster(dirToPrep):

	# for path in walk dirToPrep:
	for dirName, subdirList, fileList in os.walk(dirToPrep):
		for dir in subdirList:
			if ".ufo" in dir and "SubSource" in dir:
				sparseUfoPath = dirName + "/" + dir
				print(sparseUfoPath)
				
				# remove unneeded files
				try:
					os.remove(sparseUfoPath + '/groups.plist')
				except FileNotFoundError:
					pass
				try:
					os.remove(sparseUfoPath + '/kerning.plist')
				except FileNotFoundError:
					pass
				try:
					os.remove(sparseUfoPath + '/features.fea')
				except FileNotFoundError:
					pass

				# tag UFO as sparse master
				font = defcon.Font(sparseUfoPath)
				font.lib["com.github.googlei18n.ufo2ft.featureWriters"] = []
				font.save()


# note: you must also delete groups.plist and kerning.plist


if __name__ == '__main__':
  fire.Fire(prepSparseMaster)