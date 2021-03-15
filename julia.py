import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import time

# Image width and height; parameters for the plot

tic = time.perf_counter()
#im_width, im_height = 24000, 24000 #This takes 2 hours to run and produces 24k image, increase dpi in savefig up to 5000
im_width, im_height = 4000, 4000
c = complex(-0.1, 0.65)
zabs_max = 10
nit_max = 1000
xmin, xmax = -2, 2
xwidth = xmax - xmin
ymin, ymax = -2, 2
yheight = ymax - ymin

julia = np.zeros((im_width, im_height))
for ix in range(im_width):
    for iy in range(im_height):
        nit = 0
        # Map pixel position to a point in the complex plane
        z = complex(ix / im_width * xwidth + xmin,
                    iy / im_height * yheight + ymin)
        # Do the iterations
        while abs(z) <= zabs_max and nit < nit_max:
            z = z**2 + c
            nit += 1
        shade = 1-np.sqrt(nit / nit_max)
        ratio = nit / nit_max
        julia[ix,iy] = ratio

sns.set()
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.grid(False)
ax.imshow(julia, interpolation='nearest', cmap=cm.hot)
# Set the tick labels to the coordinates of z0 in the complex plane
xtick_labels = np.linspace(xmin, xmax, xwidth * 2 )
ax.set_xticks([(x-xmin) / xwidth * im_width for x in xtick_labels])
ax.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels], color='mediumslateblue')
ytick_labels = np.linspace(ymin, ymax, yheight * 2)
#ax.get_xaxis().set_visible(False)
#ax.get_yaxis().set_visible(False)
plt.title('Julia Set ©Paabes', color='mediumslateblue')
ax.set_yticks([(y-ymin) / yheight * im_height for y in ytick_labels])
ax.set_yticklabels(['{:.1f}'.format(ytick) for ytick in ytick_labels], color='mediumslateblue')
plt.savefig('renders/julia_set.png', dpi=600)
plt.show()

toc = time.perf_counter()
print(f"\nFinished Rendering in {toc - tic:0.4f} seconds")
print(f"\nor {(toc - tic)/60:0.4f} in minutes")