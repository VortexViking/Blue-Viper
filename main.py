import curses
import importlib.util
import os
import sys

# Import the scrape script
def load_scrape_script():
    script_path = "article-scrape.py"
    if os.path.exists(script_path):
        spec = importlib.util.spec_from_file_location("article_scrape", script_path)
        scrape_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(scrape_module)
        return scrape_module
    else:
        print("Scrape script not found.")
        return None

# Dynamically import the config from ~/.config/blueviper/config.py
def load_config():
    config_path = os.path.expanduser("~/.config/blueviper/config.py")
    if os.path.exists(config_path):
        spec = importlib.util.spec_from_file_location("config", config_path)
        config = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config)
        return config
    else:
        print("Config file not found.")
        return None

# Main UI Logic with Sidebar
def main(stdscr):
    # Load the configuration
    config = load_config()
    if config is None:
        stdscr.addstr(0, 0, "Config file not found. Using default settings.")
        stdscr.refresh()
        stdscr.getch()
        return

    # Initialize curses
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100)  # Set timeout for input refresh

    # Get colors from config
    theme = config.get_theme()
    background_color = theme['background_color']
    highlight_color = theme['highlight_color']
    text_color = theme['text_color']
    sidebar_color = theme['sidebar_color']
    selected_item_color = theme['selected_item_color']

    # Sidebar options with emojis
    sidebar_items = [
        ("Home", "🏠"),
        ("Bookmarks", "🔖"),
        ("Workspaces", "📂"),
        ("Scrape Articles", "🕷️"),
        ("Exit", "🚪")
    ]
    current_option = 0
    stdscr.clear()

    # Load the scraping script
    scrape_module = load_scrape_script()

    while True:
        # Draw Sidebar
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        sidebar_win = curses.newwin(h, 20, 0, 0)  # Sidebar width 20
        sidebar_win.box()

        for idx, (item, emoji) in enumerate(sidebar_items):
            if idx == current_option:
                sidebar_win.attron(curses.color_pair(1))  # Highlight the selected option
                sidebar_win.addstr(idx + 1, 2, f"{emoji} {item}")
                sidebar_win.attroff(curses.color_pair(1))
            else:
                sidebar_win.addstr(idx + 1, 2, f"{emoji} {item}")

        sidebar_win.refresh()

        # Handle user input
        key = stdscr.getch()

        if key == curses.KEY_DOWN:
            current_option = (current_option + 1) % len(sidebar_items)
        elif key == curses.KEY_UP:
            current_option = (current_option - 1) % len(sidebar_items)
        elif key == 10:  # Enter key
            if sidebar_items[current_option][0] == "Scrape Articles":
                # Trigger the scrape function from the script
                if scrape_module:
                    scrape_data = scrape_module.scrape_article()  # Assuming a function named scrape_article
                    stdscr.clear()
                    stdscr.addstr(1, 2, "Scraped Data:")
                    stdscr.addstr(3, 2, str(scrape_data))  # Display scraped content
                    stdscr.refresh()
                    stdscr.getch()  # Wait for user input before returning to menu
            elif sidebar_items[current_option][0] == "Exit":
                break

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
