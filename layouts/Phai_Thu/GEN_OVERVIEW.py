import dash_html_components as html

def create_card(title,id,color,icon):
    return  html.Div([
                html.Div([
                    html.Div([
                        html.Div([f'{title}'],className='title_below'),
                        html.Div(className='value', id=id),
                    ],className='col-7 content-ov'),
                    html.Div([
                        html.Img(src=f'/static/system_dashboard/images/{icon}')
                    ],className='col-5 icon-ov'),
                ],className='au-card',style={'width':'100%','height': '100%', 'backgroundColor': f'{color}'})
            ],className='col-4 ov')
