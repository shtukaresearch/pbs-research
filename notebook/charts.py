import marimo

__generated_with = "0.12.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import scipy.stats as stats
    import altair as alt
    return alt, np, pd, stats


@app.cell
def _(np):
    rng = np.random.default_rng()
    return (rng,)


@app.cell
def _(np, pd, stats):
    index = np.arange(0,15,0.01)

    def npdf(loc, scale) -> pd.Series:
        return stats.norm(loc=loc, scale=scale).cdf(index)

    variables = {
        "beta": index,
        "a0": npdf(loc=10, scale=2),
        "a1": npdf(loc=9, scale=1.7),
        "a1+σ": npdf(loc=10.3, scale=1.7),
        "b0": npdf(loc=1, scale=0.4),
        "b1": npdf(loc=1.2, scale=0.9),
        "b2": npdf(loc=1.3, scale=1.8),
    }

    keys = set(variables.keys())
    keys.remove("beta")

    X1 = pd.DataFrame(variables)
    return X1, index, keys, npdf, variables


@app.cell
def _(X1, alt, keys, variables):
    chart = alt.Chart(X1).mark_line().transform_fold(
        list(keys)
    ).encode(
        alt.X("beta"), 
        alt.Y("value:Q").title("P"),
        color="key:N"
    )

    mark_arrow_with_text = alt.layer(
        # Arrow line
        alt.Chart().mark_line(size=1).encode(
            x=alt.datum(8.5),
            y=alt.datum(variables["a1"][850]),
            x2=alt.datum(9.8),
            y2=alt.datum(variables["a1"][850]),
        ),
        # Arrow head
        alt.Chart().mark_point(shape="triangle", filled=True, fillOpacity=1).encode(
            x=alt.datum(9.7),
            y=alt.datum(variables["a1"][850]),
            angle=alt.AngleValue(-30),
            size=alt.SizeValue(74),
            color=alt.ColorValue("#000000")
        ),
        # Text
        alt.Chart().mark_text(size=14, align="center", baseline="bottom").encode(
            x=alt.datum(9),
            y=alt.datum(variables["a1"][850]),
            text=alt.datum("+σ")
        ),
    )

    drop_line = alt.Chart().mark_line(size=1, color="gray", strokeDash=[5,5]).encode(
        x=alt.datum(8.5),
        y=alt.datum(1),
        x2=alt.datum(8.5),
        y2=alt.datum(0),
    )


    drop_line_2 = alt.Chart().mark_line(size=1, color="gray", strokeDash=[5,5]).encode(
        x=alt.datum(9.8),
        y=alt.datum(1),
        x2=alt.datum(9.8),
        y2=alt.datum(0),
    )

    mark_1 = alt.Chart().mark_point(shape="cross", filled=True, fillOpacity=1, color="black", size=60).encode(
        x=alt.datum(8.5),
        y=alt.datum(variables["a0"][850])
    )

    mark_2 = alt.Chart().mark_point(shape="cross", filled=True, fillOpacity=1, color="black", size=60).encode(
        x=alt.datum(9.8),
        y=alt.datum(variables["a0"][980])
    )

    space_lines = alt.layer(
        # upper bar
        alt.Chart().mark_line(size=1.5).encode(
            x=alt.datum(0),
            y=alt.datum(variables["a0"][850]),
            x2=alt.datum(8.5),
            y2=alt.datum(variables["a0"][850]),
        ),
        alt.Chart().mark_line(size=1.5).encode(
            x=alt.datum(0),
            y=alt.datum(variables["a0"][980]),
            x2=alt.datum(9.8),
            y2=alt.datum(variables["a0"][980]),
        ),
        alt.Chart().mark_line(size=1.5).encode(
            x=alt.datum(6.2),
            y=alt.datum(variables["a0"][850]),
            x2=alt.datum(6.2),
            y2=alt.datum(variables["a0"][980]),
        ),
        alt.Chart().mark_point(shape="triangle", filled=True, fillOpacity=1, color="black").encode(
            x=alt.datum(6.2),
            y=alt.datum(variables["a0"][980] - 0.02),
            size=alt.SizeValue(100)
        ),
        # Text
        alt.Chart().mark_text(size=14, align="center", baseline="bottom").encode(
            x=alt.datum(6),
            y=alt.datum(0.3),
            text=alt.datum("ΔP")
        ),
    )

    (chart + mark_arrow_with_text + drop_line + drop_line_2 + mark_1 + mark_2 + space_lines).configure_axis(grid=False)
    return (
        chart,
        drop_line,
        drop_line_2,
        mark_1,
        mark_2,
        mark_arrow_with_text,
        space_lines,
    )


@app.cell
def _(variables):
    variables["a0"][850]
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
