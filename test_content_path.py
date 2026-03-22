#!/usr/bin/env python3
"""Test script for ContentPathFilter functionality."""

import sys
sys.path.insert(0, '/Users/xiphis/projects/autoremove-torrents')

from autoremovetorrents.filter.contentpath import ContentPathFilter
from autoremovetorrents.torrent import Torrent

def create_torrent(name, content_path):
    """Create a mock torrent with content_path."""
    t = Torrent()
    t.name = name
    t.content_path = content_path
    t.hash = name  # Use name as hash for simplicity
    return t

def test_content_path_filter():
    """Test ContentPathFilter with various scenarios."""
    
    # Create test torrents
    torrents = [
        create_torrent('movie1', '/downloads/movies/avatar.mp4'),
        create_torrent('movie2', '/downloads/movies/inception.mkv'),
        create_torrent('tv1', '/downloads/tv/breaking_bad/s01e01.mkv'),
        create_torrent('tv2', '/downloads/tv-shows/game_of_thrones/s01e01.mkv'),
        create_torrent('important', '/downloads/important/backup.zip'),
        create_torrent('keep', '/downloads/keep/data.iso'),
        create_torrent('music', '/downloads/music/album'),
        create_torrent('no_path', None),  # No content path
    ]
    
    print("=" * 60)
    print("Test 1: Filter by exact path")
    print("=" * 60)
    
    # Filter only movies
    f = ContentPathFilter(
        all_content_paths=False,
        ac=['/downloads/movies'],
        re=[]
    )
    result = f.apply(set(torrents))
    print(f"Filter: content_paths=['/downloads/movies']")
    print(f"Result: {[t.name for t in result]}")
    assert 'movie1' in [t.name for t in result], "movie1 should be included"
    assert 'movie2' in [t.name for t in result], "movie2 should be included"
    assert 'tv1' not in [t.name for t in result], "tv1 should not be included"
    print("✅ Test 1 passed!\n")
    
    print("=" * 60)
    print("Test 2: Filter by parent directory (wildcard)")
    print("=" * 60)
    
    # Filter all TV shows
    f = ContentPathFilter(
        all_content_paths=False,
        ac=['/downloads/tv', '/downloads/tv-shows'],
        re=[]
    )
    result = f.apply(set(torrents))
    print(f"Filter: content_paths=['/downloads/tv', '/downloads/tv-shows']")
    print(f"Result: {[t.name for t in result]}")
    assert 'tv1' in [t.name for t in result], "tv1 should be included"
    assert 'tv2' in [t.name for t in result], "tv2 should be included"
    print("✅ Test 2 passed!\n")
    
    print("=" * 60)
    print("Test 3: Filter with exclusions")
    print("=" * 60)
    
    # Filter all downloads except important and keep
    f = ContentPathFilter(
        all_content_paths=True,  # Accept all
        ac=[],
        re=['/downloads/important', '/downloads/keep']
    )
    result = f.apply(set(torrents))
    print(f"Filter: all_content_paths=True, excluded=['/downloads/important', '/downloads/keep']")
    print(f"Result: {[t.name for t in result]}")
    assert 'important' not in [t.name for t in result], "important should be excluded"
    assert 'keep' not in [t.name for t in result], "keep should be excluded"
    assert 'movie1' in [t.name for t in result], "movie1 should be included"
    print("✅ Test 3 passed!\n")
    
    print("=" * 60)
    print("Test 4: Combined accept and reject")
    print("=" * 60)
    
    # Accept all under /downloads, but reject /downloads/important
    f = ContentPathFilter(
        all_content_paths=False,
        ac=['/downloads'],
        re=['/downloads/important']
    )
    result = f.apply(set(torrents))
    print(f"Filter: content_paths=['/downloads'], excluded=['/downloads/important']")
    print(f"Result: {[t.name for t in result]}")
    assert 'movie1' in [t.name for t in result], "movie1 should be included"
    assert 'tv1' in [t.name for t in result], "tv1 should be included"
    assert 'important' not in [t.name for t in result], "important should be excluded"
    print("✅ Test 4 passed!\n")
    
    print("=" * 60)
    print("Test 5: Handle None content_path")
    print("=" * 60)
    
    f = ContentPathFilter(
        all_content_paths=False,
        ac=['/downloads'],
        re=[]
    )
    result = f.apply(set(torrents))
    print(f"Filter: content_paths=['/downloads']")
    print(f"Result: {[t.name for t in result]}")
    assert 'no_path' not in [t.name for t in result], "torrent with None path should not be included"
    print("✅ Test 5 passed!\n")
    
    print("=" * 60)
    print("🎉 All tests passed!")
    print("=" * 60)

if __name__ == '__main__':
    test_content_path_filter()