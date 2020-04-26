from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Your classes here

association_table1 = db.Table('course_student', db.Model.metadata,
                              db.Column('course_id', db.Integer,
                                        db.ForeignKey('course.id')),
                              db.Column('student_id', db.Integer,
                                        db.ForeignKey('user.id'))
                              )

association_table2 = db.Table('course_instructor', db.Model.metadata,
                              db.Column('course_id', db.Integer,
                                        db.ForeignKey('course.id')),
                              db.Column('instructor_id', db.Integer,
                                        db.ForeignKey('user.id'))
                              )


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    assignments = db.relationship('Assignment',
                                  cascade='delete')
    instructors = db.relationship(
        'User', secondary=association_table2, back_populates='courses_ins')
    students = db.relationship(
        'User', secondary=association_table1, back_populates='courses_stu')

    def __init__(self, **kwargs):
        self.code = kwargs.get('code', '')
        self.name = kwargs.get('name', '')

    def serialize(self):
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'assignments': [a.serialize() for a in self.assignments],
            'instructors': [i.serialize() for i in self.instructors],
            'students': [s.serialize() for s in self.students]
        }

    def sim_serialize(self):
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
        }


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    netid = db.Column(db.String, nullable=False)
    courses_stu = db.relationship(
        'Course', secondary=association_table1, back_populates='students')
    courses_ins = db.relationship(
        'Course', secondary=association_table2, back_populates='instructors')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.netid = kwargs.get('netid', '')

    def serialize(self):
        ins_course_list = [c.sim_serialize() for c in self.courses_ins]
        stu_course_list = [s.sim_serialize() for s in self.courses_stu]
        return {
            'id': self.id,
            'name': self.name,
            'netid': self.netid,
            'courses': ins_course_list + stu_course_list
        }


# class Student(db.Model):
#     __tablename__ = 'student'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     netid = db.Column(db.String, nullable=False)
#     courses = db.relationship('Course', secondary=course_student, back_populates 'Student')

#     def __init__(self, **kwargs):
#         self.name = kwargs.get('name', '')
#         self.netid = kwargs.get('netid', '')

#     def serialize(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'netid': self.netid,
#             'courses': [s.serialize() for s in self.courses]
#         }


class Assignment(db.Model):
    __tablename__ = 'assignment'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    due_date = db.Column(db.Integer, nullable=False)
    course = db.Column(db.Integer, db.ForeignKey('course.id'))

    def __init__(self, **kwargs):
        self.title = kwargs.get('title', '')
        self.due_date = kwargs.get('due_date', '')

    def serialize(self):
        course_ob = Course.query.filter_by(id=course_id).first()

        return {
            'id': self.id,
            'title': self.title,
            'due_date': self.due_date,
            'course': course_ob.sim_serialize()
        }
