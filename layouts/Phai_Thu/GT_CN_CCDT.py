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
                    dcc.Graph(id="grh_GT_CN_CCDT", style={'width': '100%', 'height': '100%'})
                ],className='au-card' ,style={'width': '100%', 'height': '100%'})
            ], className="col-6" , style={'height':'100%'})

    return layout


@app_PHAI_THU.callback(
    Output("grh_GT_CN_CCDT", "figure"),
    [Input('date', 'end_date'),
     Input('ddl_npt_loai_dt', 'value'),
     Input('ddl_npt_kh', 'value'),
     Input('ddl_npt_hd', 'value'),
     Input('ddl_npt_ct', 'value'),
     Input('grh_NPT_KH','selectedData'),
     Input('grh_TOP30_KH','selectedData'),
     Input('detail_HD','active_cell'),
     Input('detail_CT','active_cell')],
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
    [State('detail_HD','data'),
     State('detail_CT','data')]
)
def UPDATE_GT_CN_CCDT(end_date,ddl_npt_loai_dt,ddl_npt_kh,ddl_npt_hd,ddl_npt_ct,grh_NPT_KH,grh_TOP30_KH,active_cell_hd,active_cell_ct,detail_HD,detail_CT):
    ctx = dash.callback_context
    datatable = {'detail_HD':detail_HD,
                 'detail_CT':detail_CT }
    label, value = GParams.Get_Value(ctx,datatable)
    # print(label, value)
    # datatable = {'detail_XE_MAUXE':data_MX,
    #               'detail_KhoXe':data_KHO}
    # label, value = GParams.Get_Value(ctx,datatable)
    # ddl_dvcs = ('').join([ddl_dvcs[:4],'.01']) if ddl_dvcs != None else None
    df = DB_PThu.GET_PHAI_THU(('dsa_DT_CCSP_BY',None,None,ddl_npt_kh,ddl_npt_hd,ddl_npt_ct,label,value,ddl_npt_loai_dt,None,None))
    return Graph.grh_DonutChart(df['DoanhThu'], df['ten_tk'],title='<b> TỈ LỆ THEO LOẠI DOANH THU <b> ', margin = [35, 35, 35, 10])

