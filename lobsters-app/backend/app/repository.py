"""
============================================================
BACKEND LAYER 1 — REPOSITORY
============================================================
Role: Backend Developer

Responsibility: This is the ONLY layer that writes database queries
(session.query(...)). It knows how to ask the database for posts,
but it does NOT know about HTTP, JSON, or Flask routes.

Why a separate layer for this?
  - If we ever swap SQLite for PostgreSQL, only db.py changes.
  - If our query logic gets complex (filters, pagination), it stays
    contained here instead of cluttering the API routes.
  - We can unit-test queries directly, without spinning up a server.
============================================================
"""

from app.models import Post
from app.db import get_session


def get_top_posts(limit: int = 10) -> list:
    """
    Fetches the top N posts ordered by score, highest first.
    ... (mentorun bütün docstring şərhləri olduğu kimi qalır)
    """
    session = get_session()
    posts = (
        session.query(Post)
        .order_by(Post.score.desc())
        .limit(limit)
        .all()
    )
    session.close()
    return posts


def get_post_by_id(post_id: str):
    """
    Fetches a single post by its Lobsters post_id.

    Args:
        post_id (str): The Lobsters post_id, e.g. "1abcde"

    Returns:
        Post | None: The matching Post object, or None if not found.

    TODO:
        - Get a session: session = get_session()
        - Query for the post: post = session.query(Post).filter_by(post_id=post_id).first()
        - Close the session: session.close()
        - Return post
    """
    pass  # Remove this line when you implement the function


def count_posts() -> int:
    """
    Returns the total number of posts currently stored in the database.
    Useful for a health-check or stats endpoint.

    Returns:
        int: Total row count in the posts table.

    TODO:
        - Get a session: session = get_session()
        - Count rows: count = session.query(Post).count()
        - Close the session: session.close()
        - Return count
    """
    pass  # Remove this line when you implement the function
