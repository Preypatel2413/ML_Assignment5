# load Violin vs Piano dataset, reshape and save to a new file
from os import listdir
from numpy import asarray
from numpy import save
from keras.utils import load_img
from keras.utils import img_to_array
# define location of dataset
folder = 'Violin_VS_Piano/'
photos, labels = list(), list()
# enumerate files in the directory
for file in listdir(folder):
	# determine class
	output = 0.0
	if file.startswith('Violin'):
		output = 1.0
	# load image
	photo = load_img(folder + file, target_size=(200, 200))
	# convert to numpy array
	photo = img_to_array(photo)
	# store
	photos.append(photo)
	labels.append(output)
# convert to a numpy arrays
photos = asarray(photos)
labels = asarray(labels)
print(photos.shape, labels.shape)
# save the reshaped photos
save('Violin_vs_Piano_photos.npy', photos)
save('Violin_vs_Piano_labels.npy', labels)


# # load and confirm the shape
# from numpy import load
# photos = load('Violin_vs_Piano_photos.npy')
# labels = load('Violin_vs_Piano_labels.npy')
# print(photos.shape, labels.shape)



# organize dataset into a useful structure
from os import makedirs
from os import listdir
from shutil import copyfile
from random import seed
from random import random
# create directories
dataset_home = 'dataset_Violin_vs_Piano/'
subdirs = ['train/', 'test/']
for subdir in subdirs:
	# create label subdirectories
	labeldirs = ['Violin/', 'Piano/']
	for labldir in labeldirs:
		newdir = dataset_home + subdir + labldir
		makedirs(newdir, exist_ok=True)
# seed random number generator
seed(1)
# define ratio of pictures to use for validation
val_ratio = 0.2
# copy training dataset images into subdirectories
src_directory = 'Violin_vs_Piano/'
for file in listdir(src_directory):
	src = src_directory + '/' + file
	dst_dir = 'train/'
	if random() < val_ratio:
		dst_dir = 'test/'
	if file.startswith('Piano'):
		dst = dataset_home + dst_dir + 'Piano/'  + file
		copyfile(src, dst)
	elif file.startswith('Violin'):
		dst = dataset_home + dst_dir + 'Violin/'  + file
		copyfile(src, dst)