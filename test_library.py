# test_library_details.py

# Assuming the previous code snippet is saved as 'library.py'
from library import library_details 

def test_library_details():
    id = 101
    title = "The Great Gatsby"
    name = "F. Scott Fitzgerald"
    year = 1925
    
    # This is the EXACT string expected from your function
    expected_output = (
        f"Book Id:{id}\n"
        f"Book title:{title}\n"
        f"Author name:{name}\n"
        f"Published year:{year}" # Note: No trailing newline here
    )
    
    # This line will raise an AssertionError if the strings are different
    assert library_details(id, title, name, year) == expected_output
    print("Test passed!")

if __name__ == "__main__":
    test_library_details()
