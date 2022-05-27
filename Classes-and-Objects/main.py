class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age:int, tracks:list, score):
        assert type(age) == int, "Age must be an integer"
        assert type(tracks) == list or tuple, "Tracks should be a list with at least one item"
        assert type(score) == float or int, "Score should be a number"

        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    def change_name(self, new_name):
        self.name = new_name
    
    def change_age(self, new_age):
        self.age = new_age

    def add_track(self, track):
        self.tracks.append(track)
    
    def get_score(self):
        print(f"The score of {self.name} is {self.score}.")



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print(Bob.tracks)
