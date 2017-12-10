import os
from glob import glob

from painting_analysis.lib.artist_lookup import ArtistLookup
from painting_analysis.lib.painting_processor import PaintingProcessor
from painting_analysis.lib.painting_processor import WrongColourDepth

class DataLoader:
    def __init__(self, method, directory_path, painting_processor_class=PaintingProcessor):
        self.method = method
        self.directory_path = directory_path
        self.painting_processor_class = painting_processor_class
        self.artist_lookup = ArtistLookup().golden_copy

    def load_paintings_and_targets(self):
        data = []
        targets = []
        for filename in os.listdir(self.directory_path):
            if not ".DS_Store" in filename:
                try:
                    filepath = self.directory_path + filename
                    chosen_processing_method = getattr(self.painting_processor_class(filepath), self.method)
                    artist_name = filename.split("_")[0]
                    targets.append(self.artist_lookup[artist_name])
                    data.append(chosen_processing_method())
                    print(".", end="", flush=True)
                except WrongColourDepth as e:
                    print ("\nerror processing", filename, "-", type(e))
        print()
        return data, targets
