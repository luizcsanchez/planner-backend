import pytest
from datetime import datetime, timedelta
import uuid
import sqlite3
from .activities_repository import ActivitiesRepository
from src.models.settings.db_connection_handler import db_connection_handler

sqlite3.register_adapter(datetime, lambda d: d.isoformat())

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_registry_activity():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    acitivities_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "title": "Nadar",
        "occurs_at": datetime.strptime("02-01-2024", "%d-%m-%Y"),
    }

    activities_repository.registry_activity(acitivities_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_activities_from_trip():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activities = activities_repository.find_activities_from_trip(trip_id)
    print(activities)

