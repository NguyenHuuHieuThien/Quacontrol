import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import urllib.parse
from dash_table.Format import Format, Scheme
from dash.dependencies import Input, Output, State
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
                                html.Div("BẢNG HỢP ĐỒNG PHẢI THU", style={'width':'100%','background': '#FF6633'}),
                                html.A(
                                    children=[
                                        html.I(className="fas fa-file-download")
                                    ],
                                    id='download_detail_HD',
                                    download='HOP_DONG.csv',
                                    target="_blank",
                                    href = '',
                                    className='btn btn-primary',
                                    style={'position':'absolute','top':'0','right':'0','paddingTop':'0','paddingBottom':'0','height': '100%','display': 'inline-grid','alignItems': 'center'}
                                ),
                            ], style={'height': '10%','width':'100%','background': '#e5ecf6','textAlign':'center','display':'inline-grid','alignItems':'center','position':'relative'}),
                            dash_table.DataTable(
                                id='detail_HD',
                                columns=[

                                    {
                                        'name': 'Mã Hợp Đồng', 
                                        'id': 'ma_hd'
                                    },
                                    {
                                        'name': 'Tên Hợp Đồng', 
                                        'id': 'ten_hd'
                                    },
                                    {
                                        'name': 'Mã Khách Hàng', 
                                        'id': 'ma_kh'
                                    },
                                    {
                                        'name': 'Tên Khách Hàng', 
                                        'id': 'ten_kh'
                                    },
                                    {
                                        'name': 'Ngày Hợp Đồng', 
                                        'id': 'ngay_hd'
                                    },
                                    {
                                        'name': 'Giá Trị Hợp Đồng', 
                                        'id': 'tien',
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
                                        'name': 'Tỉ lệ hoàn thiện HĐ (%)', 
                                        'id': 'tl_hthd'
                                    },
                                    {
                                        'name': 'Nợ Còn Lại', 
                                        'id': 'no_cl',
                                        'type': 'numeric',
                                        'format': Format(group=',')
                                    },
                                    {
                                        'name': 'Tỉ Lệ đã thu (%)', 
                                        'id': 'tl_dathu'
                                    },
                                ],
                                style_cell_conditional=[

                                    {
                                        'if': {'column_id': 'ma_hd'},
                                        'width': '9%'
                                    },
                                    {
                                        'if': {'column_id': 'ten_hd'},
                                        'width': '20%'
                                    },
                                    {
                                        'if': {'column_id': 'ma_kh'},
                                        'width': '9%'
                                    },
                                    {
                                        'if': {'column_id': 'ten_kh'},
                                        'width': '22%'
                                    },
                                    {
                                        'if': {'column_id': 'ngay_hd'},
                                        'width': '6%'
                                    },
                                    {
                                        'if': {'column_id': 'tien'},
                                        'width': '8%'
                                    },
                                    {
                                        'if': {'column_id': 'gt_ct'},
                                        'width': '8%'
                                    },
                                    {
                                        'if': {'column_id': 'tl_hthd'},
                                        'width': '3,5%'
                                    },                                
                                    {
                                        'if': {'column_id': 'no_cl'},
                                        'width': '9%'
                                    },
                                    {
                                        'if': {'column_id': 'tl_dathu'},
                                        'width': '3,5%'
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
                                page_current = 0,
                                page_size = 10,
                                page_action = 'native',
                                sort_action = 'native',
                                sort_mode = 'multi',
                                sort_by = [],
                                # page_action = 'none',
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
    [Output("detail_HD", "data"),
     Output("detail_HD", "style_data_conditional")],
    [Input('date', 'start_date'),
     Input('date', 'end_date'),
     Input('ddl_npt_kh', 'value'),
     Input('ddl_npt_hd', 'value'),
     Input('grh_NPT_KH','selectedData'),
     Input('grh_TOP30_KH','selectedData'),
     Input('detail_CT','active_cell')],
    #  Input('ddl_vt', 'value'),
    #  Input('ddl_dgx', 'value'),
    #  Input('ddl_dx', 'value'),
    #  Input('ddl_mauxe', 'value'),
    #  Input('warehouse_date','date'),
    #  Input('grh_GiaTri_KhoXe','selectedData'),
    #  Input('grh_SL_MAUXE','selectedData'),
    #  Input('grh_TiLeXe_Kho','clickData'),
    #  Input('detail_XE_MAUXE','active_cell')],
    [State('detail_CT','data')]
)
def UPDATE_HD(start_date,end_date,ddl_npt_kh,ddl_npt_hd,grh_NPT_KH, grh_TOP30_KH, active_cell,detail_CT):
    ctx = dash.callback_context
    datatable = {'detail_CT':detail_CT}
    label, value = GParams.Get_Value(ctx,datatable)
    print(label, value)
    # ddl_dvcs = ('').join([ddl_dvcs[:4],'.01']) if ddl_dvcs != None else None
    df = DB_PThu.GET_PHAI_THU(('CNPThu_Hopdong', start_date, end_date, ddl_npt_kh, ddl_npt_hd, None, label, value, None, None, None))
    
    # if len(df) == 0:
    #     dict(df = {
    #         'ma_hd' : " ",
    #         'ten_hd': " ",
    #         'ten_kh': " ",
    #         'ngay_hd': " ",
    #         'tien': 0.00,
    #         'no_cl': 0.00,
    #         'gt_ct': 0.00
    #     })
    #     print(df)

    sdc =   (
                Graph.data_bars(df, 'tien') +
                [{
                    'if': {'row_index': 'even'},
                    'backgroundColor': '#f9f9f9'
                }]

            )
    print(type(df['tien']))
    return [df.to_dict(orient='records'), sdc]
    # return [df.to_dict(orient='records')]


@app_PHAI_THU.callback(
     Output('download_detail_HD', 'href'),
    [Input('download_detail_HD','n_clicks'),
     Input('detail_HD','data')]
)
def UPDATE_DOWNLOAD_HD(click,data):
    df = pd.DataFrame.from_dict(data)
    if len(df) > 0:
        csv_string = df.to_csv(index=False, encoding='utf-8',header=['Mã Hợp Đồng','Tên Hợp Đồng','Mã Khách Hàng','Tên Khách Hàng','Ngày Hợp Đồng','Giá Trị Hợp Đồng','Giá Trị Chứng Từ','Tỉ lệ hoàn thiện HĐ (%)','Nợ Còn Lại','Tỉ Lệ đã thu(%)'])
        csv_string = "data:text/csv;charset=utf-8,%EF%BB%BF" + urllib.parse.quote(csv_string)
        return csv_string 
    return None