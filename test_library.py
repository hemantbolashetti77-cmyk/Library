from library import library_details

def test_library_details():
    id = 101
    title = "The Great Gatsby"
    name = "F. Scott Fitzgerald"
    year = 1925
    
    expected_output = (
        f"Book Id:{id}\n"
        f"Book title:{title}\n"
        f"Author name:{name}\n"
        f"Published year:{year}"
    )
    assert library_details(id, title, name, year) == expected_output
