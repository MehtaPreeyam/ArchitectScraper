from enum import Enum

class Category(Enum):
    AllergyCare = 'Allergy Care'
    BoneJointMuscular = 'Bone, Joint, and Muscular'
    Cancer = 'Cancer'
    HearingAndVision = 'Hearing and Vision'
    HeartHealth = 'Heart Health'
    HormoneHealth = 'Hormone Health'
    MensHealth = "Men's Health"
    MentalHealthAndNeurological = 'Mental Health and Neurological'
    NephrologyUrology = 'Nephrology and Urology'
    OralCare = 'Oral Care'
    PrimaryCare = 'Primary Care'
    Respiratory = 'Respiratory'
    Skincare = 'Skincare'
    Sleep = 'Sleep'
    StomachDigestion = 'Stomach and Digestion'
    WeightManagement = 'Weight Management'
    WomensHealth = "Women's Health"
    Other = "Other"

class AllergyCare(Enum):
    Allergy_Testing = 'Allergy Testing'
    Allergy_Treatment = 'Allergy Treatment'
    Not_Sure_Other = 'Not Sure / Other'

class BoneJointMuscular(Enum):
    Acute_Pain = 'Acute Pain'
    Chronic_Pain = 'Chronic Pain'
    Osteoporosis = 'Osteoporosis'
    Physical_Therapy = 'Physical Therapy'
    Not_Sure_Other = 'Not Sure / Other'

class Cancer(Enum):
    Bladder_Health = 'Bladder Health'
    Breast_Health = 'Breast Health'
    Fertility = 'Fertility'
    Liver_Issues = 'Liver Issues'
    Not_Sure_Other = 'Not Sure / Other'

class HearingAndVision(Enum):
    Blurred_Vision_Vision_Loss = 'Blurred Vision / Vision Loss'
    Cataracts = 'Cataracts'
    Dry_Eyes = 'Dry Eyes'
    Glaucoma = 'Glaucoma'
    Hearing_Loss = 'Hearing Loss'
    Macular_Degeneration = 'Macular Degeneration'
    Vertigo = 'Vertigo'
    Not_Sure_Other = 'Not Sure / Other'

class HeartHealth(Enum):
    Chest_Pain = 'Chest Pain'
    Heart_Arrhythmia = 'Heart Arrhythmia'
    Heart_Attack_Recovery = 'Heart Attack Recovery'
    Heart_Disease = 'Heart Disease'
    High_Blood_Pressure = 'High Blood Pressure'
    High_Cholesterol = 'High Cholesterol'
    Stroke = 'Stroke'
    Not_Sure_Other = 'Not Sure / Other'

class HormoneHealth(Enum):
    Thyroid_Disease = 'Thyroid Disease'
    Type_1_Diabetes = 'Type 1 Diabetes'
    Type_2_Diabetes = 'Type 2 Diabetes'
    Low_Testosterone_Hormone_Health = 'Low Testosterone / Hormone Health'
    Not_Sure_Other = 'Not Sure / Other'

class MensHealth(Enum):
    Balding = 'Balding'
    Erectile_Dysfunction = 'Erectile Dysfunction'
    Male_Fertility_Issues = 'Male Fertility Issues'
    Not_Sure_Other = 'Not Sure / Other'

class MentalHealthAndNeurological(Enum):
    Addiction_Substance_Use = 'Addiction (alcohol, nicotine, opioids, etc.) / Substance Use'
    ADHD_ADD = 'ADHD / ADD'
    Alzheimer_Parkinson = "Alzheimer's & Parkinson's"
    Anxiety = 'Anxiety'
    Bipolar_Disorder = 'Bipolar Disorder'
    Depression = 'Depression'
    Pediatric_Mental_Health = 'Pediatric Mental Health'
    Psychiatry_Medication_Management = 'Psychiatry and Medication Management'
    Seizures = 'Seizures'
    Not_Sure_Other = 'Not Sure / Other'

