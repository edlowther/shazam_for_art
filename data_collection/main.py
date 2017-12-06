from scripts.artwork_downlaoder import ArtworkDownloader
from scripts.wikiartwork_downloader import WikiartworkDownloader

from scripts.wikiart_pages.hopper import hopper
from scripts.wikiart_pages.monet import monet

# artwork_downloader = ArtworkDownloader(
#     base_url="https://artuk.org/discover/artworks/view_as/grid/search/makers:laurence-stephen-lowry-18871976/page/9",
#     artist_name="lowry"
# )
# artwork_downloader.save_artworks()

wikiartwork_downloader = WikiartworkDownloader("monet", monet)
wikiartwork_downloader.save_artworks()
