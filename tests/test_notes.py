import pytest
import os
from notes_manager import NotesManager

@pytest.fixture
def manager():
    db_name = "test_notes.db"
    m = NotesManager(db_name)
    yield m
    m.conn.close()
    if os.path.exists(db_name):
        os.remove(db_name)

def test_add_note(manager):
    note_id = manager.add_note("t1", "c1", "cat1")
    assert note_id is not None
    assert len(manager.get_all()) == 1

def test_empty_title(manager):
    with pytest.raises(ValueError):
        manager.add_note("   ", "c", "cat")

def test_update_note(manager):
    note_id = manager.add_note("t1", "c1", "cat1")
    manager.update_note(note_id, "t2", "c2", "cat2")
    notes = manager.get_all()
    assert notes[0][1] == "t2"
    assert notes[0][3] == "cat2"

def test_delete_note(manager):
    note_id = manager.add_note("t1", "c1", "cat1")
    deleted = manager.delete_note(note_id)
    assert deleted == 1
    assert len(manager.get_all()) == 0

def test_delete_non_existent(manager):
    deleted = manager.delete_note(999)
    assert deleted == 0

def test_search_case_insensitive(manager):
    manager.add_note("Apple", "Red fruit", "Food")
    res = manager.search("red")
    assert len(res) == 1
    assert res[0][1] == "Apple"

def test_get_by_category(manager):
    manager.add_note("t1", "c1", "Work")
    manager.add_note("t2", "c2", "Home")
    res = manager.get_by_category("work")
    assert len(res) == 1
    assert res[0][3] == "Work"

def test_get_categories(manager):
    manager.add_note("t1", "c1", "Work")
    manager.add_note("t2", "c2", "Work")
    manager.add_note("t3", "c3", "Home")
    cats = manager.get_categories()
    assert len(cats) == 2
    assert "Work" in cats
    assert "Home" in cats
