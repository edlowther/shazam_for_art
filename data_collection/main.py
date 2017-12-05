from scripts.artwork_downloader import ArtworkDownloader

artwork_downloader = ArtworkDownloader(
    base_url="https://artuk.org/discover/artworks/view_as/grid/search/keyword:rubens/page/10",
    artist_name="rubens"
)
artwork_downloader.save_artworks()
