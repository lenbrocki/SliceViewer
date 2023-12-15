# SliceViewer
Simple Jupyter widget for viewing slices of 3D images. 
The image is expected to be an array (NumPy array, Torch tensor, ...)
## Requirements
ipywidget, matplotlib
## Usage
Place sliceviewer.py in the same folder as the Jupyter notebook or in a folder visible to PYTHONPATH. Then, in the notebook usage is simple:
```python
from sliceviewer import sliceviewer
%matplotlib widget
g = sliceviewer(img)
g.plot()
```
<img src="https://github.com/lenbrocki/SliceViewer/blob/main/sample_new.gif" width="30%" height="30%"/>
