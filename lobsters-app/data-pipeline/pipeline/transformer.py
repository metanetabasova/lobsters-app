"""
============================================================
PIPELINE LAYER 2 — TRANSFORMER
============================================================
Role: Data Engineer

Responsibility: Take the RAW Lobsters JSON (from fetcher.py) and turn
it into a clean list of plain Python dicts that match our database
schema exactly (see pipeline/models.py).

This layer does NOT touch the network and does NOT touch the database.
It is pure data transformation — easy to test, easy to reason about.

Why a separate layer for this?
  - Lobsters' raw JSON has fields we don't need and some nesting
    (like submitter_user) we want flattened. This layer is the ONE
    place that knows how to translate "Lobsters' shape" into "our
    shape".
  - If our database schema changes, only this file (and models.py)
    need to change — not the fetcher.
============================================================
"""

from datetime import datetime


def transform_post(raw_post_data: dict) -> dict:
    """
    Transforms a SINGLE raw Lobsters story object into our schema shape.

    Args:
        raw_post_data (dict): One story object straight out of the
            Lobsters JSON array, e.g. raw_json[0]

    Returns:
        dict: A dict with exactly these keys, matching models.Post:
            {
                "post_id": str,        <- raw_post_data["short_id"]
                "title": str,          <- raw_post_data["title"]
                "author": str,         <- raw_post_data["submitter_user"]["username"]
                "score": int,          <- raw_post_data["score"]
                "num_comments": int,   <- raw_post_data["comment_count"]
                "url": str,            <- raw_post_data["url"]
                "permalink": str,      <- raw_post_data["comments_url"]
                "created_utc": float,  <- convert raw_post_data["created_at"] (an ISO
                                           8601 string) into a Unix timestamp (float)
                "fetched_at": datetime <- datetime.now(timezone.utc)
            }

    TODO:
        - Build and return the dict described above.
        - post_id: Lobsters' "short_id" is already a short, unique,
          clean string (e.g. "xacdsk") — just use it directly.
        - author: this one is NESTED in Lobsters' JSON — you need
          raw_post_data["submitter_user"]["username"], not a flat
          "author" key.
        - url: what the story links to externally.
        - permalink: Lobsters calls this "comments_url", and it's
          already a full, absolute URL — you do NOT need to prepend
          anything to it.
        - created_utc: Lobsters gives us "created_at" as an ISO 8601
          STRING (e.g. "2023-11-02T03:47:05.000-05:00"), not a Unix
          timestamp. You need to convert it:
              parsed = datetime.fromisoformat(raw_post_data["created_at"])
              created_utc = parsed.timestamp()
          (datetime.fromisoformat can parse this format directly in
          modern Python, including the timezone offset.)
        - fetched_at: use datetime.now(timezone.utc) to record the
          moment OUR pipeline processed this post.
    """
    parsed = datetime.fromisoformat(raw_post_data["created_at"])
    created_utc = parsed.timestamp()
