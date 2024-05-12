from datetime import datetime

# global var that is reset
activity_metadata = {
    "activity": "None",
    "book": "None",
    "start_time": None,
    "location": None,
    "people": None,
}

'''
At the moment that we need to create a storage index of something we want to track,
call this function to get the metadata of the activity.
'''
def get_activity_metadata():
    date = datetime.now()
    md_copy = activity_metadata.copy()
    md_copy["start_time"] = date
    return md_copy

'''
Function to set the context for what is being recorded.
Triggered by a hand motion, and validated/inferred if there is large deviation
'''
def set_activity_metadata():
    return