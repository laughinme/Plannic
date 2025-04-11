from pydantic import BaseModel, Field, field_validator

def convert_dicts(value: dict):
    """
    If given value is dictionary like this: {"001": "name"},
    this method converts it to list of {"id": key, "name": value}.
    """
    if isinstance(value, dict):
        return [{"id": key, "name": val} for key, val in value.items()]
    return value
    

class BasicDict(BaseModel):
    id: str
    name: str


class Schedule(BaseModel):
    teachers: list[BasicDict] = Field(..., alias='TEACHERS')
    subjects: list[BasicDict] = Field(..., alias='SUBJECTS')
    classes: list[BasicDict] = Field(..., alias='CLASSES')
    rooms: list[BasicDict] = Field(..., alias='ROOMS')
    class_groups: list[BasicDict] = Field(..., alias='CLASSGROUPS')
    

    @field_validator(
        'teachers', 
        *['subjects', 'classes', 'rooms', 'class_groups'],
        mode='before'
    )
    @classmethod
    def convert_basic_dicts(cls, value: dict):
        return convert_dicts(value)


# import json
# path = 'nika.json'

# with open(path, 'r', encoding='utf-8') as file:
#     try:
#         content = json.load(file)
#     except Exception as e:
#         print(e)
#         content = json.loads(str(file.read().split("=", 1)[1].strip().rstrip(";"))) # remove odd js file elements
        
# print(Schedule(**content).teachers)
