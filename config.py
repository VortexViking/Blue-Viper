# Blue Viper Configuration File

# Color settings (Blue theme)
THEME = {
    'background_color': '#001f3d',  # Dark blue background
    'highlight_color': '#00aaff',    # Lighter blue for highlighting
    'text_color': '#ffffff',         # White text color for visibility
    'sidebar_color': '#004c7f',      # Dark blue for sidebar
    'selected_item_color': '#0066cc' # Blue for selected items in sidebar
}

# Search Engine Settings
SEARCH_ENGINE = {
    'default': 'Google',             # Set default search engine
    'google': 'https://www.google.com/search?q=',
    'duckduckgo': 'https://duckduckgo.com/?q='
}

# Other Configurations
CONFIG = {
    'enable_emojis': True,           # Whether to enable emoji support
    'enable_scraping': True,         # Enable or disable scraping feature
    'max_history_items': 100         # Maximum number of items in browsing history
}

def get_search_url(query):
    """
    Get the URL for the selected search engine
    """
    if SEARCH_ENGINE['default'] == 'Google':
        return f"{SEARCH_ENGINE['google']}{query}"
    elif SEARCH_ENGINE['default'] == 'DuckDuckGo':
        return f"{SEARCH_ENGINE['duckduckgo']}{query}"

def get_theme():
    """
    Get the theme colors
    """
    return THEME

def toggle_emojis(enable):
    """
    Toggle emoji support
    """
    CONFIG['enable_emojis'] = enable

def toggle_scraping(enable):
    """
    Toggle scraping feature
    """
    CONFIG['enable_scraping'] = enable

def set_max_history_items(limit):
    """
    Set the max history items
    """
    CONFIG['max_history_items'] = limit
