from PIL import Image
import numpy as np
from sklearn.cluster import KMeans


class ImageRead:
    def __init__(self, image, clr):
        img = Image.open(image)  # Load the image using pillow
        img_array = np.array(img)  # create array
        pixels = img_array.reshape(-1, 3)  # Reshape the image to be a list of pixels
        kmeans = KMeans(n_clusters=clr)  # Perform K-Means clustering by input number of dominant color
        kmeans.fit(pixels)  # inputting array into kmeans
        self.dominant_colors = kmeans.cluster_centers_  # Get the dominant colors(list with list of float numbers)

    def convert(self):
        dominant_colors = np.round(self.dominant_colors).astype(int)  # convert to integer(list with list of integer)
        top_10_list = []
        for items in dominant_colors:
            string = ', '.join(map(str, items))  # convert to string(list with list of strings)
            top_10_list.append(string)
        return top_10_list
