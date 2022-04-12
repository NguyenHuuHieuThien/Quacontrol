
import dash
import pandas as pd
import numpy as np
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
                    children=[dcc.Graph(id="gt_dt_day", style={'width': '100%', 'height': '100%'})],
                    style=tab_style, selected_style=tab_selected_style, className = 'col-3'
                ),
                dcc.Tab(
                    label='Tháng',
                    value='Tháng',
                    children = [dcc.Graph(id="gt_dt_month", style={'width': '100%', 'height': '100%'})],
                    style=tab_style, selected_style=tab_selected_style, className = 'col-3'
                ),
                dcc.Tab(
                    label='Quý',
                    value='Quý',
                    children = [dcc.Graph(id="gt_dt_quarter", style={'width': '100%', 'height': '100%'})],
                    style=tab_style, selected_style=tab_selected_style, className = 'col-3'
                ),
                dcc.Tab(
                    label='Năm',
                    value='Năm',
                    children=[dcc.Graph(id="gt_dt_year", style={'width': '100%', 'height': '100%'})],
                    style=tab_style, selected_style=tab_selected_style, className = 'col-3'
                ),]
            , style={'height': '7vh', 'align-items': 'center'}, className = 'row')
        ], className='au-card', style={'width': '100%', 'height': '100%'})
    ], className="col-sm-12", style={'height': '100%'})

    return layout


