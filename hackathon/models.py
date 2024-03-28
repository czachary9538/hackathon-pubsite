from hackathon import db

class SignUp(db.Model):
    __tablename__ = 'signup'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    university = db.Column(db.String, nullable=False)
    shirt_size = db.Column(db.String, nullable=False)
    study_level = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    coc = db.Column(db.Boolean)
    share_registration = db.Column(db.Boolean)
    send_emails = db.Column(db.Boolean)
    dietary_restrictions = db.relationship('DietaryRestrictions', backref='signup', lazy=True)
    underrepresented = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    pronouns = db.Column(db.String, nullable=False)
    race = db.relationship('Race', backref='signup', lazy=True)
    orientation = db.relationship('Orientation', backref='signup', lazy=True)
    highest_level = db.Column(db.String, nullable=False)
    major = db.relationship('Major', backref='signup', lazy=True)



    def __init__(self, form_data):
        self.first_name = form_data['firstName']
        if len(self.first_name) == 0:
            raise ValueError("Missing first_name")
        self.last_name = form_data['lastName']
        if len(self.last_name) == 0:
            raise ValueError("Missing last_name")
        self.email = form_data['email']
        if len(self.email) == 0:
            raise ValueError("Missing email")
        self.age = form_data['age']
        if len(self.age) == 0:
            raise ValueError("Missing age")
        self.phone_number = form_data['phoneNumber']
        if len(self.phone_number) == 0:
            raise ValueError("Missing phone_number")
        self.university = form_data['university']
        if len(self.university) == 0:
            raise ValueError("Missing university")
        self.shirt_size = form_data['shirtSize']
        if len(self.shirt_size) == 0:
            raise ValueError("Missing shirt_size")
        self.study_level = form_data['currentStudyLevel']
        if len(self.study_level) == 0:
            raise ValueError("Missing study_level")
        self.country = form_data['country']
        if len(self.country) == 0:
            raise ValueError("Missing country")
        self.coc = form_data['mlh1']
        if not self.coc:
            raise ValueError("Missing coc")
        self.share_registration = form_data['mlh2']
        if not self.share_registration:
            raise ValueError("Missing share_registration")
        self.send_emails = form_data['mlh3']
        if not self.send_emails:
            raise ValueError("Missing send_emails")
        self.underrepresented = form_data['underrep']
        if len(self.underrepresented) == 0:
            raise ValueError("Missing underrepresented")
        self.gender = form_data['gender']
        if len(self.gender) == 0:
            raise ValueError("Missing gender")
        self.pronouns = form_data['pronouns']
        if self.pronouns == 'other':
            self.pronouns = form_data['pronounsOther']
        if len(self.pronouns) == 0:
            raise ValueError("Missing pronouns")
        self.highest_level = form_data['highestEdu']
        if self.highest_level == 'other':
            self.highest_level = form_data['eduOther']
        if len(self.highest_level) == 0:
            raise ValueError("Missing highest_level")
        



class DietaryRestrictions(db.Model):
    __tablename__ = 'dietary'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    signup_id = db.Column(db.Integer, db.ForeignKey('signup.id'), nullable=False)
    vegetarian = db.Column(db.Boolean)
    vegan = db.Column(db.Boolean)
    celiac = db.Column(db.Boolean)
    kosher = db.Column(db.Boolean)
    halal = db.Column(db.Boolean)
    lactose = db.Column(db.Boolean)
    nuts = db.Column(db.Boolean)
    other = db.Column(db.String, nullable=True)




    def __init__(self, form_data, signup_id):
        self.signup_id = signup_id
        self.vegetarian = 'vegetarian' in form_data['dietary']
        self.vegan = 'vegan' in form_data['dietary']
        self.celiac = 'celiac' in form_data['dietary']
        self.kosher = 'kosher' in form_data['dietary']
        self.halal = 'halal' in form_data['dietary']
        self.lactose = 'lactose' in form_data['dietary']
        self.nuts = 'nuts' in form_data['dietary']
        if 'other' in form_data['dietary']:
            self.other = form_data['dietaryOther']
        else:
            self.other = None


