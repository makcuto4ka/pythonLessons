# 1
import json
class UserProfile:
    def __init__(self, name , age, interest):
        self.name = name
        self.age = age
        self.interest = interest
        
    def to_dict(self):
        return {'name': self.name, 'age': self.age, 'interest': self.interest}
    
    def from_dict(d):
        return UserProfile(d['name'], d['age'], d['interest'])
    
    @staticmethod
    def save_UserProfiles(UserProfiles, filename="profile.json"):
        with open(filename, "w") as f:
            json.dump([Us.to_dict() for Us in UserProfiles], f)
    @staticmethod
    def load_UserProfiles(filename="profile.json"):
        with open(filename) as f:
            return [UserProfile.from_dict(d) for d in json.load(f)]
    
    def __str__(self):
        return f"{self.name}: {self.age}"
UserProfiles = [UserProfile("Ann",35, [4, 5])]
UserProfile.save_UserProfiles(UserProfiles)
Us = UserProfile.load_UserProfiles()

print(Us[0])
