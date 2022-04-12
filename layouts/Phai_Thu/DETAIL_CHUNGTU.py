import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import urllib.parse
from dash_table.Format import Format, Scheme
from dash.dependencies import Input, Output, State
from flask import app
from static.system_dashboard.css import css_define as css
from utils import GParams, Graph
from app import app_PHAI_THU
from DB import DB_PThu
import pandas as pd

def gen_layout():


    layout = html.Div([
                html.Div([
                        html.Div([
                            html.Div([
                                html.Div("BẢNG CHỨNG TỪ PHẢI THU", style={'width':'100%','background': '#FF6633'}),
                                html.A(
                                    children=[
                                        html.I(className="fas fa-file-download")
                                    ],
                                    id='download_detail_CT',
                                    download='KHO_XE.csv',
                                    target="_blank",
                                    href = '',
                                    className='btn btn-primary',
                                    style={'position':'absolute','top':'0','right':'0','paddingTop':'0','paddingBottom':'0','height': '100%','display': 'inline-grid','alignItems': 'center'}
                                ),
                            ], style={'height': '10%','width':'100%','background': '#e5ecf6','textAlign':'center','display':'inline-grid','alignItems':'center','position':'relative'}),
                            

                          

   
                            dash_table.DataTable(
                                id='detail_CT',
                                columns=[

                                    {
                                        'name': 'Mã Hợp Đồng', 
                                        'id': 'ma_hd'
                                    },
                                    {
                                        'name': 'Mã Khách Hàng', 
                                        'id': 'ma_kh',
                                        'type': 'numeric',
                                        'format': Format(group=',')
                                    },
                                    {
                                        'name': 'Tên Hợp Đồng', 
                                        'id': 'ten_hd'
                                    },
                                    {
                                        'name': 'Tên Khách Hàng', 
                                        'id': 'ten_kh'
                                    },
                                    {
                                        'name': 'Số Chứng Từ', 
                                        'id': 'so_ct',
                                        'type': 'numeric',
                                        'format': Format(group=',')
                                    },
                                    {
                                        'name': 'Giá Trị Chứng Từ', 
                                        'id': 'gt_ct',
                                        'type': 'numeric',
                                        'format': Format(group=',')
                                    },
                                    {
                                        'name': 'Đã Thu', 
                                        'id': 'da_thu',
                                        'type': 'numeric',
                                        'format': Format(group=',')
                                    },
                                    {
                                        'name': 'Còn Lại', 
                                        'id': 'con_lai',
                                        'type': 'numeric',
                                        'format': Format(group=',')
                                    },
                                    {
                                        'name': 'Số Ngày Quá Hạn', 
                                        'id': 'so_ngay_qua_han',
                                        'type': 'numeric',
                                        'format': Format(group=',')
                                    },
                                ],
                                style_cell_conditional=[

                                    {
                                        'if': {'column_id': 'ma_hd'},
                                        'width': '9%'
                                    },
                                    {
                                        'if': {'column_id': 'ma_kh'},
                                        'width': '9%'
                                    },
                                    {
                                        'if': {'column_id': 'ten_hd'},
                                        'width': '20%'
                                    },
                                    {
                                        'if': {'column_id': 'ten_kh'},
                                        'width': '23%'
                                    },
                                    {
                                        'if': {'column_id': 'so_ct'},
                                        'width': '6%'
                                    },
                                    {
                                        'if': {'column_id': 'gt_ct'},
                                        'width': '8%'
                                    },
                                    {
                                        'if': {'column_id': 'da_thu'},
                                        'width': '9%'
                                    },
                                    {
                                        'if': {'column_id': 'con_lai'},
                                        'width': '9%'
                                    },
                                    {
                                        'if': {'column_id': 'so_ngay_qua_han'},
                                        'width': '7%'
                                    }
                                ],
                                css=[
                                        {
                                            'selector': '.dash-fixed-content',
                                            'rule': 'width: 100%;'
                                        }
                                    ],
                                fixed_rows={'headers': True},
                                style_header=css.style_header,
                                style_cell=css.style_cell,
                                # page_action = 'none',
                                page_current = 0,
                                page_size = 10,
                                page_action = 'native',
                                sort_action = 'native',
                                sort_mode = 'multi',
                                sort_by = [],
                                style_table={'height': '90%','width':'100%'},
                                filter_action= 'native',
                                # sort_action="native",
                                # sort_mode="multi",
                                )

                        ], className="au-card",style={'height':'100%'})
                    ], className="col-lg-12",style={'height':'100%'})
            ],className='ele_row',style={'height':'100%'})

    return layout


