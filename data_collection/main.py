from scripts.artwork_downlaoder import ArtworkDownloader

artwork_downloader = ArtworkDownloader(
    base_url="https://artuk.org/discover/artworks/view_as/grid/search/makers:claude-monet-18401926-56211/page/3",
    artist_name="monet"
)
artwork_downloader.save_artworks()
