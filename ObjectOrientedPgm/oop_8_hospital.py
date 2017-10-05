# import random module to generate names for list of patients
import random

class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)

class Patient(object):
    __metaclass__ = IterRegistry
    _registry = []
    def __init__(self, name):
        self.id = id(self)
        self.name = name
        self.allergies = []
        self.bed_number = 5
        self._registry.append(self)
    def add_allergies(self, *allergies):
        self.allergies.append(', '.join(allergies))
        return self
    def assign_bed_number(self, assigned_bed):
        self.bed_number = assigned_bed
        return self
    


class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.patients = []
        self.capacity = capacity
        self.beds_assigned = []
    def create_patient(self, name):
        # create new patient record instance
        if not is_patient_record_exist(name):
            # determine whether patient already has a record by name
            Patient(name)
            return self
        else:
            print "The patient already has a record. A new record is not needed and will not be saved."
            return -2
    def admit_patient(self, name):
        # admit patients to the hospital (add to patients attribute)
        if not is_patient_record_exist(name):
            print "The patient does not have a record and cannot be admitted. Please create a patient record before attempting to admit the patient."
            return -1
        if len(self.patients) > self.capacity:
            # determine whether hospital has reached capacity
            patient_size_error()
            return -1
        self.patients.append(search_for_patient(name))
        assigned_bed = self.find_empty_bed()
        search_for_patient(name).assign_bed_number(assigned_bed)
        self.beds_assigned.append(assigned_bed)
        # print self.beds_assigned
        return self
    def discharge_patient(self, name):
        # discharge patient by name -- using search helper function
        self.patients.remove(search_for_patient(name))
        search_for_patient(name).bed_number = None
        return self
    def display_patient_list(self):
        # display list of admitted patients and bed number
        print "___ LIST OF CURRENTLY ADMITTED PATIENTS AT " + self.name + " ___"
        count = 0
        for patient_rec in self.patients:
            print patient_rec.name + " - Bed #" + str(patient_rec.bed_number)
            count += 1
        print "___ TOTAL ADMITTED PATIENTS = " + str(count) + " ___"
        return self
    def find_empty_bed(self):
        if not self.beds_assigned:
            return 1
        for i in range(1, self.capacity):
            flag_is_in_list = False
            for j in range(0, len(self.beds_assigned)):
                # print "i = " + str(i) + " and beds_assigned[" + str(j) + "] = " + str(self.beds_assigned[j])
                if i == self.beds_assigned[j]:
                    flag_is_in_list = True
            if not flag_is_in_list:
                return i
        return None



def is_patient_record_exist(name):
    # search for existing patient in Patient class by name
    for patient_rec in Patient:
        if patient_rec.name == name:
            return True
    return False
def key_no_line(key):
    # return the key name without any underscores
    # replace with spaces
    return key.replace("_", " ")
def patient_size_error():
    # generate message to user that hospital capacity exceeded
    print "The hospital cannot accept any more patients!"
    print "The capacity is full. This patient has not been admitted."
def search_for_patient(name):
    # search for patient record and return Person instance (object)
    for patient_rec in Patient:
        if patient_rec.name == name:
            return patient_rec
    return -1


# instantiate new calls using random list generators
# random list of 30 names
names_list = [
    'Yasuko Mcglown',
    'Bart Tompson',
    'Williemae Ashmore',
    'Jona Ullery',
    'Belle Mcguire',
    'Kelli Odonoghue',
    'Billy Drummond',
    'Carlita Wiles',
    'Marianne Peete',
    'Carmelita Durocher',
    'Fernando Whitton',
    'Andree Willis',
    'Colette Gaudet',
    'Lionel Leininger',
    'Nancy Rollison',
    'Georgina Teixeira',
    'Kaley Lukes',
    'Kamilah Mcpeak',
    'Lance Tower',
    'Dolores Anding',
    'Danette Findlay',
    'Tanner Dipasquale',
    'Berry Lintner',
    'Lauralee Trumbo',
    'Josephine Cushing',
    'Drema Pottinger',
    'Sommer Tingey',
    'Sherrill Poat',
    'Jinny Peiffer',
    'Louie Pillai'
]


# generate hospital
hospital_1 = Hospital('Memorial Hospital', 50)
hospital_2 = Hospital('St. Francis Hospital', 25)

# generate random patients
num_patients = 20
for i in range(num_patients):
    rand_name = names_list[random.randint(0, len(names_list)-1)]
    obj_create = hospital_1.create_patient(rand_name)
    # obj_create = hospital_1.admit_patient(names_list[random.randint(0, len(names_list)-1)])
    # if the __init__ method returns -1, there was queue size error; break
    if obj_create == -1:
        break
    # if the create_patient method returns -2, the patient currently has a record; go to the next name
    if obj_create == -2:
        continue
    hospital_1.admit_patient(rand_name)

# generate full patient list for hospital
hospital_1.display_patient_list()

# admit and discharge a patient
hospital_1.create_patient('John').admit_patient('John').display_patient_list().discharge_patient('John').display_patient_list()
