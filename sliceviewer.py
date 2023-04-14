from ipywidgets import interactive, fixed, widgets, interact
import matplotlib.pyplot as plt
import sys

this = sys.modules[__name__]

x_widget = widgets.IntSlider(min=0, max=100)
y_widget = widgets.Dropdown(
    options=[0,1,2],
    description='axis'
)

def update_pos_range(*args):
    x_widget.max = this.shape[y_widget.value] - 1
    

y_widget.observe(update_pos_range, 'value')

def plotter(pos, axis, image):
    if(axis == 0):
        plt.matshow(image[pos,:,:], cmap="gray")
    elif(axis == 1):
        plt.matshow(image[:,pos,:], cmap="gray")
    else:
        plt.matshow(image[:,:,pos], cmap="gray")
    plt.show()

def plot(image):
    this.shape = image.shape
    x_widget.max = this.shape[0] - 1

    return interact(plotter, pos=x_widget, axis=y_widget, image=fixed(image))