@app_PHAI_THU.callback(
    Output("gt_dt_day", "figure"),
    Output("gt_dt_month", "figure"),
    Output("gt_dt_quarter", "figure"),
    Output("gt_dt_year", "figure"),
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
    
    df_date = DB_PThu.GET_PHAI_THU(('DTTT', start_date, end_date,  ddl_npt_kh,  ddl_npt_hd,  None,  label , value, None, 'D', None))
    df_month = DB_PThu.GET_PHAI_THU(('DTTT', start_date, end_date ,  ddl_npt_kh,  ddl_npt_hd,  None,  label , value , None, 'M', None))
    df_quarter = DB_PThu.GET_PHAI_THU(('DTTT', start_date, end_date,  ddl_npt_kh,  ddl_npt_hd,  None, label , value , None, 'Q', None))
    df_year = DB_PThu.GET_PHAI_THU(('DTTT', start_date, end_date,  ddl_npt_kh,  ddl_npt_hd,  None,  label , value , None, 'Y', None))
    

    # Thêm các ngày bị thiếu cho các biểu đồ
    # for df in [df_date, df_month, df_year, df_quarter]:
    #     dff = df.groupby('TG').Loai.nunique()
    #     time = list(dff[dff != 2].index)
    #     index = []

    #     for t in time:
    #         for i, k in enumerate(df.TG):
    #             if k == t:
    #                 index.append(i)

    #     type = list(df.iloc[index, :].Loai)
    #     for i, val in enumerate(index):

    #         if type[i] == 'DT':
    #             df.loc[val+0.5] = time[i], 0.0, 'T'

    #         else:
    #             df.loc[val+0.5] = time[i], 0.0, 'DT'


    # df_year.drop(df_year[(df_year['TG'] == 0) | (df_year['TG'] == 1970)].index, inplace=True)
    # df_year = df_year.sort_values(by='TG')

    #  # Tháng/Năm
    # df_month.drop(df_month[df_month['TG'] == '0-0'].index, inplace=True)
    # df_month = df_month.sort_values(by='TG')
    # df_month = df_month.sort_values(by='TG', key=lambda x: pd.to_datetime(x, format='%m-%Y'))

    # df_quarter.drop(df_quarter[df_quarter['TG'] == '0 - Q0'].index, inplace=True)
    # df_quarter = df_quarter.sort_values(by='TG')

    #  # Ngày/Tháng/Năm

    # df_date.drop(df_date[df_date['TG'] == '0-0-0'].index, inplace=True)

    # df_date['TG'] = pd.to_datetime(df_date.TG, format='%d/%m-%Y').dt.date

    # df_date = df_date.sort_values(by='TG')

    # df_date['TG'] = pd.to_datetime(df_date.TG, format='%Y-%m-%d').dt.strftime('%d-%m-%Y')


# Truyền giá trị 0/0/0 vào dataframe trong trường hợp không có giá trị nào trả về
    df_none_date = pd.DataFrame({'TG': ['0-0-0', '0-0-0'], 'GT': [0, 0], 'Loai': ['DT', 'T']})
    df_none_month = pd.DataFrame({'TG': ['0-0-0', '0-0-0'], 'GT': [0, 0], 'Loai': ['DT', 'T']})
    df_none_quarter = pd.DataFrame({'TG': ['0-0-0', '0-0-0'], 'GT': [0, 0], 'Loai': ['DT', 'T']})
    df_none_year = pd.DataFrame({'TG': ['0-0-0', '0-0-0'], 'GT': [0, 0], 'Loai': ['DT', 'T']})
    if df_date.empty:
        df_date = df_none_date
    if df_month.empty:
        df_month = df_none_month
    if df_quarter.empty:
        df_quarter = df_none_quarter
    if df_year.empty:
        df_year = df_none_year
   
    return  Graph.grh_Multi_Line(df_date, 'TG', 'GT',legend='Loai',label_x = 'Thời Gian', label_y = 'Giá Trị', title=f'<b>GIÁ TRỊ DOANH THU VÀ TIỀN THEO NGÀY</b>',size_title=13, margin=[40, 83, 50, 35]),\
            Graph.grh_Multi_Line(df_month,'TG', 'GT',legend='Loai',label_x = 'Thời Gian', label_y = 'Giá Trị', title=f'<b>GIÁ TRỊ DOANH THU VÀ TIỀN THEO THÁNG</b>',size_title=13,  margin=[40, 83, 50, 35]),\
            Graph.grh_Multi_Line(df_quarter, 'TG', 'GT',legend='Loai',label_x = 'Thời Gian', label_y = 'Giá Trị', title=f'<b>GIÁ TRỊ DOANH THU VÀ TIỀNTHEO QUÝ</b>',size_title=13, margin=[40, 83, 50, 35]),\
            Graph.grh_Multi_Line(df_year, 'TG', 'GT',legend='Loai',label_x = 'Thời Gian', label_y = 'Giá Trị', title=f'<b>GIÁ TRỊ DOANH THU VÀ TIỀN THEO NĂM</b>',size_title=13,  margin=[40, 83, 50, 35])


    # print (df_date)
    # return  Graph.thien_line(df_date,x=df_date['thoigian'], y=df_date['doanhthu','tien'], title=f'<b>GIÁ TRỊ DOANH THU VÀ TIỀN THEO NGÀY</b>', margin=[40, 83, 50, 35]),\
    #         Graph.thien_line(df_month,x=df_month['thoigian'], y=df_month['doanhthu','tien'], title=f'<b>GIÁ TRỊ DOANH THU VÀ TIỀN THEO THÁNG</b>', margin=[40, 83, 50, 35]),\
    #         Graph.thien_line(df_quarter,x=df_quarter['thoigian'], y=df_quarter['doanhthu','tien'], title=f'<b>GIÁ TRỊ DOANH THU VÀ TIỀN THEO QUÝ</b>', margin=[40, 83, 50, 35]),\
    #         Graph.thien_line(df_year,x=df_year['thoigian'], y=df_year['doanhthu','tien'], title=f'<b>GIÁ TRỊ DOANH THU VÀ TIỀN THEO NĂM</b>', margin=[40, 83, 50, 35]),\
            # Graph.grh_LineChart(x=df_date['thoigian'], y=df_date['tien'],mode = 'lines+markers', title=f'<b>GIÁ TRỊ DOANH THU VÀ TIỀN THEO NGÀY</b>', margin=[40, 83, 50, 35],color='#60B664'),\
            # Graph.grh_LineChart(x=df_month['thoigian'], y=df_month['tien'],mode = 'lines+markers', title=f'<b>GIÁ TRỊ DOANH THU VÀ TIỀN THEO THÁNG</b>', margin=[40, 83, 50, 35],color='#60B664'),\
            # Graph.grh_LineChart(x=df_quarter['thoigian'], y=df_quarter['tien'],mode = 'lines+markers', title=f'<b>GIÁ TRỊ DOANH THU VÀ TIỀN THEO QUÝ</b>', margin=[40, 83, 50, 35],color='#60B664'),\
            # Graph.grh_LineChart(x=df_year['thoigian'], y=df_year['tien'],mode = 'lines+markers', title=f'<b>GIÁ TRỊ DOANH THU VÀ TIỀN THEO NĂM</b>', margin=[40, 83, 50, 35],color='#60B664'),\
            

               


