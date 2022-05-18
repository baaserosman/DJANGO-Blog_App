import uuid

def get_random_code():
    code = str(uuid.uuid4())[:15].replace("-","")
    return code