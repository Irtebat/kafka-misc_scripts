import json

def json_serializer(obj,ctx):
    return json.dumps(obj).encode('utf-8')

def delivery_report(err, event):
    if err is not None:
        print(f'Delivery failed on reading for {event.key().decode("utf8")}: {err}')
    else:
        print(f'Delivery succeeded {event.key().decode("utf8")} produced to {event.topic()}')
