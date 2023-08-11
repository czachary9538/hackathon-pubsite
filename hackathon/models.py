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
    study_level = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    coc = db.Column(db.Boolean)
    share_registration = db.Column(db.Boolean)
    send_emails = db.Column(db.Boolean)
    underrepresented = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    #pronouns = db.Column(db.String, nullable=False)
    #race = db.Column(db.String, nullable=False)
    sexual_identity = db.Column(db.String, nullable=False)
    shirt_size = db.Column(db.String, nullable=False)
    address_line_1 = db.Column(db.String, nullable=False)
    address_line_2 = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    zip_code = db.Column(db.String, nullable=False)
    major = db.Column(db.String, nullable=False)
    dietary_restrictions = db.relationship('DietaryRestrictions', backref='signup', lazy=True)
    pronouns = db.relationship('Pronouns', backref='signup', lazy=True)
    race = db.relationship('Race', backref='signup', lazy=True)

    def __init__(self, form_data):
        pass

class DietaryRestrictions(db.Model):
    __tablename__ = 'dietary'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    signup_id = db.Column(db.Integer)
    vegetarian = db.Column(db.Boolean)
    vegan = db.Column(db.Boolean)
    celiac = db.Column(db.Boolean)
    allergies = db.Column(db.Boolean)
    allergies_explained = db.Column(db.String, nullable=True)
    kosher = db.Column(db.Boolean)
    halal = db.Column(db.Boolean)

    def __init__(self, form_data, signup_id):
        pass

class Pronouns(db.Model):
    __tablename__ = 'pronouns'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    signup_id  = db.Column(db.Integer)
    she_her = db.Column(db.Boolean)
    he_him = db.Column(db.Boolean)
    they_them = db.Column(db.Boolean)
    other = db.Column(db.String, nullable=True)
    prefer_not_to_answer = db.Column(db.Boolean)

    def __init__(self, form_data, signup_id):
        pass

class Race(db.Model):
    __tablename__ = 'race'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    signup_id = db.Column(db.Integer)
    asian_indian = db.Column(db.Boolean)
    black_african = db.Column(db.Boolean)
    chinese = db.Column(db.Boolean)
    filipino = db.Column(db.Boolean)
    guamanian_chamorro = db.Column(db.Boolean)
    hispanic_latino_spanish = db.Column(db.Boolean)
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
    prefer_not_to_answer = db.Column(db.Boolean)

    def __init__(self, form_data, signup_id):
        pass
