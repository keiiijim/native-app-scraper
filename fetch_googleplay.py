from time import sleep
import pandas
import json
import play_scraper

if __name__ == "__main__":
    output = pandas.DataFrame()
    bundle_ids = pandas.read_csv("app-list/googleplay.csv").bundle_id.unique()

    for bundle_id in bundle_ids:
        sleep(0.5)

        try:
            app_info = play_scraper.details(bundle_id, hl="ja")
            output = output.append(pandas.io.json.json_normalize(app_info))
        except:
            pass

    output.to_csv("output/googleplay.csv", index=False)

