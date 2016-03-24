# # 1.5 - Stabilization

# In[8]:

# source: http://stackoverflow.com/questions/12729228/simple-efficient-bilinear-interpolation-of-images-in-numpy-and-python
def bilinear_interpolate(im, x, y):
    x = np.asarray(x)
    y = np.asarray(y)

    x0 = np.floor(x).astype(int)
    x1 = x0 + 1
    y0 = np.floor(y).astype(int)
    y1 = y0 + 1

    x0 = np.clip(x0, 0, im.shape[1]-1)
    x1 = np.clip(x1, 0, im.shape[1]-1)
    y0 = np.clip(y0, 0, im.shape[0]-1)
    y1 = np.clip(y1, 0, im.shape[0]-1)

    Ia = im[y0, x0]
    Ib = im[y1, x0]
    Ic = im[y0, x1]
    Id = im[y1, x1]

    wa = (x1-x) * (y1-y)
    wb = (x1-x) * (y-y0)
    wc = (x-x0) * (y1-y)
    wd = (x-x0) * (y-y0)

    # trying to invert
    return 255-(wa*Ia + wb*Ib + wc*Ic + wd*Id)

if __name__ == '__main__':
    path = 'Images/Q1'
    imagelist = []

    for filename in glob.glob(os.path.join(path, '*.bmp')):
        im = cv2.imread(filename)
        fn = filename.split('/')[-1].split('.')[0]
        imagelist.append((fn, im))

    stableds = []
    stableds.append(np.copy(imagelist[0][1]))

    for i in xrange(len(A)):
        A_matrix = A[i]
        stable = np.zeros(imagelist[0][1].shape)
        print imagelist[i+1][0]
        frame = imagelist[i+1][1]

        for (ys, xs) in np.ndindex((stable.shape[0], stable.shape[1])):
            coor = np.array([xs, ys, 1])
            x, y = coor.dot(A_matrix)
            if (x % 1 == 0) and (y % 1 == 0):
                stable[ys, xs] = np.copy(frame[y, x])
            else:
                stable[ys, xs] = np.copy(bilinear_interpolate(frame, x, y).astype('uint8'))
        stableds.append(stable)
        plt.imshow(stable)
        fn = imagelist[i+1][0] + '_stable1.png'
        plt.savefig('Q1/' + fn, dpi=200)
        plt.close()


# In[10]:

get_ipython().magic(u'matplotlib notebook')

print stableds[0][0, 0]
print stableds[1][0, 0]
print stableds[2][0, 0]
print stableds[3][0, 0]
print stableds[4][0, 0]
print stableds[5][0, 0]
print stableds[6][0, 0]

# kick off the animation
ani = animate_tool(stableds, 100, True, 500)
