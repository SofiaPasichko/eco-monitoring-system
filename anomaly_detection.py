def detect(value, threshold):
    if value is None:
        return "NO DATA"
    return "ALERT" if value > threshold else "OK"