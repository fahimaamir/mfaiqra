import numpy as np
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
from collections import defaultdict
#from st_aggrid.shared import getAllColumnProps, getAllGridOptions
#from st_aggrid import getAllColumnProps, getAllGridOptions
from st_aggrid import AgGrid, GridOptionsBuilder

import numpy as np
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
from collections import defaultdict
#from st_aggrid.shared import getAllColumnProps, getAllGridOptions
#from st_aggrid import getAllColumnProps, getAllGridOptions
from st_aggrid import AgGrid, GridOptionsBuilder

import mysql.connector
import datetime
import numpy as np
import os
import streamlit.components.v1 as components
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import numpy as np
import matplotlib.pyplot as plt
import numpy
import streamlit as st
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from st_aggrid import JsCode, AgGrid, GridOptionsBuilder
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, ColumnsAutoSizeMode
from st_aggrid.shared import GridUpdateMode

from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from st_aggrid.shared import ColumnsAutoSizeMode
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')       #서버에서, 화면에 표시하기 위해서 필요
import seaborn as sns
import altair as alt               ##https://altair-viz.github.io/
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

import numpy as np
import streamlit.components.v1 as components
from pivottablejs import pivot_ui
import pandas as pd
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder



import numpy
import streamlit as st
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from st_aggrid.shared import ColumnsAutoSizeMode
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')       #서버에서, 화면에 표시하기 위해서 필요
import seaborn as sns
import altair as alt               ##https://altair-viz.github.io/
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

from collections import defaultdict
from matplotlib.cm import get_cmap
from pivottablejs import pivot_ui
from st_aggrid import AgGrid
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, ColumnsAutoSizeMode
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from st_aggrid import JsCode, AgGrid, GridOptionsBuilder
from st_aggrid.shared import ColumnsAutoSizeMode
from st_aggrid.shared import GridUpdateMode
import altair as alt ##https://altair-viz.github.io/
import datetime
import matplotlib
import matplotlib as mb
import matplotlib.pyplot as plt
import mysql.connector
import numpy
import numpy as np
import os
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st
import streamlit.components.v1 as components
matplotlib.use('Agg') #서버에서, 화면에 표시하기 위해서 필요









st.html("""
    <style>
        .stMainBlockContainer {
            max-width:350rem;
            max-hight:10rem;
        }
    </style>
    """
)


#@st.cache_resource
def load_data():
    url12 = "https://docs.google.com/spreadsheets/d/1j4zRBnAb1nXi4NMMC8NEnEZMBVTW2oje/edit?pli=1&gid=92713901#gid=92713901"
    file_id122 = url12.split("/")[-2]
    path1122 = "https://drive.google.com/uc?export=download&id=" + file_id122
    Bismillha = pd.read_excel(path1122)
    data = Bismillha
    if 'sampledata' not in st.session_state:
        st.session_state.sampledata = data


    return data

data = load_data()

shouldDisplayPivoted = st.checkbox("Pivot data on Reference Date",True)
tab1, tab2, tab3, tab4 , tab5, tab6, tab7,tab8,tab9,tab10,tab11,tab12,tab13 = st.tabs(["View-1", "View-2", "View-3", "View-4", "View-5", "View-6", "View-7", "View-Graph", "View-Groupby", "View-Pivot", "View-Finance", "Data Entery ", "MySql Data "])

with tab1:
    st.title("Muhammad is the Best")
