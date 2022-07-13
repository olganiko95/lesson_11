import json

def load_candidates_from_json():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def get_candidate(candidate_id):
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate

def get_candidates_by_name(candidate_name):
    result=[]
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate['name'] == candidate_name:
            result.append(candidate)
    return result

def get_candidates_by_skill(skill_name):
    result = []
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if skill_name in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result

