import json
import hashlib
from models import Schedule, WeekDay, Hash
from dataclasses import dataclass


def setup_lessons(
    class_id: str,
    lesson_number: int,
    day: WeekDay,
    lesson
) -> list[Schedule]:
    
    lessons: list[Schedule] = []
    for i, subject_id in enumerate(lesson["s"]):
        group_id = None
        if "g" in lesson:
            if i > 1: break
            
            group_id = lesson["g"][i]
            if group_id == "0":
                group_id = "3"
            elif group_id == "1":
                group_id = "4"
            elif group_id == "2":
                    continue
        
        if subject_id == "":
            lessons.append(
                Schedule(
                    class_id=class_id,
                    day=day,
                    lesson_number=lesson_number,
                    group_id=group_id or None,
                    is_active=False
                )
            )
            continue
            
        lessons.append(
            Schedule(
                class_id=class_id,
                day=day,
                lesson_number=lesson_number,
                subject_id=subject_id or None,
                teacher_id=lesson["t"][i] or None,
                classroom_id=lesson["r"][i] or None,
                group_id=group_id or None,
            )
        )
        
    if len(lessons) > 1:
        lessons.sort(key=lambda x: int(x.group_id))
        
    return lessons


def lessons_equal(old: Schedule, new: Schedule):
    return (
        old.class_id == new.class_id
        and old.day == new.day
        and old.lesson_number == new.lesson_number
        and old.subject_id == new.subject_id
        and old.teacher_id == new.teacher_id
        and old.group_id == new.group_id
        and old.classroom_id == new.classroom_id
        and old.is_active == new.is_active
    )

def compute_hash(data: dict) -> str:
    """Compute MD5 hash of the data."""
    
    stringified = json.dumps(data, ensure_ascii=True, sort_keys=True)
    m = hashlib.md5()
    m.update(stringified.encode('utf-8'))
    return m.hexdigest()


# @dataclass
# class Hashes(object):
#     schedule: str
#     exchanges: str
#     teachers: str
#     subjects: str
#     classes: str
#     rooms: str
#     classgroups: str
#     periods: str
#     lesson_times: str

def generate_hashes(content: dict) -> Hash:
    return Hash(
        schedule = compute_hash(content["CLASS_SCHEDULE"]),
        exchanges = compute_hash(content["CLASS_EXCHANGE"]),
        teachers = compute_hash(content["TEACHERS"]),
        subjects = compute_hash(content["SUBJECTS"]),
        classes = compute_hash(content["CLASSES"]),
        rooms = compute_hash(content["ROOMS"]),
        classgroups = compute_hash(content["CLASSGROUPS"]),
        periods = compute_hash(content["PERIODS"]),
        lesson_times = compute_hash(content["LESSON_TIMES"])
    )
    