import pandas as pd
from dash.dependencies import Input, Output #type:ignore
from data_fetcher import fetch_data

def register_callbacks(app):
    @app.callback(
        [Output('time-series-chart', 'figure'),
         Output('data-points', 'children'),
         Output('min-value', 'children'),
         Output('max-value', 'children'),
         Output('avg-value', 'children')],
        [Input('field-dropdown', 'value'),
         Input('start-datetime-input', 'value'),
         Input('end-datetime-input', 'value'),
         Input('threshold-value-input', 'value'),
         Input('threshold-condition', 'value')]
    )
    def update_chart(selected_field, start_datetime, end_datetime, threshold_value, threshold_condition):
        try:
            start_date = pd.to_datetime(start_datetime)
            end_date = pd.to_datetime(end_datetime)
            date_diff = (end_date - start_date).days

            if date_diff > 90:  # time difference of 90 days
                return (
                    {"data": [], "layout": {"title": "Date range exceeds 90 days"}},
                    "-", "-", "-", "-"
                )
        except Exception as e:
            return (
                {"data": [], "layout": {"title": f"Invalid datetime format: {e}"}},
                "-", "-", "-", "-"
            )

        df = fetch_data(selected_field, start_datetime, end_datetime)

        if df.empty or df[selected_field].isnull().all():
            return (
                {"data": [], "layout": {"title": f"No data available for {selected_field}"}},
                "-", "-", "-", "-"
            )

        if threshold_value is not None:
            if threshold_condition == 'above':
                df = df[df[selected_field] > threshold_value]
            elif threshold_condition == 'below':
                df = df[df[selected_field] < threshold_value]

        if df.empty:
            return (
                {"data": [], "layout": {"title": f"No data available for {selected_field} with the selected filter"}},
                "-", "-", "-", "-"
            )

        df = df.sort_values(by='time')

        data_points = len(df)
        min_value = df[selected_field].min()
        max_value = df[selected_field].max()
        avg_value = df[selected_field].mean()

        figure = {
            "data": [
                {"x": df['time'], "y": df[selected_field], "type": "line", "name": selected_field}
            ],
            "layout": {"title": f"{selected_field} vs Time"}
        }

        return figure, str(data_points), f"{min_value:.3f}", f"{max_value:.3f}", f"{avg_value:.3f}"