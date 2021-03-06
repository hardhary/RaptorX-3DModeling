import numpy as np
import sys
import os
import cPickle

sys.path.append('../')
import PropertyUtils
from LoadAngleFile import LoadAngleFile

sys.path.append(os.path.join(os.environ['ModelingHome'], 'Common') )
from LoadTPLTGT import load_tpl as LoadTPL

from GenPropertyFeaturesFromTPL import LoadTrainData4Properties

## this script file generates training data from TPL files and Yujuan's angle files

def Usage():
	print 'python BatchGenPropertyFeaturesFromTPL.py proteinListFile tpl_dir angle_dir'
	print '	tpl_dir: the tpl dir for tpl files generated for template-based modeling'
	print '	angle_dir: the directory for angle files generated by Yujuan'


def main(argv):

	if len(argv) < 3:
		Usage()
		exit(-1)

	proteinListFile = argv[0]
	tplDir = argv[1]
	angDir = argv[2]

	fh = open(proteinListFile, 'r')
	names = [ line.strip() for line in list(fh) ]
	fh.close()

	proteins = []
	for name in names:
		tplFile = os.path.join(tplDir, name + '.tpl')
		angFile = os.path.join(angDir, name + '.ang')

		protein = LoadTrainData4Properties(tplFile, angFile)
		proteins.append(protein)

	savefile = os.path.basename(proteinListFile).split('.')[0] + '.' + os.getpid() + '.propertyFeatures.pkl'
	fh = open(savefile, 'wb')
	cPickle.dump( proteins, fh, protocol=cPickle.HIGHEST_PROTOCOL)
	fh.close()

if __name__ == "__main__":
        main(sys.argv[1:])

