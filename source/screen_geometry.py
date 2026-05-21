
def get_screen_geometry(app):
    """
    Returns screen width and height in a cross-platform way.
    Works on Windows and macOS.
    """
    screen = app.primaryScreen().availableGeometry()
    screen_width = screen.width()
    screen_height = screen.height()

    return screen_width, screen_height