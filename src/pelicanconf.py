AUTHOR = "Alessandro"
SITENAME = "Alessandro Ferrini"
SITEURL = ""
CONTACT_EMAIL = "contact@alessandroferrini.com"
PATH = "content"

TIMEZONE = "Europe/Rome"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Github", "https://github.com/Alurith/"),
    ("LinkedIn", "https://www.linkedin.com/in/alessandro-ferrini-it86/"),
)

# Social widget
SOCIAL = (
    ("Github", "https://github.com/Alurith/"),
    ("X", "https://github.com/Alurith/"),
    ("Instagram", "https://www.instagram.com/imalessandro/"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
THEME = "theme/"

DESCRIPTION = "I am a fullstack web developer with a lenght experience in Python, my stack involves Django, htmx, FastApi, Starlite"

PROJECTS = [
    {
        "title": "Flowtex",
        "stack": ["Django 4.2", "htmx", "PostgreSQL"],
        "description": "",
    },
    {
        "title": "Modula Integration",
        "stack": ["Python 3.11", "redis", "rocketry"],
        "description": "Integrate Modula with client's management software",
    },
    {
        "title": "Knowledgebase Azerbaijan",
        "stack": ["Django 4.2", "htmx", "PostgreSQL", "redis"],
        "description": "Share best practices for social entrepreneurs in Azerbaijan ",
        "link": "https://knowledge-platform-web.onrender.com/",
    },
    {
        "title": "Reset",
        "stack": ["Django 4.2", "htmx", "PostgreSQL"],
        "description": "RESults Enabling Transitions: mapping green and circular business support achievements in the MED region",
        "link": "https://reset-web.onrender.com/",
    },
    {
        "title": "DaTa",
        "stack": ["Django 2.0", "htmx", "MariaDB"],
        "description": "Dashboard to visualize data from different leathercutting machines, supporting brands like: Comelz, Teseo, and Atom",
    },
]
