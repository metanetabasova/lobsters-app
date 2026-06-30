"""
============================================================
BACKEND LAYER 2 — SERVICE
============================================================
Role: Backend Developer

Responsibility: Sits between the Repository (raw DB queries) and
the API routes (HTTP handling). Converts ORM objects into plain
dicts, and is the place to add business rules later (e.g. "only
show posts with score > 0", "limit max 50 per request", etc).

This layer does NOT know about Flask, requests, or HTTP status codes.
It does NOT write raw SQL queries — that's the Repository's job.
============================================================
"""

from app import repository


def get_top_posts_for_api(limit: int = 10) -> dict:
    """
    Gets the top posts and formats them for the API response.
    ...
    """
    if limit < 1: limit = 1
    if limit > 50: limit = 50
    
    posts = repository.get_top_posts(limit)
    posts_data = [post.to_dict() for post in posts]
    
    return {"success": True, "data": posts_data, "count": len(posts_data)}


def get_single_post_for_api(post_id: str) -> dict:
    """
    Gets one post by id and formats it for the API response.
    ...
    """
    post = repository.get_post_by_id(post_id)
    if post is None:
        return {"success": False, "error": "Post not found."}
    
    return {"success": True, "data": post.to_dict()}


def get_stats_for_api() -> dict:
    """
    Gets simple stats about the dataset for a health/stats endpoint.
    ...
    """
    count = repository.count_posts()
    return {"success": True, "data": {"total_posts": count}}
