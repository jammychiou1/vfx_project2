import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from PIL import Image
import msop
import motion
def displacement(filenames,focal_length):
	displace = [np.asarray([0,0])]
	for i in range(len(filenames) - 1):
		im = Image.open(filenames[i])
		arr = np.asarray(im)
		deltay, deltax = motion.get_model(msop.msop(filenames[i]), msop.msop(filenames[i+1]), arr.shape[1], arr.shape[0], focal_length)
		deltax = -deltax
		deltax += displacement[-1][0]
		deltay += displacement[-1][1]
		displace.append(np.asarray([deltax, deltay]))
	im = Image.open(filenames[-1])
	arr = np.asarray(im)
	deltax, deltay = motion.get_model(msop.msop(filenames[-1]), msop.msop(filenames[0]), arr.shape[1], arr.shape[0])
	deltax += displacement[-1][0]
	deltay += displacement[-1][1]
	displace.append(np.asarray([deltax, deltay]))
	displace = np.asarray(displace)
	return displace