class Race(db.Model):
    __tablename__ = 'race'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    signup_id = db.Column(db.Integer, db.ForeignKey('signup.id'), nullable=False)
    asian_indian = db.Column(db.Boolean)
    black_african = db.Column(db.Boolean)
    chinese = db.Column(db.Boolean)
    filipino = db.Column(db.Boolean)
    guamanian_chamorro = db.Column(db.Boolean)
    hispanic_latino = db.Column(db.Boolean)
    japanese = db.Column(db.Boolean)
    korean = db.Column(db.Boolean)
    middle_eastern = db.Column(db.Boolean)
    native_american_alaskan = db.Column(db.Boolean)
    native_hawaiian = db.Column(db.Boolean)
    samoan = db.Column(db.Boolean)
    vietnamese = db.Column(db.Boolean)
    white = db.Column(db.Boolean)
    other_asian = db.Column(db.Boolean)
    other_pacific_island = db.Column(db.Boolean)
    other = db.Column(db.String, nullable=True)
    prefer_not_answer = db.Column(db.Boolean)

    def __init__(self, form_data, signup_id):
        self.signup_id = signup_id
        self.asian_indian = 'asian_indian' in form_data['race']
        self.black_african = 'black_african' in form_data['race']
        self.chinese = 'chinese' in form_data['race']
        self.filipino = 'filipino' in form_data['race']
        self.guamanian_chamorro = 'guamanian_chamorro' in form_data['race']
        self.hispanic_latino = 'hispanic_latino' in form_data['race']
        self.japanese = 'japanese' in form_data['race']
        self.korean = 'korean' in form_data['race']
        self.middle_eastern = 'middle_eastern' in form_data['race']
        self.native_american_alaskan = 'native_american_alaskan' in form_data['race']
        self.native_hawaiian = 'native_hawaiian' in form_data['race']
        self.samoan = 'samoan' in form_data['race']
        self.vietnamese = 'vietnamese' in form_data['race']
        self.white = 'white' in form_data['race']
        self.other_asian = 'other_asian' in form_data['race']
        self.other_pacific_island = 'other_pacific_islander' in form_data['race']
        self.prefer_not_answer = 'prefer_not_answer' in form_data['race']
        if 'other' in form_data['race']:
            self.other = form_data['raceOther']
        else:
            self.other = None
        if not any((self.asian_indian, self.black_african, self.chinese, self.filipino, self.guamanian_chamorro,
                   self.hispanic_latino, self.japanese, self.korean, self.middle_eastern, self.native_american_alaskan,
                   self.native_hawaiian, self.samoan, self.vietnamese, self.white, self.other_asian, self.other_pacific_island,
                   self.prefer_not_answer, self.other)):
            return ValueError("No option selected, or missing other field box")


class Orientation(db.Model):
    __tablename__ = 'orientiation'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    signup_id = db.Column(db.Integer, db.ForeignKey('signup.id'), nullable=False)
    heterosexual = db.Column(db.Boolean)
    gay_lesbian = db.Column(db.Boolean)
    bisexual = db.Column(db.Boolean)
    other = db.Column(db.String, nullable=True)
    prefer_not_answer = db.Column(db.Boolean)

    def __init__(self, form_data, signup_id):
        self.signup_id = signup_id
        self.heterosexual = 'heterosexual' in form_data['orientation']
        self.gay_lesbian = 'gay_lesbian' in form_data['orientation']
        self.bisexual = 'bisexual' in form_data['orientation']
        self.other = 'other' in form_data['orientation']
        self.prefer_not_answer = 'prefer_not_answer' in form_data['orientation']
        if 'other' in form_data['orientation']:
            self.other = form_data['orientationOther']
        else:
            self.other = None
        if not any((self.heterosexual, self.gay_lesbian, self.bisexual, self.other, self.prefer_not_answer, self.other)):
            return ValueError("No option selected, or missing other field box")

class Major(db.Model):
    __tablename__ = 'major'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    signup_id = db.Column(db.Integer, db.ForeignKey('signup.id'), nullable=False)
    cs_ce_se = db.Column(db.Boolean)
    other_eng = db.Column(db.Boolean)
    is_it_sysadmin = db.Column(db.Boolean)
    nat_sci = db.Column(db.Boolean)
    math = db.Column(db.Boolean)
    web_dev = db.Column(db.Boolean)
    business = db.Column(db.Boolean)
    humanities = db.Column(db.Boolean)
    social_sci = db.Column(db.Boolean)
    fine_art = db.Column(db.Boolean)
    health_sci = db.Column(db.Boolean)
    undecided_none = db.Column(db.Boolean)
    no_major = db.Column(db.Boolean)
    other = db.Column(db.String, nullable=True)
    prefer_not_answer = db.Column(db.Boolean)

    def __init__(self, form_data, signup_id):
        self.signup_id = signup_id
        self.cs_ce_se = 'cs_ce_se' in form_data['major']
        self.other_eng = 'other_eng' in form_data['major']
        self.is_it_sysadmin = 'is_it_sysadmin' in form_data['major']
        self.nat_sci = 'nat_sci' in form_data['major']
        self.math = 'math' in form_data['major']
        self.web_dev = 'web_dev' in form_data['major']
        self.business = 'business' in form_data['major']
        self.humanities = 'humanities' in form_data['major']
        self.social_sci = 'social_sci' in form_data['major']
        self.fine_art = 'fine_art' in form_data['major']
        self.health_sci = 'health_sci' in form_data['major']
        self.undecided_none = 'undecided_none' in form_data['major']
        self.no_major = 'no_major' in form_data['major']
        self.prefer_not_answer = 'prefer_not_answer' in form_data['major']
        if 'other' in form_data['major']:
            self.other = form_data['majorOther']
        else:
            self.other = None
        if not any((self.cs_ce_se, self.other_eng, self.is_it_sysadmin, self.nat_sci, self.math, self.web_dev, self.business,
                   self.humanities, self.social_sci, self.fine_art, self.health_sci, self.undecided_none, self.no_major,
                   self.prefer_not_answer, self.other)):
            return ValueError("No option selected, or missing other field box")
        


class photoConsent(db.Model):
    __tablename__ = 'photo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    signup_id = db.Column(db.Integer, db.ForeignKey('signup.id'), nullable=False)
    
    yes = db.Column(db.Boolean)
    no = db.Column(db.Boolean)
   
    def __init__(self, form_data, signup_id):
        self.signup_id = signup_id
        self.yes = 'yes' in form_data['photo']
        self.no = 'no' in form_data['photo']

        if not any((self.yes, self.no)):
            return ValueError("No option selected, or missing other field box")
