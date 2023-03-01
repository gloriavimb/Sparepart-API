# app.py
from flask import Flask, request
from flask_restful import Resource, Api
import pandas



app = Flask(__name__)
api = Api(app)

def get_csv_convert_to_dict(csv_file_path):
    print("csv to json conversion in progress...")


    df = pandas.read_csv(csv_file_path, names=("id","serial","name", "storage_1", "storage_2", "storage_3", "storage_4", "storage_5", "sus_1", "sus_2", "manufacturer", "price"), low_memory=False)
    df.fillna({"id": 0, "serial": "Teadmata", "name": "Teadmata", "storage_1": 0, "storage_2": 0, "storage_3": 0, "storage_4": 0, "storage_5": 0, "sus_1": 0.0, "sus_2": 0.0, "manufacturer": "Teadmata", "price": 0.0}, inplace = True)
    df.astype({"id": int, "serial": str, "name": str, "storage_1": int, "storage_2": int, "storage_3": int, "storage_4": int, "storage_5": int, "sus_1": float, "sus_2": float, "manufacturer": str, "price": float})

    print("Conversion finished.")
    return df.to_dict(orient='records')

csv_file_path = r'data/LE.csv'


class parts(Resource):
    def get(self):
        
        search_by = request.args.get("search_by", type = str, default = "")
        search = request.args.get("search", type = str, default = "")
        sort_by = request.args.get("sort_by", type = str, default = "name")
        decending = request.args.get("decending", type = bool, default = False)
        page = request.args.get("page",type = int, default = 0)
        page_size = request.args.get("page_size",type = int,default = 5)

        if page_size > 20:
            return 'Page size too large', 400


        if not(search_by == "name" or search_by == "serial" or search_by == "manufacturer" or search_by == ""):
            return  'Invalid search field', 400

        all_parts = get_csv_convert_to_dict(csv_file_path)
        searched_parts = []

        if search_by or search != "":
            for i in all_parts:
                if search in i[search_by]:
                    searched_parts.append(i)
        else:
            searched_parts = all_parts


        sorted_parts = sorted(searched_parts, key=lambda d: d[sort_by], reverse=decending)
        paged_parts = [sorted_parts[i:i+page_size] for i in range(0, len(sorted_parts), page_size)]

        if page > len(paged_parts):
            return 'Out of page bounds', 404

        return paged_parts[page], 200

api.add_resource(parts, '/parts', endpoint='parts')



if __name__ == '__main__':
    app.run(debug=True)