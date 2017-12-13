from scripts.artwork_downloader import ArtworkDownloader
from scripts.wikiartwork_downloader import WikiartworkDownloader

from scripts.wikiart_pages.hopper import hopper
from scripts.wikiart_pages.monet import monet
from scripts.wikiart_pages.rothko import rothko
from scripts.wikiart_pages.kandinsky import kandinsky
from scripts.wikiart_pages.kandinsky_abstract import kandinsky_abstract
from scripts.wikiart_pages.kandinsky_expressionism import kandinsky_expressionism
from scripts.wikiart_pages.van_gogh import van_gogh
from scripts.wikiart_pages.cezanne_cubism import cezanne_cubism
from scripts.wikiart_pages.cezanne_impressionism import cezanne_impressionism
from scripts.wikiart_pages.cezanne_post_impressionism import cezanne_post_impressionism
from scripts.wikiart_pages.cezanne_romanticism import cezanne_romanticism
from scripts.wikiart_pages.renoir_impressionism import renoir_impressionism
from scripts.wikiart_pages.gauguin_cloisonnism import gauguin_cloisonnism
from scripts.wikiart_pages.gauguin_impressionism import gauguin_impressionism
from scripts.wikiart_pages.gauguin_post_impressionism import gauguin_post_impressionism
from scripts.wikiart_pages.sargent_impressionism import sargent_impressionism
from scripts.wikiart_pages.sargent_realism import sargent_realism

# artwork_downloader = ArtworkDownloader(
#     base_url="https://artuk.org/discover/artworks/view_as/grid/search/makers:laurence-stephen-lowry-18871976/page/9",
#     artist_name="lowry"
# )
# artwork_downloader.save_artworks()

# wikiartwork_downloader = WikiartworkDownloader("cezanne_cubism", cezanne_cubism)
# wikiartwork_downloader.save_artworks()
#
# wikiartwork_downloader = WikiartworkDownloader("cezanne_impressionism", cezanne_impressionism)
# wikiartwork_downloader.save_artworks()

# wikiartwork_downloader = WikiartworkDownloader("cezanne_post_impressionism", cezanne_post_impressionism)
# wikiartwork_downloader.save_artworks()
#
# wikiartwork_downloader = WikiartworkDownloader("cezanne_romanticism", cezanne_romanticism)
# wikiartwork_downloader.save_artworks()
#
# wikiartwork_downloader = WikiartworkDownloader("renoir_impressionism", renoir_impressionism)
# wikiartwork_downloader.save_artworks()

wikiartwork_downloader = WikiartworkDownloader("gauguin_cloisonnism", gauguin_cloisonnism)
wikiartwork_downloader.save_artworks()

wikiartwork_downloader = WikiartworkDownloader("gauguin_impressionism", gauguin_impressionism)
wikiartwork_downloader.save_artworks()

wikiartwork_downloader = WikiartworkDownloader("gauguin_post_impressionism", gauguin_post_impressionism)
wikiartwork_downloader.save_artworks()

wikiartwork_downloader = WikiartworkDownloader("sargent_impressionism", sargent_impressionism)
wikiartwork_downloader.save_artworks()

wikiartwork_downloader = WikiartworkDownloader("sargent_realism", sargent_realism)
wikiartwork_downloader.save_artworks()
