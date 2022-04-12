import dash
import dash_core_components as dcc
import dash_html_components as html
from app import app_PHAI_THU
from utils import GParams
from DB import DB_PThu
# from dash.exceptions import PreventUpdate

def gen_ddl(id_ddl, placeholder,className):
    data = DB_PThu.GET_DDL_NPT((id_ddl,))
    if id_ddl in ("ddl_npt_kh","ddl_npt_hd","ddl_npt_loai_dt"):
        options = [{'value': data.values[i][0], 'label': data.values[i][1], 'title': data.values[i][1]} for i in range(data.shape[0])]
    else:
        options = [{'value': data.values[i][0], 'label': data.values[i][0], 'title': data.values[i][0]} for i in range(data.shape[0])]
    return  html.Div([
                dcc.Dropdown(
                    id=id_ddl,
                    options = options,
                    placeholder=placeholder,
                )
            ], className=className)

def gen_layout():
    layout= html.Div([
                    gen_ddl('ddl_npt_kh', "Chọn tên khách hàng",'col-6'),
                    gen_ddl('ddl_npt_hd', "Chọn tên hợp đồng",'col-6'),
                    gen_ddl("ddl_npt_ct", "Chọn mã chứng từ",'col-6'),
                    gen_ddl("ddl_npt_loai_dt", "Chọn loại doanh thu",'col-6'),
                    # gen_ddl("ddl_mauxe", "Chọn màu xe",'col-6'),
                ], className="ele_row m-b-15",style={'width':'100%','flexWrap':'wrap'})
    return layout