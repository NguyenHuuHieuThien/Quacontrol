import dash
import dash_core_components as dcc
import dash_html_components as html
from DB import DB_PThu
from app import app_PHAI_THU
from dash.dependencies import Input, Output, State
from utils import GParams
from static.system_dashboard.css import css_define as css
import pandas as pd
from layouts.Phai_Thu.GEN_OVERVIEW import create_card

def gen_layout():
    
    title = 'TỔNG DOANH THU'
    color = '#FFCC00'
    icon = 'profit.svg'

    layout = create_card(title,'ov_gt',color,icon)
           
    return layout


@app_PHAI_THU.callback(
    Output("ov_gt", "children"),
    [Input('date', 'start_date'),
     Input('date', 'end_date'),
     Input('ddl_npt_kh', 'value'),
     Input('ddl_npt_hd', 'value'),
     Input('ddl_npt_ct', 'value'),
     Input('grh_NPT_KH','selectedData'),
     Input('detail_HD','active_cell'),
     Input('detail_CT','active_cell')],
    # [Input('ddl_dvcs', 'value'),
    #  Input('ddl_vt', 'value'),
    #  Input('ddl_dgx', 'value'),
    #  Input('ddl_dx', 'value'),
    #  Input('ddl_mauxe', 'value'),
    #  Input('warehouse_date','date'),
    #  Input('grh_GiaTri_KhoXe','selectedData'),
    #  Input('grh_SL_MAUXE','selectedData'),
    #  Input('grh_TiLeXe_Kho','clickData'),
    #  Input('detail_XE_MAUXE','active_cell'),
    #  Input('detail_KhoXe','active_cell'),],
    # [State('detail_XE_MAUXE','data'),
    #  State('detail_KhoXe','data')]
    [State('detail_HD','data'),
     State('detail_CT','data')]
)
def UPDATE_OV_DT(start_date,end_date,ddl_npt_kh,ddl_npt_hd,ddl_npt_ct,grh_NPT_KH,active_cell_hd,active_cell_ct,detail_HD,detail_CT):
    ctx = dash.callback_context
    # datatable = {'detail_XE_MAUXE':data_MX,
    #               'detail_KhoXe':data_KHO}
    datatable = {'detail_HD':detail_HD,
                 'detail_CT':detail_CT }
    label, value = GParams.Get_Value(ctx,datatable)
    # ddl_dvcs = ('').join([ddl_dvcs[:4],'.01']) if ddl_dvcs != None else None
    df = DB_PThu.GET_PHAI_THU(('DT_OV_test',start_date,end_date,ddl_npt_kh,ddl_npt_hd,ddl_npt_ct,label,value,None,None,None))
    print (df)
    return df['Tien'].values[0]
    