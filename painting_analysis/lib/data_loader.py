import os

from painting_analysis.lib.artist_lookup import ArtistLookup

class DataLoader:
    def __init__(self, method, directory_path, painting_processor_class):
        self.method = method
        self.directory_path = directory_path
        self.painting_processor_class = painting_processor_class
        self.artist_lookup = ArtistLookup().golden_copy

    def load_paintings(self):
        data = []
        for filename in os.listdir(self.directory_path):
            filepath = self.directory_path + filename
            chosen_processing_method = getattr(self.painting_processor_class(filepath), self.method)
            data.append(chosen_processing_method())
        return data

    def load_targets(self):
        targets = []
        for filename in os.listdir(self.directory_path):
            artist_name = filename.split("_")[0]
            targets.append(self.artist_lookup[artist_name])
        return targets
