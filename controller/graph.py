
# ------------------------------------------------------------------------------------------------------------
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import random

class gen_graph:

    def __init__(self):
        colors = {
            'background': '#F0FFFF'
        }

        self.layout = {
            'plot_bgcolor': colors['background'],
            'paper_bgcolor': colors['background'],
            'showgrid': 'False',
            'showline': 'False',
            'clickmode': 'event+select',
            'yaxis': {'fixedrange': True},
            'xaxis' : {'fixedrange': True},
        }

    def gen_color(self, number_colors):        
        '''Generator random color'''
        color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                    for i in range(number_colors)]
        return color

    def maker_color(self,categorize,color,data_y):
        len_data = len(data_y)
        if categorize == 'color':
            maker_color = [color,]*len_data
        elif categorize == 'auto':
            maker_color = self.gen_color(len_data)
        elif categorize == 'emphasize': #emphasize : nhấn mạnh
            maker_color = []
            for i in range(len_data):
                if data_y[i] < 0:
                    maker_color.append('#FF0000')
                else:
                    maker_color.append(color)
        else: maker_color = None
        return maker_color

    def data_bars(self, df, column):
        '''Create Data Bars in Datatable'''
        df[column] = round(df[column].astype('float'),3)
        n_bins = 100
        bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
        ranges = [
            ((df[column].max() - df[column].min()) * i) + df[column].min()
            for i in bounds
        ]
        styles = []
        for i in range(1, len(bounds)):
            min_bound = ranges[i - 1]
            max_bound = ranges[i]
            max_bound_percentage = bounds[i] * 100
            styles.append({
                'if': {
                    'filter_query': (
                        '{{{column}}} >= {min_bound}' +
                        (' && {{{column}}} < {max_bound}' if (i < len(bounds) - 1) else '')
                    ).format(column=column, min_bound=min_bound, max_bound=max_bound),
                    'column_id': column
                },
                'background': (
                    """
                        linear-gradient(90deg,
                        #5ed357 0%,
                        #5ed357 {max_bound_percentage}%,
                        white {max_bound_percentage}%,
                        white 100%)
                    """.format(max_bound_percentage=max_bound_percentage)
                ),
                'paddingBottom': 2,
                'paddingTop': 2
            })

        return styles

    def grh_BarChart(self, x, y, text=None,label_x = None, label_y = None,label_color = None, marker_color=[None,None], width = None , orientation='v', title=None, size_title=13, margin=[5, 5, 5, 5]):
        '''Create bar chart'''
        l = len(x)
        
        data = [
            go.Bar(
                x = x, 
                y = y,
                text = y if text is None else text,
                textfont=dict(
                    family="nunito",
                    size=15,
                    color = 'black'
                ),
                textposition = 'auto',
                hovertemplate="%{x}: <br>%{y:,.0f}" if orientation == 'v' else "%{x}",
                orientation = orientation,
                marker_color = self.maker_color(marker_color[0],marker_color[1],y),
                width = 0.05*l if l > 1 else 0.1 ,
                name='',
                cliponaxis=False,
            )
        ]

        layout_bar = self.layout.copy()
        layout_bar.update({
            'title': {
                'text':title,
                'font': {
                    'size': size_title
                },
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
        })
        layout_bar.update({'margin':{'t': margin[0],'b':margin[1],'l':margin[2],'r':margin[3]},'labels':{'x':label_x, 'y':label_y, 'color':label_color}})

        return {
            'data': data,
            'layout': layout_bar
        }
    
    def grh_DonutChart(self, values, labels, title=None, size_title=13, margin = [5, 5, 5, 5]):
        '''Create biểu đồ bánh xinh xinh'''
        data = [
            go.Pie(
                values=values,
                labels=labels,
                hole=.3,
                name='',
                hovertemplate="%{label}: <br><b>%{value:,.0f}</b>",
            )
        ]
        
        layout_donut = self.layout.copy()
        layout_donut.update(legend=dict(
            font=dict(size=10),
        ))
        layout_donut.update({'margin':{'t': margin[0],'b':margin[1],'l':margin[2],'r':margin[3]}})
        layout_donut.update({
            'title': {
                'text':title,
                'font': {
                    'size': size_title
                },
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        })

        return {
            'data': data,
            'layout': layout_donut
        }

    def grh_Two_PieC(self, val_1, labels_1, name_1, val_2, labels_2, name_2):
        fig = make_subplots(rows=1, cols=2,
                            specs=[[{'type':'domain'}, {'type':'domain'}]],
                            subplot_titles=[name_1, name_2])
        fig.add_trace(go.Pie(labels=labels_1, values=val_1, name=name_1), 1, 1)
        fig.add_trace(go.Pie(labels=labels_2, values=val_2, name=name_2), 1, 2)

        # Use `hole` to create a donut-like pie chart
        fig.update_traces(hole=.3,
                          hoverinfo="label+value",
                          hovertemplate="%{label}: <br><b>%{value:,.0f}</b>")
        fig.update_layout(margin=dict(t=50, b=20, r=10, l=10),
                          clickmode='event+select',
                          plot_bgcolor='#e5ecf6',
                          paper_bgcolor='#e5ecf6')
        return fig

    def grh_LineChart(self, x, y, mode, text=None, title=None, size_title=13, margin = [5, 5, 5, 5],color=None):
        data = [
            go.Scatter(
                x = x,
                y = y,
                text = y if text is None else text,
                textposition = "top center",
                hovertemplate="%{x}: <b>%{y:,.0f}</b>",
                mode=mode,
                name = '',
                line_color = color,
                cliponaxis=False
            )
        ]

        layout_line = self.layout.copy()
        layout_line.update({
                'title': {
                    'text':title,
                    'font': {
                        'size': size_title
                    },
                    'y': 0.95,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'
                },
                'xaxis': {
                    'tickformat': '%m/%Y'
                }
            })
        layout_line.update({'margin':{'t': margin[0],'b':margin[1],'l':margin[2],'r':margin[3]}})

        
        return {
            'data': data,
            'layout': layout_line
        }

    def grh_Sunburst(self, labels, parents, values, title=None, size_title=13, margin = [5, 5, 5, 5]):
        data = [
            go.Sunburst(
                labels=labels,
                parents=parents,
                values=values,
                branchvalues='total',
                hovertemplate='<b>%{label}:</b> %{value:,.0f}',
                maxdepth=2,
                name=''
            )
        ]

        layout_sb = self.layout.copy()
        layout_sb.update({'margin':{'t': margin[0],'b':margin[1],'l':margin[2],'r':margin[3]}})
        layout_sb.update({
            'title': {
                'text':title,
                'font': {
                    'size': size_title
                },
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        })

        return {
            'data': data,
            'layout': layout_sb
        }


    def grh_Multi_Line(self, data, x, y, legend,label_x = None, label_y = None,label_color = None,title=None, size_title=13, margin = [5, 5, 5, 5]):
        fig = px.line(data, x=x, y=y, color=legend)
        
        fig.update_layout(plot_bgcolor='#e5ecf6',
                          paper_bgcolor='#e5ecf6')
        fig.update_layout({'margin':{'t': margin[0],'b':margin[1],'l':margin[2],'r':margin[3]}})
        fig.update_layout(
            title={
                'text': title,
                'font': {
                    'size': size_title
                },
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            xaxis_title=label_x,
            yaxis_title=label_y,
            legend_title=label_color,

        )
        fig.update_xaxes(
            # dtick="M1",
            tickformat="%d/%m/%Y")

        fig.update_layout({'xaxis': { 'showgrid': True,'fixedrange':True }, 'yaxis': {'showgrid': True,'fixedrange':True}})

        fig.update_layout({'clickmode': 'event+select'})
        mode = "lines+markers"
        for i in range(len(data[legend].unique())):
            fig.data[i].update(mode=mode)
        return fig

    def gen_Bar(self, x, y, text=None, orientation='v', textposition='auto', marker_color = [None,None], name=''):
        l = len(x)
        GB = go.Bar(
                x = x if orientation == 'v' else y, 
                y = y if orientation == 'v' else x,
                text = y if text is None else text,
                textposition = textposition,
                hovertemplate="%{x}: <br>%{y:,.0f}" if orientation == 'v' else "%{x}",
                orientation = orientation,
                marker_color = None if marker_color[0] == None else self.maker_color(marker_color[0],marker_color[1],y),
                name=name,
                cliponaxis=False,
            )
        return GB

    def grh_GroupBarChart(self, x1, y1, name_1, text_1, x2, y2,name_2,text_2,categoryarray,title, font_size=15, barmode = 'group',margin = [5, 5, 5, 5], orientation = 'h'):
        data = [self.gen_Bar(x1, y1, name=name_1, text=text_1,orientation=orientation), self.gen_Bar(x2, y2, name=name_2, text=text_2,orientation=orientation)]

        layout_bar = self.layout.copy()
        layout_bar.update({'margin':{'t': margin[0],'b':margin[1],'l':margin[2],'r':margin[3]}, 'barmode':barmode,'xaxis': {'categoryorder':'array', 'categoryarray':categoryarray}})
        layout_bar.update({
            'title': {
                'text':title,
                'font': {
                    'size': font_size
                },
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        })

        return {
            'data': data,
            'layout': layout_bar
        }
    
    def grh_StackedBarChart(self, x, y1, name_1, y2,name_2, y3, name_3,categoryarray = None,title = None, font_size=15, text_1=None,text_2 = None, text_3= None, barmode = 'stack',margin = [5, 5, 5, 5], orientation = 'v'):
        data = [self.gen_Bar(x, y1, name=name_1, text=text_1,orientation=orientation,marker_color = ['color','#00CC66']), self.gen_Bar(x, y2, name=name_2, text=text_2,orientation=orientation,marker_color = ['color','#FF6633']),self.gen_Bar(x, y3, name=name_3, text=text_3,orientation=orientation)]
        layout_bar = self.layout.copy()
        layout_bar.update({'margin':{'t': margin[0],'b':margin[1],'l':margin[2],'r':margin[3]}, 'barmode':barmode,'xaxis': {'categoryorder':'array', 'categoryarray':categoryarray}})
        layout_bar.update({
            'title': {
                'text':title,
                'font': {
                    'size': font_size
                },
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                
            },
            'xaxis' :{

                'type': 'category',
                'tickangle':75
            }
            
        })

        return {
            'data': data,
            'layout': layout_bar
        }