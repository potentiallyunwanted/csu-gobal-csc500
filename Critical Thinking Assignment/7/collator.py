#list of courses
#csc101, csc102, csc103, net110, com241
#list of rooms
#3004, 4501, 6755, 1244, 1411
#list of instructors
#Haynes, Alvarado, Rich, Burke, Lee
#list of meeting times
#8:00am, 9:00am, 10:00am, 11:00am, 1:00pm
#create a collator class that will store the lists of courses, rooms, instructors, and meeting times
#method that creates key-value pairs for each course, room, instructor, and meeting time
#method that returns the instructor, room, and meeting time for a specific course

class Collator:
    def __init__(self):
        self.courses = ["csc101", "csc102", "csc103", "net110", "com241"]
        self.rooms = ["3004", "4501", "6755", "1244", "1411"]
        self.instructors = ["Haynes", "Alvarado", "Rich", "Burke", "Lee"]
        self.meeting_times = ["8:00am", "9:00am", "10:00am", "11:00am", "1:00pm"]
    
    def create_course_info(self):
        rooms = {}
        instructors = {}
        meeting_times = {}
        for i in range(len(self.courses)):
            rooms[self.courses[i]] = self.rooms[i]
            instructors[self.courses[i]] = self.instructors[i]
            meeting_times[self.courses[i]] = self.meeting_times[i]
        return rooms, instructors, meeting_times
    
    def get_course_info(self, course):
        rooms, instructors, meeting_times = self.create_course_info()
        return f"""
                Details for {course}:
                -------------------------------------------------
                Instructor: {instructors[course]}
                Room #: {rooms[course]}
                Time: {meeting_times[course]}"""
                
def main():
    collator = Collator()
    course = input("Enter a course: ")
    print(collator.get_course_info(course))
    
if __name__ == "__main__":
    main()