with tab2:
    gb = GridOptionsBuilder()

    gb.configure_default_column(
        resizable=True,
        filterable=True,
        sortable=True,
        editable=False,
    )
    gb.configure_column(
        field="Campus", header_name="Campus", width=80, rowGroup=shouldDisplayPivoted
    )

    gb.configure_column(
        field="Faculty",
        header_name="Faculty",
        flex=1,
        tooltipField="Faculty",
        rowGroup=shouldDisplayPivoted,
        #rowGroup=True if shouldDisplayPivoted else False,
    )
    gb.configure_column(
        field="Career",
        header_name="Career",
        width=110,
        rowGroup=shouldDisplayPivoted,
    )

    #Campus	Faculty	Career	Program	ctype	semister	credithh		
    gb.configure_column(
        field="Program",
        header_name="Program",
        width=150,
        tooltipField="Program",
        rowGroup=shouldDisplayPivoted,
    )
    
    #field="dat32 ReferenceDate",
    #valueGetter="new Date(data.referenceDate).getFullYear()",
    gb.configure_column(
        field="semister",
        header_name="semister",
        #valueGetter="ctype",
        valueGetter="(data.semister)",
        pivot=True,
        hide=True,
    )

    gb.configure_column(
            field="ctype",
            header_name="ctype",
            #valueGetter="ctype",
            valueGetter="(data.ctype)",
            pivot=True,
            hide=True,
        )

    #valueGetter="new Date(data.referenceDate).toLocaleDateString('en-US',options={year:'numeric', month:'2-digit'})",

    gb.configure_column(
        field="credithh",
        #header_name="Volume [MWh]",
        header_name="credithh",
        width=100,
        type=["numericColumn"],
        aggFunc="sum",
        valueFormatter="value.toLocaleString()",
    )

    gb.configure_grid_options(
        tooltipShowDelay=0,
        pivotMode=shouldDisplayPivoted,
    )

    gb.configure_grid_options(
        autoGroupColumnDef=dict(
            minWidth=300, 
            pinned="left", 
            cellRendererParams=dict(suppressCount=True)
        )
    )
    go = gb.build()

    AgGrid(data, gridOptions=go, width =1900 ,height=400)


with tab3:
    gb = GridOptionsBuilder()

    gb.configure_default_column(
        resizable=True,
        filterable=True,
        sortable=True,
        editable=False,
    )
    gb.configure_column(
        field="Campus", header_name="Campus", width=80, rowGroup=shouldDisplayPivoted
    )

    gb.configure_column(
        field="Faculty",
        header_name="Faculty",
        flex=1,
        tooltipField="Faculty",
        rowGroup=shouldDisplayPivoted,
        #rowGroup=True if shouldDisplayPivoted else False,
    )
    gb.configure_column(
        field="Career",
        header_name="Career",
        width=110,
        rowGroup=shouldDisplayPivoted,
    )

    #Campus	Faculty	Career	Program	ctype	semister	credithh		
    gb.configure_column(
        field="Program",
        header_name="Program",
        width=150,
        tooltipField="Program",
        rowGroup=shouldDisplayPivoted,
    )
    gb.configure_column(
        field="ctype",
        header_name="ctype",
        width=150,
        tooltipField="ctype",
        rowGroup=shouldDisplayPivoted,
    )

    #field="dat32 ReferenceDate",
    #valueGetter="new Date(data.referenceDate).getFullYear()",
    gb.configure_column(
        field="semister",
        header_name="semister",
        #valueGetter="ctype",
        valueGetter="(data.semister)",
        pivot=True,
        hide=True,
    )


    #valueGetter="new Date(data.referenceDate).toLocaleDateString('en-US',options={year:'numeric', month:'2-digit'})",

    gb.configure_column(
        field="credithh",
        #header_name="Volume [MWh]",
        header_name="credithh",
        width=100,
        type=["numericColumn"],
        aggFunc="sum",
        valueFormatter="value.toLocaleString()",
    )

    gb.configure_grid_options(
        tooltipShowDelay=0,
        pivotMode=shouldDisplayPivoted,
    )

    gb.configure_grid_options(
        autoGroupColumnDef=dict(
            minWidth=300, 
            pinned="left", 
            cellRendererParams=dict(suppressCount=True)
        )
    )
    go = gb.build()

    AgGrid(data, gridOptions=go, width =1900 ,height=400)


