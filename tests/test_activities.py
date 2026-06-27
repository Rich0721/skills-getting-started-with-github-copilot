def test_get_activities_returns_all_required_fields(client):
    # Arrange
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert "Chess Club" in payload

    for details in payload.values():
        assert expected_fields.issubset(details.keys())
        assert isinstance(details["participants"], list)
