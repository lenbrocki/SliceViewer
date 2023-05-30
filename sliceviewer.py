from ipywidgets import widgets
import matplotlib.pyplot as plt
import numpy as np
class sliceviewer:
    def __init__(self, image):
        self.image = image
        plt.ioff()
        self.fig = plt.figure()
        plt.ion()
        # init_arr is needed for plt.imshow() to be properly set up for printing of the image slices
        init_arr = np.zeros(image.shape[1:]).astype(image.dtype)
        init_arr[10,10] = image.max()
        init_arr[20,10] = image.min()
        self.im = plt.imshow(init_arr, cmap="gray")
        # plot first slice on init
        self.im.set_data(self.image[0,:,:])
        self.slider = widgets.IntSlider(value=0, min=0, max=image.shape[0])
        self.view = widgets.Dropdown(
            options=[0,1,2],
            description='axis',
            value = 0
        )
    
    def update(self,_):
        axis = self.view.value
        self.slider.max = self.image.shape[axis] - 1

        if(axis == 0):
            self.im.set_data(self.image[self.slider.value,:,:])
        elif(axis == 1):
            self.im.set_data(self.image[:,self.slider.value,:])
        else:
            self.im.set_data(self.image[:,:,self.slider.value])
        self.fig.canvas.draw_idle()
    
    def plot(self):
        self.slider.observe(self.update)
        self.view.observe(self.update)
        return widgets.VBox(children=[self.slider, self.view, self.fig.canvas])
