def test_signup_adds_new_participant(client):
    # Arrange
    activity_name = "Chess Club"
    new_email = "newstudent@mergington.edu"

    # Act
    signup_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": new_email},
    )
    activities_response = client.get("/activities")
    activities_payload = activities_response.json()

    # Assert
    assert signup_response.status_code == 200
    assert signup_response.json()["message"] == f"Signed up {new_email} for {activity_name}"
    assert new_email in activities_payload[activity_name]["participants"]


def test_signup_returns_404_for_unknown_activity(client):
    # Arrange
    unknown_activity = "Unknown Activity"
    email = "student@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{unknown_activity}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_returns_400_for_duplicate_participant(client):
    # Arrange
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": existing_email},
    )

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"
