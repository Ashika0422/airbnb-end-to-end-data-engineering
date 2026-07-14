import plotly.express as px


def price_distribution(df):

    fig = px.histogram(

        df,

        x="price",

        nbins=40,

        title="Price Distribution",

        color_discrete_sequence=["#FF5A5F"]

    )

    fig.update_layout(

        template="plotly_white",

        title_x=0.5

    )

    return fig


def room_type_chart(df):

    room = (

        df.groupby("room_type")["price"]

        .mean()

        .reset_index()

    )

    fig = px.bar(

        room,

        x="room_type",

        y="price",

        color="price",

        color_continuous_scale="Reds",

        title="Average Price by Room Type"

    )

    fig.update_layout(

        template="plotly_white",

        title_x=0.5

    )

    return fig


def property_chart(df):

    prop = (

        df.groupby("property_type")["price"]

        .mean()

        .sort_values(ascending=False)

        .head(15)

        .reset_index()

    )

    fig = px.bar(

        prop,

        x="property_type",

        y="price",

        color="price",

        color_continuous_scale="Reds",

        title="Average Price by Property Type"

    )

    fig.update_layout(

        template="plotly_white",

        xaxis_tickangle=-40,

        title_x=0.5

    )

    return fig


def scatter_reviews(df):

    fig = px.scatter(

        df,

        x="number_of_reviews",

        y="price",

        color="room_type",

        size="review_scores_rating",

        hover_data=[

            "property_type",

            "review_scores_rating"

        ],

        title="Reviews vs Price"

    )

    fig.update_layout(

        template="plotly_white",

        title_x=0.5

    )

    return fig


def pie_room_type(df):

    fig = px.pie(

        df,

        names="room_type",

        title="Room Type Distribution",

        hole=.45,

        color_discrete_sequence=px.colors.sequential.Reds

    )

    return fig