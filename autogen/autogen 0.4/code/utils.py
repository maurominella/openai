def topic_to_string(topic:dict) -> str:
    """
    Given a dictionary with a single element plus a string array,
    returns a string that includes the key plus the strings
    """
    keys = list(topic.keys())
    topic_main = keys[0]
    result = topic_main + ":"
    for t in topic[topic_main]:
        result += f"\n- {t}"
        
    return result