from scripts.artwork_downlaoder import ArtworkDownloader

artwork_downloader = ArtworkDownloader(
    base_url="https://artuk.org/discover/artworks/view_as/grid/search/makers:laurence-stephen-lowry-18871976/page/9",
    artist_name="lowry"
)
artwork_downloader.save_artworks()