@app_PHAI_THU.callback(
    [Output("detail_CT", "data"),
     Output("detail_CT", "style_data_conditional")],
    [Input('date', 'start_date'),
     Input('date', 'end_date'),
     Input('ddl_npt_kh', 'value'),
     Input('ddl_npt_hd', 'value'),
     Input('ddl_npt_ct', 'value'),
     Input('grh_NPT_KH','selectedData'),
     Input('grh_TOP30_KH','selectedData'),
     Input('detail_HD','active_cell')],
    #  Input('ddl_vt', 'value'),
    #  Input('ddl_dgx', 'value'),
    #  Input('ddl_dx', 'value'),
    #  Input('ddl_mauxe', 'value'),
    #  Input('warehouse_date','date'),
    #  Input('grh_GiaTri_KhoXe','selectedData'),
    #  Input('grh_SL_MAUXE','selectedData'),
    #  Input('grh_TiLeXe_Kho','clickData'),
    #  Input('detail_XE_MAUXE','active_cell')],
    # [State('detail_XE_MAUXE','data')]
    [State('detail_HD','data')]
)
def UPDATE_CT(start_date,end_date, ddl_npt_kh,ddl_npt_hd,ddl_npt_ct,grh_NPT_KH,grh_TOP30_KH,active_cell,detail_HD):
    ctx = dash.callback_context
    datatable = {'detail_HD':detail_HD}
    label, value = GParams.Get_Value(ctx,datatable)
    print(label, value)
    # ddl_dvcs = ('').join([ddl_dvcs[:4],'.01']) if ddl_dvcs != None else None
    df = DB_PThu.GET_PHAI_THU(('CNPThu_Hoadon',start_date,end_date,ddl_npt_kh,ddl_npt_hd,ddl_npt_ct,label, value,None,None,None))
    sdc =   (
                Graph.data_bars(df, 'con_lai') +
                [{
                    'if': {'row_index': 'even'},
                    'backgroundColor': '#f9f9f9'
                }]+
                [
            {
                'if': {
                    'filter_query': '{{{}}} >= 0'.format(col, value),
                    'column_id': col
                },
                'backgroundColor': '#01DF01',
                'color': 'black'
            } for (col, value) in df.quantile(0.1).iteritems()
        ] +
        [
            {
                'if': {
                    'filter_query': '{{{}}} < 0'.format(col, value),
                    'column_id': col
                },
                'backgroundColor': '#FF4136',
                'color': 'white'
            } for (col, value) in df.quantile(0.5).iteritems()
        ]
            )
    return [df.to_dict(orient='records'), sdc]
    # return [df.to_dict(orient='records')]

@app_PHAI_THU.callback(
     Output('download_detail_CT', 'href'),
    [Input('download_detail_CT','n_clicks'),
     Input('detail_CT','data')]
)
def UPDATE_DOWNLOAD_CT(click,data):
    df = pd.DataFrame.from_dict(data)
    if len(df) > 0:
        csv_string = df.to_csv(index=False, encoding='utf-8',header=['Mã Hợp Đồng','Mã Khách Hàng','Tên Hợp Đồng','Tên Khách Hàng','Số Chứng Từ','Giá Trị Chứng Từ','Đã Thu','Còn Lại','Số Ngày Quá Hạn'])
        csv_string = "data:text/csv;charset=utf-8,%EF%BB%BF" + urllib.parse.quote(csv_string)
        return csv_string 
    return None
