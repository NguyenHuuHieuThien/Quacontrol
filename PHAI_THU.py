import dash_core_components as dcc
import dash_html_components as html
import datetime
from dash_html_components.Div import Div
from index_string import index_str
from app import app_PHAI_THU
from DB import DB_PThu
from dash.dependencies import Input, Output, State
from layouts.Phai_Thu import OV_DT, OV_DATHU, OV_CONLAI, DDL_NPT, GT_DT_TG, DDL_DATE, GT_CN_CCDT, GT_NPT_TG, GT_NPT_KH, TOP_30KH, DETAIL_CHUNGTU, DETAIL_HOPDONG, GT_CL_TG
                        

app_PHAI_THU.index_string = index_str


def render_layout():

    now = datetime.datetime.today().strftime('%Y-%m-%d')

    layout = html.Div([
        html.Div([
            html.Div([
                OV_DT.gen_layout(),
                OV_DATHU.gen_layout(),
                OV_CONLAI.gen_layout(),
            ],style={'height':'18vh'},className='ele_row m-b-1'),

            html.Br(),
            html.Div([
                html.Div([
                    dcc.DatePickerRange(
                    id='date',
                    day_size = 43,
                    display_format = 'DD/MM/YYYY',
                    clearable=True,
                    start_date_placeholder_text='Ngày bắt đầu',
                    end_date_placeholder_text='Ngày kết thúc',
                    number_of_months_shown=3,
                    minimum_nights=0,
                    start_date_id='start_date',
                    end_date_id='end_date',
                    start_date = min(['20210101']),
                   end_date = max([datetime.datetime.today().strftime('%Y-%m-%d')]),)],className= 'col-6',style={'height': '5vh'}),
                    html.Div([DDL_DATE.gen_layout()],className= 'ele_row m-b-15',style ={'margin':'0' '0' '0' '0'})],
                className='ele_row m-b-15',style = {'height': '100%'}),
         
        
            html.Br(),
            DDL_NPT.gen_layout(),
            html.Div([
                TOP_30KH.gen_layout(),
                GT_CN_CCDT.gen_layout(),
            ],style={'height':'40vh'},className='ele_row m-b-15'),
            html.Br(),
            html.Div([
                GT_NPT_KH.gen_layout(),
            ],style={'height':'40vh'},className='ele_row m-b-15'),
            html.Div([
                GT_CL_TG.gen_layout(),
            ],style={'height':'50%'},className='ele_row m-b-15'),
            html.Div([
               GT_DT_TG.gen_layout(),
            ],style={'height':'50%'},className='ele_row m-b-15'),

            html.Div([
                DETAIL_CHUNGTU.gen_layout()
            ],style={'height':'50%'},className='m-b-15'),

            html.Div([
                DETAIL_HOPDONG.gen_layout()
            ],style={'height':'100%'},className='m-b-15'),

            #  html.Div([
            #     dcc.DatePickerRange(
            #             id='date_DG',
            #             day_size = 42,
            #             display_format = 'DD/MM/YYYY',
            #             clearable=True,
            #             start_date_placeholder_text='Ngày bắt đầu',
            #             end_date_placeholder_text='Ngày kết thúc',
            #             number_of_months_shown=3,
            #             minimum_nights=0,
            #             start_date_id='start_date',
            #             end_date_id='end_date',
            #             start_date = min(df['ngay_giao']).strftime('%Y-%m-%d'),
            #             end_date = max(df['ngay_giao']).strftime('%Y-%m-%d'),)
            # ],className='col',style ={'marginBottom':'10px'}),

            # DDL_XE_DG.gen_layout(),

            # html.Div([
            #     SL_XE_DG.gen_layout(),
            #     DETAIL_XE_DG.gen_layout()
            # ],style={'height':'40vh'},className='ele_row m-b-15'),

            # html.Div([
            #     SL_XE_DG_TG.gen_layout(),
            #     DETAIL_MAU_XE_DG.gen_layout(),
            # ],style={'height':'40vh'},className='ele_row m-b-15'),

        ], className="container-fluid")
    ], className="section__content--p30", style={'backgroundColor': '#e5e5e5'})

    return layout

app_PHAI_THU.layout = render_layout

if __name__ == '__main__':
    app_PHAI_THU.run_server(port=2222, debug=True,host='192.168.21.3')