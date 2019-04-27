import dash
import dash_core_components as dcc
import dash_html_components as dhtml


def main():
    app = dash.Dash()

    app.layout = dhtml.Div(
        dhtml.H1(children="Hello World")
    )

    if __name__ == "__main__":
        app.run_server(debug=True)


main()
