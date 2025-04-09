
import pytest
from unittest.mock import MagicMock
from entity.gallery import Gallery
from service.gallery_manager import GalleryManager
from exception.exceptions import GalleryNotFoundException, GalleryNotAddedException

@pytest.fixture
def mock_db():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    return mock_conn, mock_cursor

def test_add_gallery_success(mock_db):
    mock_conn, mock_cursor = mock_db
    manager = GalleryManager(mock_conn)
    gallery = Gallery(1, "Modern Art House", "Contemporary collections", "NYC", "Curator01", "10AM-5PM")

    manager.add_gallery(gallery)

    assert mock_cursor.execute.called
    assert mock_conn.commit.called

def test_update_gallery_success(mock_db):
    mock_conn, mock_cursor = mock_db
    manager = GalleryManager(mock_conn)
    gallery = Gallery(1, "Updated Gallery", "Updated desc", "Paris", "CuratorX", "9AM-6PM")

    mock_cursor.fetchone.return_value = (1,)
    manager.update_gallery(gallery)

    assert mock_cursor.execute.call_count >= 2
    assert mock_conn.commit.called

def test_update_gallery_not_found(mock_db):
    mock_conn, mock_cursor = mock_db
    manager = GalleryManager(mock_conn)
    gallery = Gallery(99, "Ghost Gallery", "Nowhere", "Hidden", "NoOne", "Never")

    mock_cursor.fetchone.return_value = None
    with pytest.raises(GalleryNotFoundException):
        manager.update_gallery(gallery)

def test_remove_gallery_success(mock_db):
    mock_conn, mock_cursor = mock_db
    manager = GalleryManager(mock_conn)

    mock_cursor.fetchone.return_value = ("some gallery",)
    manager.remove_gallery(1)

    assert mock_cursor.execute.call_count >= 2
    assert mock_conn.commit.called

def test_remove_gallery_not_found(mock_db):
    mock_conn, mock_cursor = mock_db
    manager = GalleryManager(mock_conn)

    mock_cursor.fetchone.return_value = None
    with pytest.raises(GalleryNotFoundException):
        manager.remove_gallery(404)

def test_search_gallery_by_name_success(mock_db):
    mock_conn, mock_cursor = mock_db
    manager = GalleryManager(mock_conn)

    mock_cursor.fetchall.return_value = [(1, "Gallery A", "Desc", "Loc", "Curator", "9-5")]
    results = manager.search_gallery_by_name("Gallery")

    assert results[0][1] == "Gallery A"

def test_search_gallery_by_name_not_found(mock_db):
    mock_conn, mock_cursor = mock_db
    manager = GalleryManager(mock_conn)

    mock_cursor.fetchall.return_value = []
    with pytest.raises(GalleryNotFoundException):
        manager.search_gallery_by_name("DoesNotExist")
