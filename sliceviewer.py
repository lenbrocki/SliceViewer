import matplotlib.pyplot as plt
from ipywidgets import interactive, fixed, IntSlider, Dropdown
def update_pos_range(*args):
    pos_widget.max = shape[axis_widget.value] - 1

def update(img, pos=10, axis=0):
    if(axis == 0):
        plt.matshow(img[pos,:,:], cmap="gray")
    elif(axis == 1):
        plt.matshow(img[:,pos,:], cmap="gray")
    else:
        plt.matshow(img[:,:,pos], cmap="gray")
    plt.show()
    
def plot(img):
    shape = img.shape
    axis_default = 0
    pos_widget = IntSlider(min=0, max=shape[axis_default] - 1)
    axis_widget = Dropdown(
        options=[0,1,2],
        value=axis_default,
        description='axis:',
        disabled=False,
    )
    axis_widget.observe(update_pos_range, 'value')
    return interactive(update, pos=pos_widget, axis=axis_widget, img=fixed(img))
