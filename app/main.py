"""Basic WASM test for Python"""
# import json

def getConfig():
    '''Return the settings as a JSON string'''
    return "OK"

def handler(phrase, label_candidates_json):
    '''Classify the phrase with the given label candidates'''
    # return json.dumps({ 'phrase': phrase, 'label_candidates': label_candidates_json })
    return "NICE"
