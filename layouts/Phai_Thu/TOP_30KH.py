import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output, State
from app import app_PHAI_THU
from utils import Graph, GParams
from DB import DB_PThu



def gen_layout():
    layout =html.Div([
                html.Div([
                    dcc.Graph(id="grh_TOP30_KH", style={'width': '100%', 'height': '100%'})
                ],className='au-card' ,style={'width': '100%', 'height': '100%'}),
            #     dcc.RangeSlider(
            #     id='range_slider_grh_30KH',
            #     min=1,
            #     max=30,
            #     step=1,
            #     value=[2, 28]
            # ),
                html.Div([
                    dcc.RangeSlider(
                        id = "slider_grh_30KH",
                        min=1,
                        max=30,
                        value=[1,5],
                        # tooltip={'always_visible ':''},
                        marks={
                            1: {'label': '1', 'style': {'color': '#fc6262'}},
                            5: {'label': '5'}   ,
                            10: {'label': '10', 'style': {'color': '#fc6262'}},
                            15: {'label': '15'},
                            20: {'label': '20', 'style': {'color': '#fc6262'}},
                            25: {'label': '25'},
                            30: {'label': '30', 'style': {'color': '#fc6262'}}
                        },
                    )  
                ],style={
                    'background':'#e5ecf6', 
                    # 'border': '1px solid #b1154a'
                })
            ], className="col-6" , style={'height':'100%'})

    return layout


@app_PHAI_THU.callback(
    Output("grh_TOP30_KH", "figure"),
    [Input('date', 'end_date'),
     Input('slider_grh_30KH','value')]
    #  Input('ddl_vt', 'value'),
    #  Input('ddl_dgx', 'value'),
    #  Input('ddl_dx', 'value'),
    #  Input('ddl_mauxe', 'value'),
    #  Input('warehouse_date','date'),
    #  Input('grh_SL_MAUXE','selectedData'),
    #  Input('grh_TiLeXe_Kho','clickData'),
    #  Input('detail_XE_MAUXE','active_cell'),
    #  Input('detail_KhoXe','active_cell'),],
    # [State('detail_XE_MAUXE','data'),
    #  State('detail_KhoXe','data')]
)
def UPDATE_TOP30KH(end_date,slider_grh_30KH):
    ctx = dash.callback_context
    # datatable = {'detail_XE_MAUXE':data_MX,
    #               'detail_KhoXe':data_KHO}
    # label, value = GParams.Get_Value(ctx,datatable)
    # ddl_dvcs = ('').join([ddl_dvcs[:4],'.01']) if ddl_dvcs != None else None
    df = DB_PThu.GET_PHAI_THU(('Top30_KH_CNPThu',None,None,None,None,None,None,None,None,None,None))
    df = df.loc[(slider_grh_30KH[0] - 1):(slider_grh_30KH[1] - 1)]
    return Graph.grh_BarChart(x=df['ten_kh'],y=df['so_du'],text=df['doi_tien'],label_x='Tên khách hàng',label_y='Giá trị',marker_color=['color','#FF3333'],title='<b> TOP 30 KHÁCH HÀNG NỢ PHẢI THU <b>', margin = [70, 55, 55, 55])
