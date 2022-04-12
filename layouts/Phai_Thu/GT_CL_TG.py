from controller.get_params import Get_Params
import dash
import datetime
import dash_core_components as dcc
import dash_html_components as html 

from dash.dependencies import Input, Output, State
from dash_html_components.Button import Button
from pkg_resources import PathMetadata
from plotly import graph_objs
from app import app_PHAI_THU
from utils import Graph, GParams
from DB import DB_PThu
from dash.dependencies import Input, Output


def gen_layout():
    tab_style = {
        'borderBottom': '1px solid #d6d6d6',
        'color': 'black',
        'background-color': 'white',
        'border-left': '1px solid #E5E5E5',
        'text-align': 'center',
        'padding': '9px 25px'
    }

    tab_selected_style = {
        'border-top': '5px solid #FF3333',
        'backgroundColor': '#006666',
        'color': 'white',
        'fontWeight': 'bold',
        'text-align': 'center',
        'padding': '9px 25px'
    }
    layout = html.Div([
        html.Div([
            dcc.Tabs(
                value='Ngày',
                children = [
                dcc.Tab(
                    label='Ngày',
                    value='Ngày',
                    children=[dcc.Graph(id="gt_day", style={'width': '100%', 'height': '100%'})],
                    style=tab_style, selected_style=tab_selected_style, className = 'col-3'
                ),
                dcc.Tab(
                    label='Tháng',
                    value='Tháng',
                    children = [dcc.Graph(id="gt_month", style={'width': '100%', 'height': '100%'})],
                    style=tab_style, selected_style=tab_selected_style, className = 'col-3'
                ),
                dcc.Tab(
                    label='Quý',
                    value='Quý',
                    children = [dcc.Graph(id="gt_quarter", style={'width': '100%', 'height': '100%'})],
                    style=tab_style, selected_style=tab_selected_style, className = 'col-3'
                ),
                dcc.Tab(
                    label='Năm',
                    value='Năm',
                    children=[dcc.Graph(id="gt_year", style={'width': '100%', 'height': '100%'})],
                    style=tab_style, selected_style=tab_selected_style, className = 'col-3'
                ),]
            , style={'height': '7vh', 'align-items': 'center'}, className = 'row')
        ], className='au-card', style={'width': '100%', 'height': '100%'})
    ], className="col-sm-12 ", style={'height': '100%'})
    # ], className="col-sm-12 col-md-6 col-lg-6 mb-3", style={'height': '100%'})
    return layout


@app_PHAI_THU.callback(
    Output("gt_day", "figure"),
    Output("gt_month", "figure"),
    Output("gt_quarter", "figure"),
    Output("gt_year", "figure"),
    Input('date', 'start_date'),
    Input('date', 'end_date'),
    Input("gt_month", "selectedData"),
    Input("gt_quarter", "selectedData"),
    Input("gt_year", "selectedData"),
    Input("gt_day", "selectedData"),
    Input("grh_TOP30_KH", "clickData"),
    Input("grh_NPT_KH", "clickData"),
    Input("ddl_npt_kh", "value"),
    Input("ddl_npt_hd", "value"),
    Input("detail_CT", 'active_cell'),
    Input("detail_HD", "active_cell"),
    State("detail_CT", "data"),
    State("detail_HD", "data")
    

)
def render_content(start_date,end_date,gt_month,gt_quarter,gt_year,GT_ngay,top_30,npt_kh,ddl_npt_kh,ddl_npt_hd,dt_ct,dt_hd,detail_ct,detail_hd):
    ctx = dash.callback_context
    datatable = {'detail_CT': detail_ct,
                'detail_HD' : detail_hd
                 }
    label, value = GParams.Get_Value(ctx, datatable) 
    print(ddl_npt_kh)

    df_date = DB_PThu.GET_PHAI_THU(('DEBT_TG_thien', start_date, end_date,  ddl_npt_kh,  ddl_npt_hd,  None,  label , value, None, 'D', None))
    df_month = DB_PThu.GET_PHAI_THU(('DEBT_TG_thien', start_date, end_date , ddl_npt_kh,  ddl_npt_hd,  None,  label , value, None, 'M', None))
    df_quarter = DB_PThu.GET_PHAI_THU(('DEBT_TG_thien', start_date, end_date,  ddl_npt_kh,  ddl_npt_hd,  None,  label , value, None, 'Q', None))
    df_year = DB_PThu.GET_PHAI_THU(('DEBT_TG_thien', start_date, end_date,  ddl_npt_kh,  ddl_npt_hd,  None,  label , value, None, 'Y', None))
    print(df_date)
    print(df_month)
    print(df_quarter)
    print(df_year)

    return Graph.grh_BarChart(x=df_date['ThoiGian'], y=df_date['Tien'], text=df_date['text'],label_x='Thời Gian',label_y='Giá trị',marker_color=['emphasize','#00FF66'], title=f'<b>CÔNG NỢ PHẢI THU THEO NGÀY</b>', margin=[40, 83, 50, 35]),\
           Graph.grh_BarChart(x=df_month['ThoiGian'], y=df_month['Tien'],text=df_month['text'],label_x='Thời Gian',label_y='Giá trị',marker_color=['emphasize','#00FF66'],  title=f'<b>CÔNG NỢ PHẢI THU THEO THÁNG</b>', margin=[40, 83, 50, 35]),\
           Graph.grh_BarChart(x=df_quarter['ThoiGian'], y=df_quarter['Tien'],text=df_quarter['text'],label_x='Thời Gian',label_y='Giá trị',marker_color=['emphasize','#00FF66'], title=f'<b>CÔNG NỢ PHẢI THU THEO QUÝ</b>', margin=[40, 83, 50, 35]),\
           Graph.grh_BarChart(x=df_year['ThoiGian'], y=df_year['Tien'],text=df_year['text'],label_x='Thời Gian',label_y='Giá trị',marker_color=['emphasize','#00FF66'], title=f'<b>CÔNG NỢ PHẢI THU THEO NĂM</b>', margin=[40, 83, 50, 35])
    

               


# @app_PHAI_THU.callback(
#     Output("grh_GT_CL", "figure"),
#     # [Input('ddl_npt_kh', 'value'),
#     #  Input('ddl_npt_hd', 'value'),
#     #  Input('ddl_npt_ct', 'value'),
#     #  Input('ddl_npt_loai_dt', 'value'),
#      [Input('start_end_date','date')]
    #  Input('grh_SL_MAUXE','selectedData'),
    #  Input('grh_TiLeXe_Kho','clickData'),
    #  Input('detail_hd','active_cell'),
    #  Input('detail_ct','active_cell'),],
    # [State('detail_XE_MAUXE','data'),
    #  State('detail_KhoXe','data')]

# def UPDATE_DEBT(date):
#     ctx = dash.callback_context
#     # datatable = {'detail_XE_MAUXE':data_MX,
#     #               'detail_KhoXe':data_KHO}
#     # label, value = GParams.Get_Value(ctx,datatable)
#     # ddl_dvcs = ('').join([ddl_dvcs[:4],'.01']) if ddl_dvcs != None else None
#     df = DB_PThu.GET_PHAI_THU(('DEBT_TG_thien',None,None,None,None,None,None,None,None,None,None))
#     return Graph.grh_BarChart(df['ThoiGian'],df['Tien'],label_x='Thời Gian',label_y='Giá trị',title='GIÁ TRỊ CÒN LẠI PHẢI THU', margin = [50, 35, 35, 35])