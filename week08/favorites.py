import json


class FavoritesManager:
    def __init__(self, filename):
        self.filename = filename
        self.favorites = self._load()

    def _load(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return data if isinstance(data, dict) else {}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save(self):
        with open(self.filename, "w") as file:
            json.dump(self.favorites, file, indent=4)

    def add(self, name, location):
        key = name.lower()
        if key in self.favorites:
            return False
        self.favorites[key] = location
        self._save()
        return True

    def remove(self, name):
        key = name.lower()
        if key not in self.favorites:
            return False
        del self.favorites[key]
        self._save()
        return True

    def list_all(self):
        return self.favorites

    def get_location(self, name):
        return self.favorites.get(name.lower())