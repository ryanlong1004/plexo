import os
from dotenv import load_dotenv
from plexapi.server import PlexServer
from typing import Generator

# Load environment variables from .env file
load_dotenv()

# Extract base URL and token from environment variables
BASE_URL = os.getenv("BASE_URL")
TOKEN = os.getenv("TOKEN")

# Initialize Plex server connection
plex = PlexServer(BASE_URL, TOKEN)


def get_clients():
    """
    Retrieve a list of connected clients to the Plex server.
    """
    return plex.clients()


def list_unwatched_movies():
    """
    List all unwatched movies in the "Movies" library section.
    """
    unwatched_movies = []
    for video in plex.library.section("Movies").search(unwatched=True):
        unwatched_movies.append(video.title)
    return unwatched_movies


def search_content(keyword: str) -> Generator:
    """
    Search for content in the Plex library containing the specified keyword.

    Args:
        keyword (str): The keyword to search for.

    Returns:
        Generator: A generator yielding matched video items.
    """
    return (video for video in plex.search(keyword))


def get_library_section(name: str):
    """
    Get a specific library section by name.

    Args:
        name (str): The name of the library section.

    Returns:
        PlexSection: The Plex library section object.
    """
    return plex.library.section(name)


if __name__ == "__main__":
    # Example 1: Print unwatched movies.
    print("Unwatched Movies:")
    for title in list_unwatched_movies():
        print(f"- {title}")

    # Example 2: Print all connected clients.
    print("\nConnected Clients:")
    for client in get_clients():
        print(f"- {client}")

    # Example 3: Search for content with a specific keyword.
    search_keyword = "transformers"
    print(f"\nSearch Results for '{search_keyword}':")
    for video in search_content(search_keyword):
        print(f"- {video.title}")

    # Example 4: Print all items in the "Movies" library section.
    library_section = "Movies"
    print(f"\nItems in the '{library_section}' Library Section:")
    section = get_library_section(library_section)
    for item in section.all():
        print(f"- {item.title} (URL: {item.getWebURL()})")
