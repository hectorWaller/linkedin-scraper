thonimport csv

class CSVWriter:
    @staticmethod
    def write(path: str, data: list):
        if not data:
            return

        keys = list(data[0].keys())

        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)