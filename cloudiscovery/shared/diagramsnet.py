MX_FILE = """<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="2020-09-01T05:47:00.000Z" agent="cloudiscovery" etag="123456" 
    version="13.7.7" type="device">
   <diagram id="123456654321" name="Page-1"><MX_GRAPH></diagram>
</mxfile>
"""

DIAGRAM_HEADER = """<?xml version="1.0" encoding="UTF-8"?>
<mxGraphModel dx="1186" dy="773" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" 
    pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
   <root>
      <mxCell id="0" />
      <mxCell id="1" parent="0" />"""

DIAGRAM_SUFFIX = """
   </root>
</mxGraphModel>"""

CELL_TEMPLATE = (
    """
<mxCell id="zB3y0Dp3mfEUP9Fxs3Er-<CELL_IDX>" value="" style="outlineConnect=0;fontColor=#232F3E;"""
    + "gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;"
    + "verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;"
    + """aspect=fixed;shape=<SHAPE>;resIcon=<RES_ICON>;" vertex="1" parent="1">
   <mxGeometry x="<X>" y="<Y>" width="<W>" height="<H>" as="geometry" />
</mxCell>
"""
)
