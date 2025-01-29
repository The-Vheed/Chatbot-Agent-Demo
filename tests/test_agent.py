import os
import csv
import pytest
from langchain_openai import ChatOpenAI
from pydantic import ValidationError

# Importing functions and classes from the main code
from app.agent import (
    GetOrderStatus,
    GetAllReturnPolices,
    ExportUserData,
)


# Test GetOrderStatus
@pytest.mark.parametrize(
    "order_id, expected_status",
    [
        (123, "Pending"),
        (456, "Shipped"),
        (789, "Delivered"),
        (900, "Delivered"),  # Test edge case
    ],
)
def test_get_order_status(order_id, expected_status):
    # Pass the input as a dictionary
    result = GetOrderStatus.invoke({"order_id": order_id})
    assert result == expected_status


# Test GetAllReturnPolices
def test_get_all_return_policies():
    result = GetAllReturnPolices.invoke({})
    assert "return most items within 30 days" in result
    assert "certain items such as clearance merchandise" in result
    assert "Refunds will be issued to the original form of payment" in result


# Test ExportUserData
def test_export_user_data(tmp_path):
    # Create a temporary directory
    os.chdir(tmp_path)

    full_name = "John Doe"
    email = "john.doe@example.com"
    phone = "123-456-7890"

    # Test ExportUserData
    result = ExportUserData.invoke(
        {"full_name": full_name, "email": email, "phone": phone}
    )
    assert result == "Contact information saved successfully."

    # Verify file content
    filename = "user_data.csv"
    assert os.path.exists(filename)

    with open(filename, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        assert len(rows) == 1
        assert rows[0] == {"full_name": full_name, "email": email, "phone": phone}


# Test ExportUserData with invalid Email input
def test_export_user_data_invalid_email_input(tmp_path):
    # Create a temporary directory
    os.chdir(tmp_path)

    full_name = "John Doe"
    email = "john;doe@x23.com"
    phone = "123-456-7890"

    # Test ExportUserData
    result = ExportUserData.invoke(
        {"full_name": full_name, "email": email, "phone": phone}
    )

    # Verify file doesn't exist
    filename = "user_data.csv"
    assert os.path.exists(filename) == False


# Test agent_invoke
# def test_agent_invoke():
#     response = agent_invoke("What is the return policy?")
#     assert "return most items within 30 days" in response


# Clean up generated files
@pytest.fixture(scope="module", autouse=True)
def cleanup():
    yield
    if os.path.exists("user_data.csv"):
        os.remove("user_data.csv")
