AUTHOR = 'Kian Wee Chen'
SITENAME = 'Project Automated'
# SITESUBTITLE ='Sub-title that goes underneath site name in jumbotron.'
# SITETAG = "Text that's displayed in the title on the home page."
SITEURL = ""

THEME = 'themes/pa_bootstrap5' # default was 'notmyidea'

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False  # default was True
DELETE_OUTPUT_DIRECTORY = True  # default was False
USE_FOLDER_AS_CATEGORY = False  # default was True
SLUGIFY_SOURCE = 'basename'  # default was 'title'

INDEX_SAVE_AS = '/blogs/index.html'  # default was 'index.html'
ARTICLE_PATHS = ['blogs']  # default was ['']
PAGE_PATHS = ['pages', 'projects']  # default was ['pages']

PATH_METADATA = r'(?P<path_no_ext>.*)\..*'  # default was ''
ARTICLE_URL = '{path_no_ext}.html'  # default was '{slug}.html'
PAGE_URL = '{path_no_ext}.html'  # default was 'pages/{slug}.html'

ARTICLE_SAVE_AS = '{path_no_ext}.html'  # default was '{slug}.html'
PAGE_SAVE_AS = '{path_no_ext}.html'  # default was 'pages/{slug}.html'

ARCHIVE_SAVE_AS = False
DISPLAY_CATEGORIES_ON_MENU = False
CATEGORIES_SAVE_AS = 'categories.html'
# STATIC_PATHS = ['images', 'extra', 'theme/static', 'pdfs']
# DIRECT_TEMPLATES = ['index', 'categories', 'tags', 'archives', 'software']

MENUITEMS = (
    ("Blog", "/pa_theme/blogs/"),
    ("Projects", "/pa_theme/pages/projects.html"),
    ("About", "/pa_theme/pages/about.html"),
    ("Contact", "/pa_theme/pages/contact.html"),
)
