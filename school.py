class School:
  def __init__(self, name=None, roster={}):
    self.name=name
    self.roster=roster

  def add_student(self, name, grade):
    self.roster.setdefault(grade,[]).append(name)

  def grade(self, grade):
    return self.roster[grade]

  def sort_roster(self):
    for key in self.roster.keys():
      self.roster[key].sort()

    return self.roster







