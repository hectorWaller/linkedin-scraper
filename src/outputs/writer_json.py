thonimport json

class JSONWriter:
    @staticmethod
    def write(path: str, data: list):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)