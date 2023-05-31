from ipywidgets import widgets
import matplotlib.pyplot as plt

class sliceviewer:
    def __init__(self, image):
        self.image = image
        
        # without plt.ioff() the figure is plotted twice
        plt.ioff()
        self.fig = plt.figure()
        plt.ion()
        self.im = plt.imshow(image[0,:,:], cmap="gray")

        # set up widgets
        self.slider = widgets.IntSlider(value=0, description="slice", min=0, max=image.shape[0])
        self.view = widgets.Dropdown(
            options=[0,1,2],
            description='axis',
            value = 0
        )
    
    def update(self,_):
        axis = self.view.value
        self.slider.max = self.image.shape[axis] - 1

        if(axis == 0):
            img = self.image[self.slider.value,:,:]
        elif(axis == 1):
            img = self.image[:,self.slider.value,:]
        else:
            img = self.image[:,:,self.slider.value]
        self.im.set_data(img)
        self.im.set_clim(img.min(), img.max())
        self.fig.canvas.draw_idle()
    
    def plot(self):
        self.slider.observe(self.update)
        self.view.observe(self.update)
        return widgets.VBox(children=[self.slider, self.view, self.fig.canvas])
