from sqlalchemy.exc import IntegrityError
from model import Applicant, Education, Skill, Work_experience, Reference, dbconnect
from sqlalchemy.orm.exc import NoResultFound
def addApplicant(applicant_dict):
    applicant = Applicant()
    # Add attributes
    applicant.name = applicant_dict["name"]
    applicant.email = applicant_dict["email"]
    applicant.phone_number = applicant_dict["phone_number"]
    applicant.linked_in = applicant_dict["linked_in"]
    applicant.location = applicant_dict["location"]
    applicant.summary = applicant_dict["summary"]
    return applicant
    
def addEducation(education_dict):
    education = Education()
    # Add attributes
    education.school = education_dict["school"]
    education.qualification = education_dict["qualification"]
    education.duration = education_dict["duration"]
    return education

def addSkill(skill_dict):
    skill = Skill()
    # Add attributes
    skill.skill_name = skill_dict["skill_name"]
    skill.score = skill_dict["score"]
    return skill

def addWorkExperience(work_experience_dict):
    work_experience = Work_experience()
    # Add attributes
    work_experience.company = work_experience_dict["company"]
    work_experience.role = work_experience_dict["role"]
    work_experience.duration = work_experience_dict["duration"]
    work_experience.description = work_experience_dict["description"]
    return work_experience

def addReference(reference_dict):
    reference = Reference()
    # Add attributes
    reference.name = reference_dict["name"]
    reference.number = reference_dict["number"]
    reference.email = reference_dict["email"]
    reference.position = reference_dict["position"]
    return reference