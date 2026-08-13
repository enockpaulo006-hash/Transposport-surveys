import requests
from django.conf import settings


class KoboService:

    @staticmethod
    def get_responses():

        url = (
            f"{settings.KOBO_SERVER}"
            f"/api/v2/assets/"
            f"{settings.KOBO_FORM_UID}"
            f"/data/?format=json"
        )

        headers = {
            "Authorization": f"Token {settings.KOBO_API_TOKEN}"
        }

        try:

            response = requests.get(
                url,
                headers=headers,
                timeout=30
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as e:

            print("Kobo API Error:", e)

            return {
                "count": 0,
                "results": []
            }

    @staticmethod
    def _count_item(counter, value):

        if not value:
            value = "Unknown"

        counter[value] = counter.get(value, 0) + 1

    @staticmethod
    def _most_common(counter):

        if not counter:
            return "-", 0

        key = max(counter, key=counter.get)

        return key, counter[key]

    @staticmethod
    def dashboard_statistics():

        data = KoboService.get_responses()

        responses = data.get("results", [])

        total = len(responses)

        male = 0
        female = 0

        transport = {}

        safety = {}

        age_group = {}

        occupation = {}

        travel_time = {}

        harassment = {}

        for row in responses:
            

            gender = row.get(
                "What_is_your_gender",
                ""
            ).strip().lower()

            if gender == "male":
                male += 1

            elif gender == "female":
                female += 1

            mode = row.get(
                "What_is_your_primary_mode_of_transport",
                "Unknown"
            )

            KoboService._count_item(transport, mode)

            safe = row.get(
                "How_safe_do_you_feel_while_travelling",
                "Unknown"
            )

            KoboService._count_item(safety, safe)

            age = row.get(
                "What_is_your_age_group",
                "Unknown"
            )

            KoboService._count_item(age_group, age)

            job = row.get(
                "What_is_your_occupation",
                "Unknown"
            )

            KoboService._count_item(occupation, job)

            time = row.get(
                "What_is_your_average_one_way_travel_time",
                "Unknown"
            )

            KoboService._count_item(travel_time, time)

            harass = row.get(
                "Have_you_experienced_harassmen",
                "Unknown"
            )

            KoboService._count_item(harassment, harass)

        gender_labels = [
            "Male",
            "Female"
        ]

        gender_values = [
            male,
            female
        ]

        transport_labels = list(
            transport.keys()
        )

        transport_values = list(
            transport.values()
        )

        safety_labels = list(
            safety.keys()
        )

        safety_values = list(
            safety.values()
        )

        age_labels = list(
            age_group.keys()
        )

        age_values = list(
            age_group.values()
        )

        occupation_labels = list(
            occupation.keys()
        )

        occupation_values = list(
            occupation.values()
        )

        travel_labels = list(
            travel_time.keys()
        )

        travel_values = list(
            travel_time.values()
        )

        harassment_labels = list(
            harassment.keys()
        )

        harassment_values = list(
            harassment.values()
        )
        most_transport, most_transport_count = KoboService._most_common(transport)

        most_age, most_age_count = KoboService._most_common(age_group)

        most_occupation, most_occupation_count = KoboService._most_common(occupation)

        most_safety, most_safety_count = KoboService._most_common(safety)

        most_harassment, most_harassment_count = KoboService._most_common(harassment)

        most_travel_time, most_travel_time_count = KoboService._most_common(travel_time)

        return {

            "total": total,

            "male": male,

            "female": female,

            "responses": responses,

            "gender_labels": gender_labels,
            "gender_values": gender_values,

            "transport_labels": transport_labels,
            "transport_values": transport_values,

            "safety_labels": safety_labels,
            "safety_values": safety_values,

            "age_labels": age_labels,
            "age_values": age_values,

            "occupation_labels": occupation_labels,
            "occupation_values": occupation_values,

            "travel_labels": travel_labels,
            "travel_values": travel_values,

            "harassment_labels": harassment_labels,
            "harassment_values": harassment_values,
            
            "most_transport": most_transport,
            "most_transport_count": most_transport_count,

            "most_age": most_age,
            "most_age_count": most_age_count,

            "most_occupation": most_occupation,
            "most_occupation_count": most_occupation_count,

            "most_safety": most_safety,
            "most_safety_count": most_safety_count,

            "most_harassment": most_harassment,
            "most_harassment_count": most_harassment_count,

            "most_travel_time": most_travel_time,
            "most_travel_time_count": most_travel_time_count,            

        }