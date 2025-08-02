import requests

def get_summary(book, chapter):
   
    base_url = "https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/"
    
    # Clean the inputs to match what the API expects
    book = book.strip().lower().replace(" ", "")
    chapter = chapter.strip()
    
    if not chapter.isdigit():
        raise ValueError("Chapter must be a number.")
    # Ensure chapter is a valid number

    full_url = base_url + book + "/" + chapter 
      

    response = requests.get(full_url) 

    # If the request failed (e.g., 404), raise an error
    if response.status_code != 200:
        raise ValueError("Invalid book or chapter.")

    data = response.json()
   
    if 'summary' not in data:
        raise ValueError("No summary found for this book and chapter.")
    
    summary = data['summary']
    reference = f"{book.title()} {chapter}"
    
    return reference, summary


def run_summary_tool():
    print("Welcome to the Book of Mormon Summary Tool!")
    
    keep_going = True
    while keep_going:
        try:
            book = input("Which book of the Book of Mormon would you like? ")
            chapter = input("Which chapter of " + book + " are you interested in? ")
            
            reference, summary = get_summary(book, chapter)
            print("")
            print("\nSummary for " + reference + ":")
            print(summary)
        except (ValueError, KeyError):
            print("Sorry, we could not find that book or chapter.")
        except Exception as e:
            print("There was an error: " + str(e))

        again = input("\nWould you like to view another (Y/N)? ")
        if again != "Y" and again != "y":
            keep_going = False
            print("Thank you for using Book of Mormon Summary Tool!")


# Only run the interactive part if this script is the main one being executed
if __name__ == "__main__":
    run_summary_tool()