with tab4:
    t = pivot_ui(data)

    with open(t.src) as t:
        components.html(t.read(), width=900, height=1000, scrolling=True)


with tab5:

    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_default_column(
        groupable=True,
        value=True,
        enableRowGroup=True,
        aggFunc='sum'
    )

    # Customize specific column behaviors
    #gb.configure_column('country', header_name="Home Country")
    gb.configure_pagination(enabled=True, paginationPageSize=5)
    #gb.configure_selection(selection_mode="multiple", use_checkbox=True)
    gb.configure_side_bar(filters_panel=True, defaultToolPanel='filters')

    # Build the final option object
    grid_options = gb.build()

    # Render AgGrid
    mfatt = AgGrid(
        data,
        gridOptions=grid_options,
        height=400,
        width='100%',
        allow_unsafe_jscode=True,
            
    #    gridOptions=gridoptions,
        enable_enterprise_modules=True,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
        fit_columns_on_grid_load=False,
     #   header_checkbox_selection_filtered_only=True,
        use_checkbox=True)
        


    st.markdown("### All Possible builder options")
    for p in dir(GridOptionsBuilder):
        if not p.startswith("_"):
            _ = gb.__getattribute__(p)
            #st.write(_)
with tab6:
    st.heaer("Muhammad is the best")
    
    def generate_sales_data():
            """Generate dataset simulating sales data."""
            np.random.seed(42)
            rows = 50

            # Create a more complex dataset
            df = pd.DataFrame({
                'Product ID': range(1, rows + 1),
                'City': np.random.choice(['Karachi', 'Islamabad', 'Quata', 'Pishawar'], rows),
                'Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Sports'], rows),
                'Base Price': np.random.uniform(10, 500, rows).round(2),
                'Quantity Sold': np.random.randint(1, 100, rows),
            })

            return df


    def configure_grid_options(data):
            """Configure advanced grid options with multiple features."""
            gb = GridOptionsBuilder.from_dataframe(data)
            # Configure row grouping and aggregation
            gb.configure_default_column(
                        groupable=True,
                        value=True,
                        enableRowGroup=True,
                        aggFunc='sum'
                    )

                    # Add filter and sort options
            gb.configure_grid_options(
                        enableRangeSelection=True,
                        enableRangeHandle=True,
                        suppressColumnMoveAnimation=False,
                        suppressRowClickSelection=False
                    )
            # Make some columns editable
            #gb.configure_columns(['Base Price', 'Quantity Sold'], editable=True)
            # Add a virtual column (This will be calculated on the client side)
            #gb.configure_column('Total Revenue',valueGetter="Number(data['Base Price']) * Number(data['Quantity Sold'])",            cellRenderer="agAnimateShowChangeCellRenderer",type=["numericColumn"],editable=False,            valueFormatter="x.toLocaleString('en-US', {style: 'currency', currency: 'USD'})"        )
            
            return gb.build()


        # Generate data
#    sales_data = generate_sales_data()
        # Configure grid options
    #grid_options = configure_grid_options(sales_data)
    grid_options = configure_grid_options(data)
    gb = GridOptionsBuilder()
    gb.configure_default_column(
                        groupable=True,
                        value=True,
                        enableRowGroup=True,
                        aggFunc='sum'
                    )

                    # Add filter and sort options
    gb.configure_grid_options(
                        enableRangeSelection=True,
                        enableRangeHandle=True,
                        suppressColumnMoveAnimation=False,
                        suppressRowClickSelection=False)
    gb.build()
        #st.subheader('Interactive Sales Data Grid')
    st.markdown("""
        **Features:**
        - Edit Base Price and Quantity Sold
        - Automatic Total Revenue calculation
        """)
        # AgGrid with custom options
    ag_return = AgGrid(
            data,
            gridOptions=grid_options,
            height=500,
            theme='alpine',
            allow_unsafe_jscode=True,
            fit_columns_on_grid_load=True,
            reload_data=False
        )


