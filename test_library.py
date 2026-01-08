from library import library_details

def test_library_details():
    # Define test data
    book_id = 101
    title = "The Great Gatsby"
    name = "F. Scott Fitzgerald"
    year = 1925
    
    # Define the expected single string output
    expected_output = (
        f"Book Id:{book_id}\n"
        f"Book title:{title}\n"
        f"Author name:{name}\n"
        f"Published year:{year}"
    )
    
    # Assert that the function return matches the expected string
    assert library_details(book_id, title, name, year) == expected_output
