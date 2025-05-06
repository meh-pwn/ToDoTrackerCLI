import pytest
import json
import os
from task_manager import (add_task, delete_task, update_task, update_status,
                  parse_input)

TEST_FILENAME = "test_user_tasks.json"

def setup_function():
    with open(TEST_FILENAME, 'w') as file:
        json.dump({}, file)

def teardown_function():
    if os.path.exists(TEST_FILENAME):
        os.remove(TEST_FILENAME)

def test_add_task():
    add_task("Buy milk", filename=TEST_FILENAME)
    with open(TEST_FILENAME, 'r') as file:
        test_tasks_dict = json.load(file)
    assert len(test_tasks_dict) == 1
    task = test_tasks_dict["1"]
    assert task[0] == "Buy milk"
    assert task[1] == "todo"

def test_update_task():
    add_task("Buy milk", filename=TEST_FILENAME)
    update_task("1", "Updated task", filename=TEST_FILENAME)
    with open(TEST_FILENAME, 'r') as file:
        test_tasks_dict = json.load(file)
    assert test_tasks_dict["1"][0] == "Updated task"

def test_update_nonexistent_task():
    with pytest.raises(SystemExit) as excinfo:
        update_task("99", "Updated task", filename=TEST_FILENAME)
    assert "Error: You can't update this task because it's not on the to-do list." in str(excinfo.value)

def test_delete_task():
    add_task("Task to delete", filename=TEST_FILENAME)
    delete_task("1", filename=TEST_FILENAME)
    with open(TEST_FILENAME, 'r') as file:
        test_tasks_dict = json.load(file)
    assert test_tasks_dict == {}

def test_delete_nonexistent_task():
    with pytest.raises(SystemExit) as excinfo:
        delete_task("99", filename=TEST_FILENAME)
    assert "Error: You can't delete this task because it's not on the to-do list." in str(excinfo.value)

def test_update_status():
    add_task("Task to mark somehow", filename=TEST_FILENAME)
    update_status("1", "done", filename=TEST_FILENAME)
    with open(TEST_FILENAME, 'r') as file:
        test_tasks_dict = json.load(file)
    assert test_tasks_dict["1"][1] == "done"

def test_parse_input():
    assert parse_input("add Buy milk") == ["add", "Buy", "milk"]
    assert parse_input("delete 1") == ["delete", "1"]
    assert parse_input('add "Buy milk"') == ["add", "Buy milk"]