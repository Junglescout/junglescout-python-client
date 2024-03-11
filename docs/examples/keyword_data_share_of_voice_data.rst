########################################################
Combine ASIN-level keyword data with Share of Voice data
########################################################

Description
===========

Combine ASIN-level keyword data with Share of Voice data to show clicks and conversions by
keyword. This report requires less than 50 API calls.

The following inputs are required:

- **ASINs**: Input up to 10 ASINs to pull in the top keywords related to those ASINs
- **Number of Keywords**: Specify the number of keywords you want to pull in data for (i.e., if you
  select 10, the report will highlight the clicks and conversions data for the top 10 keywords by search volume)

Code Example
============

First, set up your API key and API Key Name and instantiate the client

.. code-block:: python

    from jungle_scout.client import Client
    from jungle_scout.models.parameters import (
        Marketplace,
    )

    API_KEY_NAME = "API_KEY_NAME"
    API_KEY = "API_KEY"

    client = Client(api_key_name=API_KEY_NAME, api_key=API_KEY, marketplace=Marketplace.US)

Now, we define a function to pull in the top keywords for the ASINs provided. This function will return the
top keywords for the ASINs provided.

.. code-block:: python

    import pandas as pd

    def get_top_keywords(asins, number_of_keywords, marketplace=Marketplace.US):
        keywords_by_asin = client.keywords_by_asin(
            asin=asins,
        )
        df = pd.json_normalize(keywords_by_asin.data)
        df = df[["attributes.name", "attributes.monthly_trend", "attributes.monthly_search_volume_exact"]]
        df.rename(
            columns={
                "attributes.name": "Keyword",
                "attributes.monthly_trend": "Monthly_Trend",
                "attributes.monthly_search_volume_exact": "Monthly_Search_Volume",
            },
            inplace=True,
        )
        top_keywords = list(df["Keyword"][:number_of_keywords].values)
        return top_keywords

Now we define a function that pulls data from the Share of Voice API endpoint. This function takes a list of
ASINs and returns the share of voice for each ASIN.

.. code-block:: python

    def pull_clicks_and_conversions_SOV_API(top_keywords, marketplace=Marketplace.US):
        clicks_conversions = pd.DataFrame(
            columns=["asin", "name", "brand", "clicks", "conversions", "conversion_rate", "Related Keyword"]
        )

        for keyword in top_keywords:
            share_of_voice = client.share_of_voice(
                keyword=keyword,
                marketplace=marketplace,
            )
            data_sect = share_of_voice.data[0]
            attribute = data_sect["attributes"]
            df1 = pd.json_normalize(attribute["brands"])
            df1 = pd.json_normalize(attribute["top_asins"])
            df1["Related Keyword"] = keyword
            clicks_conversions = pd.concat([clicks_conversions, df1], ignore_index=True)
        return clicks_conversions

Finally, we define a function that combines the data from the previous functions and returns the clicks and
conversions data for the top keywords for the ASINs provided.

.. code-block:: python

    def compile_report_data(clicks_conversions, top_keywords):
        clicks_conversions = clicks_conversions.sort_values(by="clicks", ascending=False).reset_index()
        clicks_conversions.drop(columns=["index"], inplace=True)
        print(f"This clicks and conversions data points are based on the following keywords, sorted by search volume:")
        for key in top_keywords:
            print(f" - {key.title()}")
        total_clicks = clicks_conversions["clicks"].sum()
        total_conversions = clicks_conversions["conversions"].sum()
        conversion_rate = total_conversions / total_clicks
        print("\nOverall Metrics : ")
        print(f" - Total Clicks : {total_clicks}")
        print(f" - Total Conversions : {total_conversions}")
        print(f' - Conversion Rate : {"{:.2%}".format(conversion_rate)}')
        print(f" - Based on {len(clicks_conversions)} ASINs")

        clicks_conversions_grouped = (
            clicks_conversions.groupby("brand")[["clicks", "conversions"]]
            .sum()
            .reset_index()
            .sort_values(by="clicks", ascending=False)
        )

        clicks_conversions_grouped["conversion_rate"] = (
            clicks_conversions_grouped["conversions"] / clicks_conversions_grouped["clicks"]
        )

        clicks_conversions_grouped_keyword = (
            clicks_conversions.groupby("Related Keyword")[["clicks", "conversions"]]
            .sum()
            .reset_index()
            .sort_values(by="clicks", ascending=False)
        )

        clicks_conversions_grouped_keyword["conversion_rate"] = (
            clicks_conversions_grouped_keyword["conversions"] / clicks_conversions_grouped_keyword["clicks"]
        )

        return display(clicks_conversions_grouped, clicks_conversions, clicks_conversions_grouped_keyword)

With these functions defined, we can call these functions to get the data we need.

.. code-block:: python

    asins = [
        "B09BCMMFZ2",
        "B0764P9T73",
        "B08T34VX9M",
        "B089P8XVGZ",
        "B097CVZ2N2",
        "B099NBCVLR",
        "B09JHR1K76",
        "B089W847RL",
        "B08P4VLB5H",
        "B07XVTD4F2",
    ]

    number_of_keywords = 10
    keywords = get_top_keywords(asins, number_of_keywords)
    clicks_conversions = pull_clicks_and_conversions_SOV_API(keywords)
    clicks_conversions_report = compile_report_data(clicks_conversions, keywords)
