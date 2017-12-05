from scripts.artwork_downlaoder import ArtworkDownloader

artwork_downloader = ArtworkDownloader(
    base_url="https://artuk.org/discover/artworks/search/actor:constable-john-17761837/page/18",
    artist_name="constable"
)
artwork_downloader.save_artworks()