class NephrologyUrology(Enum):
    Chronic_Kidney_Disease = 'Chronic Kidney Disease'
    Kidney_Stones = 'Kidney stones'
    Urinary_Incontinence = 'Urinary incontinence'
    Not_Sure_Other = 'Not Sure / Other'

class OralCare(Enum):
    Cavities = 'Cavities'
    Oral_Decay = 'Oral Decay'
    Teeth_Grinding = 'Teeth Grinding'
    Teeth_Realignment = 'Teeth Realignment'
    Teeth_Whiteness = 'Teeth Whiteness'
    Not_Sure_Other = 'Not Sure / Other'

class PrimaryCare(Enum):
    General_Primary_Care = 'General Primary Care'
    Immunizations_Vaccinations = 'Immunizations / Vaccinations'
    Pediatrics = 'Pediatrics'
    Prenatal_Pregnancy_Postnatal_Support = 'Prenatal, Pregnancy, and Postnatal Support'
    Reproductive_Sexual_Health = 'Reproductive and Sexual Health'
    Not_Sure_Other = 'Not Sure / Other'

class Respiratory(Enum):
    Asthma = 'Asthma'
    COPD = 'Chronic Obstructive Pulmonary Disease (COPD)'
    Difficulty_Breathing = 'Difficulty Breathing'
    Nasal_Congestion = 'Nasal Congestion'
    Wheezing = 'Wheezing'
    Not_Sure_Other = 'Not Sure / Other'

class Skincare(Enum):
    Acne = 'Acne'
    Dark_Spots = 'Dark Spots'
    Dermatitis = 'Dermatitis'
    Eczema = 'Eczema'
    Rosacea = 'Rosacea'
    Skin_Dryness = 'Skin Dryness'
    Skin_Rashes = 'Skin Rashes'
    General_Skincare = 'General Skincare'
    Not_Sure_Other = 'Not Sure / Other'

class Sleep(Enum):
    Insomnia = 'Insomnia'
    Poor_Quality_Sleep = 'Poor Quality Sleep'
    Sleep_Apnea = 'Sleep Apnea'
    Sleep_Walking_Talking = 'Sleep Walking/Talking'
    Snoring = 'Snoring'
    General_Sleep_Support = 'General Sleep Support'
    Not_Sure_Other = 'Not Sure / Other'

class StomachDigestion(Enum):
    Bacterial_Viral_Infections = 'Bacterial or Viral Infections'
    Constipation = 'Constipation'
    Diarrhea_Loose_Stools = 'Diarrhea/Loose Stools'
    Gallstones = 'Gallstones'
    Heartburn_Acid_Reflux = 'Heartburn / Acid Reflux'
    Inflammatory_Bowel_Disease_IBD = 'Inflammatory Bowel Disease (IBD)'
    Irritable_Bowel_Syndrome_IBS = 'Irritable Bowel Syndrome (IBS)'
    Not_Sure_Other = 'Not Sure / Other'

class WeightManagement(Enum):
    Anemia = 'Anemia'
    Bloating = 'Bloating'
    Eating_Disorder = 'Eating Disorder (Anorexia, Bulimia, Extreme Dieting, etc.)'
    Weight_Loss = 'Weight Loss'
    Not_Sure_Other = 'Not Sure / Other'

class WomensHealth(Enum):
    Menopause = 'Menopause'
    Ovarian_Health = 'Ovarian Health'
    Pelvic_Floor_Therapy = 'Pelvic Floor Therapy'
    PMS_Menstruation = 'PMS/Menstruation'
    Vaginal_Health_Discomfort = 'Vaginal Health / Discomfort'
    Not_Sure_Other = 'Not Sure / Other'



category_dict = {}

for category in Category:
    category_name = category.value
    
    subcategories = []
    
    # Get the corresponding enum for the current category
    subcategory_enum = globals()[category.name]
    
    for subcategory in subcategory_enum:
        subcategories.append(subcategory.value)
    
    category_dict[category_name] = subcategories

print(category_dict)