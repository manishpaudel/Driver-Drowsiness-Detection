import cv2
import numpy as np
import math

def equalizeHist(img):
	with np.errstate(divide='ignore', invalid='ignore'):
		# bgr = np.float32(img)/255

		# b = bgr[:,:,0]
		# g = bgr[:,:,1]
		# r = bgr[:,:,2]
		b,g,r = cv2.split(img)
		b = b/255
		g = g/255
		r = r/255
		print(b)
		print(g)
		print(r)

		#for intensity
		I = np.divide(r+g+b, 3)

		#for saturation
		min = np.minimum(np.minimum(r,g),b)
		S = 1 - ((3/(r+g+b)) * min)

		#for hue
		H = np.copy(r)

		for i in range(0, b.shape[0]):
			for j in range(0, b.shape[1]):
				H[i][j] = 0.5 * ((r[i][j] - g[i][j]) + (r[i][j] - b[i][j])) /  math.sqrt((r[i][j] - g[i][j])**2 + ((r[i][j] - b[i][j]) * (g[i][j] - b[i][j])))
				H[i][j] = math.acos(H[i][j])

				if b[i][j] <= g[i][j]:
					H[i][j] = H[i][j]
				else:
					H[i][j] = ((360 * math.pi) / 180.0) - H[i][j]
		print(H)
	hsi = cv2.merge((H,S,I))
	
	cv2.imwrite("hsi.jpg",hsi)


if __name__ == '__main__':
	img = cv2.imread("sourceImg.jpg")
	equalizeHist(img)