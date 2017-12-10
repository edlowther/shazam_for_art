from scripts.artwork_downlaoder import ArtworkDownloader
from scripts.wikiartwork_downloader import WikiartworkDownloader

from scripts.wikiart_pages.hopper import hopper
from scripts.wikiart_pages.monet import monet
from scripts.wikiart_pages.rothko import rothko
from scripts.wikiart_pages.kandinsky import kandinsky
from scripts.wikiart_pages.van_gogh import van_gogh

# artwork_downloader = ArtworkDownloader(
#     base_url="https://artuk.org/discover/artworks/view_as/grid/search/makers:laurence-stephen-lowry-18871976/page/9",
#     artist_name="lowry"
# )
# artwork_downloader.save_artworks()
artists = {"hopper": hopper, "monet": monet, "rothko": rothko, "kandinsky": kandinsky, "van-gogh": van_gogh}
for artist_name, artist_wikiartpage  in artists.items():
    wikiartwork_downloader = WikiartworkDownloader(artist_name, artist_wikiartpage)
    wikiartwork_downloader.save_artworks()
