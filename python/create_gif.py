import imageio.v3 as iio

#FILL THESE AND MAKE ACTIVE filenames = ['__________', '____________']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

#iio.imwrite('_______', images, duration = 500, loop = 0)