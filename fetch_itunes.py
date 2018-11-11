import pandas
import re
import json
import requests
from time import sleep

if __name__ == "__main__":
    output = pandas.DataFrame()
    app_ids = pandas.read_csv("app-list/itunes.csv").app_id.unique()

    for app_id in app_ids:
        sleep(0.5)

        if re.match("\d+", str(app_id)):
            id_name = "id"
        else:
            id_name = "bundleId"

        api_url = "http://itunes.apple.com/JP/lookup?{id_name}={app_id}".format(id_name=id_name, app_id=app_id)

        try:
            app_info = requests.get(api_url).json()
            output = output.append(pandas.io.json.json_normalize(app_info, record_path="results"))
        except:
            pass

    output.to_csv("output/itunes.csv", index=False)

