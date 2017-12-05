from scripts.artwork_downlaoder import ArtworkDownloader

artwork_downloader = ArtworkDownloader(
    base_url="https://artuk.org/discover/artworks/search/actor:rembrandt-van-rijn-16061669/page/5",
    artist_name="rembrandt"
)
artwork_downloader.save_artworks()
