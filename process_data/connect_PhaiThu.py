import pymssql
import pandas as pd
from process_data.connect import Connect_SQLServer

class Data_PHAI_THU(Connect_SQLServer):

    def GET_PHAI_THU(self, params):
        params = self.convert_params(params)
        if params[6] in ("'ten_kh'","'ten_hd'"):
            params[7] = f"N{params[7]}"
        # print(params)
        proc_name = 'EXEC Gop_No_Phai_Thu {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}'.format(*params)
        cursor = self.Call_Procedure(proc_name)
        if params[0] == "'DT_TG_thien'":
            cols = ['ThoiGian', 'Tien']      
        elif params[0] == "'DTTT'":
            cols = ['TG','GT','Loai'] 
        elif params[0] == "'Tien_TG_thien'":
            cols = ['ThoiGian','Tien']        
        elif params[0] == "'dsa_DT_CCSP_BY'":
            cols = ['tk','ten_tk','DoanhThu']
        elif params[0] == "'dsa_DT_CCSP_BY_test'":
            cols = ['tk','ten_tk','DoanhThu']
        elif params[0] == "'dsa_Cn_PTHU_KH_BY'":
            cols = ['ma_kh','ten_kh','ps_no','GT_ps_no','no_ck','GT_no_ck','co_ck','GT_co_ck']
        elif params[0] == "'CNPThu_Hopdong'":
            cols = ['ma_hd','ten_hd','ma_kh','ten_kh', 'ngay_hd', 'tien', 'no_cl', 'gt_ct','tl_dathu','tl_hthd']
        elif params[0] == "'CNPThu_Hoadon'":
            cols = ['ma_hd', 'ma_kh', 'ten_hd', 'ten_kh','so_ct','gt_ct','da_thu','con_lai','so_ngay_qua_han']
        elif params[0] == "'Top30_KH_CNPThu'":
            cols = ['ma_kh', 'ten_kh', 'so_du', 'doi_tien']
        elif params[0] == "'DT_OV_test'":
            cols = ['Tien']
        elif params[0] == "'Tien_OV_NPTHU'":
            cols = ['Tien']
        elif params[0] == "'Tien_OV_NPTHU_test'":
            cols = ['Tien']
        elif params[0] == "'CONLAI_OV_NPTHU_test'":
            cols = ['ConLai']
        elif params[0] == "'DEBT_TG_thien'":
            cols = ['ThoiGian','Tien','text']
        return self.Convert_DataFrame(cursor, cols)
        
    def GET_DDL_NPT(self, params):
        params = self.convert_params(params)
        proc_name = 'EXEC ddl_npt {0}'.format(*params)
        cursor = self.Call_Procedure(proc_name)
        if params[0] in ("'ddl_npt_kh'","'ddl_npt_hd'","'ddl_npt_loai_dt'"):
            cols = ['id', 'Ten']
        else:
            cols = ['Ten']
        return self.Convert_DataFrame(cursor, cols)
