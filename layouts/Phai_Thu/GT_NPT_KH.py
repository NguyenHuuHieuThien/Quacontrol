import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output, State
from app import app_PHAI_THU
from utils import Graph
from utils import Graph, GParams
from DB import DB_PThu


def gen_layout():
    layout = html.Div([
                html.Div([
                    dcc.Graph(id="grh_NPT_KH", style={'width': '100%', 'height': '100%'})
                ],className='au-card' ,style={'width': '100%', 'height': '100%'}),
                html.Div([
                    dcc.RangeSlider(
                        id = "slider_grh_NPT_KH",
                        min=1,
                        max=112,
                        value=[1,8],
                        # tooltip={'always_visible ':''},
                        marks={
                            20: {'label': '20', 'style': {'color': '#fc6262'}},
                            40: {'label': '40', 'style': {'color': '#fc6262'}},
                            60: {'label': '60', 'style': {'color': '#fc6262'}},
                            100: {'label': '100', 'style': {'color': '#fc6262'}},
                            112: {'label': '112', 'style': {'color': '#fc6262'}}
                        },
                    )  
                ],style={
                    'background':'#e5ecf6', 
                    # 'border': '1px solid #b1154a'
                })
            ], className="col-12" , style={'height':'100%'})

    return layout


@app_PHAI_THU.callback(
    Output("grh_NPT_KH", "figure"),
    [Input('date', 'start_date'),
     Input('date', 'end_date'),
     Input('slider_grh_NPT_KH','value'),
     Input('ddl_npt_kh', 'value'),
     Input('ddl_npt_hd', 'value'),
     Input('grh_TOP30_KH','selectedData'),
     Input('detail_HD','active_cell'),
     Input('detail_CT','active_cell')],
    #  Input('ddl_ten_loai', 'value'),
    #  Input('ddl_ten_mau', 'value'),
    #  Input('date_DG','start_date'),
    #  Input('date_DG','end_date'),
    #  Input('grh_SL_XEDG_TG','selectedData'),
    #  Input('detail_Xe_DG_TG','active_cell'),
    #  Input('detail_MauXe_DG','active_cell'),],
    # [State('detail_Xe_DG_TG','data'),
    #  State('detail_MauXe_DG','data')]
    [State('detail_HD','data'),
     State('detail_CT','data')]
)
def UPDATE_NPT_KH(start_date,end_date,slider_grh_NPT_KH,ddl_npt_kh,ddl_npt_hd,grh_TOP30_KH,active_cell_hd,active_cell_ct,detail_HD,detail_CT):
    ctx = dash.callback_context
    datatable = {'detail_HD':detail_HD,
                 'detail_CT':detail_CT }
    label, value = GParams.Get_Value(ctx,datatable)
    # print(label, value)
    # datatable = {'detail_Xe_DG_TG':data_XEDG_TG,
    #               'detail_MauXe_DG':data_MauXE_DG}
    # label, value = GParams.Get_Value(ctx,datatable)
    df = DB_PThu.GET_PHAI_THU(('dsa_Cn_PTHU_KH_BY',start_date,end_date,ddl_npt_kh,ddl_npt_hd,None,label,value,None,None,None))
    if(len(df) > 0):
        df = df.loc[(slider_grh_NPT_KH[0] - 1):(slider_grh_NPT_KH[1] - 1)]
    else:
        df = DB_PThu.GET_PHAI_THU(('dsa_Cn_PTHU_KH_BY',None,None,ddl_npt_kh,ddl_npt_hd,None,label,value,None,None,None))
    return Graph.grh_StackedBarChart(x = df["ten_kh"], y1 = df["ps_no"],name_1= 'Đã trả',y2=df["no_ck"],name_2='Còn lại',y3=df["co_ck"],name_3='Ứng trước',title = '<b> TÌNH HÌNH CÔNG NỢ PHẢI THU THEO KHÁCH HÀNG <b>',text_1= df["GT_ps_no"],text_2 =df["GT_no_ck"], text_3= df["GT_co_ck"],margin = [20, 35, 60, 35])
