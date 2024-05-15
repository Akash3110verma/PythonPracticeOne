import json


class JsonOperation:
    @staticmethod
    def load_json_data(path):
        """This function will responsible for loading the json file"""
        with open(path, "r") as fi:
            return json.load(fi)

    @staticmethod
    def dump_json_data(path, data):
        """This function is responsible for dumping the data into json file"""
        with open(path, "w") as file:
            json.dump(data, file)
