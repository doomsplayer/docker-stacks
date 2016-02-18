from bokeh.plotting import Figure
from bokeh.core.properties import Dict, String, List, Tuple, Instance
from bokeh.models.plots import Plot
from bokeh.core.properties import HasProps

class EnhancedFigure:
    variables = Dict(String, String)
    category = List(String)
    plot = Instance(Plot)

    def __getattr__(self, attrib):
        return getattr(self.plot, attrib)
