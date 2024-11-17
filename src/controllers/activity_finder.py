from typing import Dict

class ActivityFinder:
    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository

    def find_activities_from_trip(self, trip_id) -> Dict:
        try:
            activities = self.__activities_repository.find_activities_from_trip(trip_id)
        
            formatted_activities = []

            for activity in activities:
                formatted_activities.append({
                    "id": activity[0],
                    "titile": activity[2],
                    "occurs_at": activity[3]
                })

            return {
                "body": { "activities": formatted_activities },
                "status_code": 200
            }
        except Exception as execption:
            return {
                "body": { "error": "Bad Request", "message": str(execption) },
                "status_code": 400
            }

