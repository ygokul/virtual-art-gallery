import pytest
from unittest.mock import MagicMock
from service.artwork_manager import ArtworkManager
from entity.artwork import Artwork
from exception.exceptions import ArtworkNotFoundException

@pytest.fixture
def mock_db():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    return mock_conn, mock_cursor

def test_add_artwork(mock_db):
    mock_conn, mock_cursor = mock_db
    manager = ArtworkManager(mock_conn)

    # Setup mock behavior
    mock_cursor.lastrowid = 1

    result = manager.add_artwork(
        title='Mona Lisa',
        description='A classic painting',
        creation_date='2024-04-09',
        medium='Oil',
        image_url='http://image.com/mona.jpg'
    )

    assert isinstance(result, Artwork)
    assert result.get_title() == 'Mona Lisa'
    mock_cursor.execute.assert_called_once()
    mock_conn.commit.assert_called_once()

def test_update_artwork_success(mock_db):
    mock_conn, mock_cursor = mock_db
    manager = ArtworkManager(mock_conn)

    mock_cursor.rowcount = 1

    artwork = Artwork(
        artwork_id=1,
        title='Updated',
        description='Updated Desc',
        creation_date='2024-04-09',
        medium='Acrylic',
        image_url='http://image.com/updated.jpg'
    )

    manager.update_artwork(artwork)

    assert mock_cursor.execute.called
    assert mock_conn.commit.called

def test_update_artwork_not_found(mock_db):
    mock_conn, mock_cursor = mock_db
    manager = ArtworkManager(mock_conn)

    mock_cursor.rowcount = 0

    artwork = Artwork(
        artwork_id=99,
        title='Missing',
        description='Not there',
        creation_date='2024-01-01',
        medium='Digital',
        image_url='http://image.com/missing.jpg'
    )

    with pytest.raises(ArtworkNotFoundException):
        manager.update_artwork(artwork)

def test_remove_artwork_success(mock_db):
    mock_conn, mock_cursor = mock_db
    manager = ArtworkManager(mock_conn)

    mock_cursor.rowcount = 1

    manager.remove_artwork(1)

    mock_cursor.execute.assert_called_once()
    mock_conn.commit.assert_called_once()

def test_remove_artwork_not_found(mock_db):
    mock_conn, mock_cursor = mock_db
    manager = ArtworkManager(mock_conn)

    mock_cursor.rowcount = 0

    with pytest.raises(ArtworkNotFoundException):
        manager.remove_artwork(999)

def test_get_artwork_by_id_success(mock_db):
    mock_conn, mock_cursor = mock_db
    manager = ArtworkManager(mock_conn)

    mock_cursor.fetchone.return_value = (
        1, 'Starry Night', 'Night sky',
        '2024-04-09', 'Oil',
        'http://image.com/starry.jpg'
    )

    artwork = manager.get_artwork_by_id(1)

    assert isinstance(artwork, Artwork)
    assert artwork.get_title() == 'Starry Night'
    assert artwork.get_medium() == 'Oil'

def test_get_artwork_by_id_not_found(mock_db):
    mock_conn, mock_cursor = mock_db
    manager = ArtworkManager(mock_conn)

    mock_cursor.fetchone.return_value = None

    with pytest.raises(ArtworkNotFoundException):
        manager.get_artwork_by_id(999)
