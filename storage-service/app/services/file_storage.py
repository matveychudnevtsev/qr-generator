# Placeholder for file storage logic

def save_file(data: bytes, filename: str):
    with open(filename, 'wb') as f:
        f.write(data)
