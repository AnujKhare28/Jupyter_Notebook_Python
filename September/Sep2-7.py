class Courses:
    def __init__(self, name, dur, *books):
        self.course_name = name
        self.duration = dur
        self.books = [self.Book(b) for b in books]

    def show_details(self):
        print("Name:", self.course_name)
        print("Duration:", self.duration)
        print("Suggested books:")
        for b in self.books: 
            print(b)

    class Book:
        def __init__(self,title):
            self.title = title

        def __str__(self):
            return self.title
        
c1 = Courses('Python', 10, 'Python Essentials', 'Python Crashcourse', 'Python Practice Series')
c1.show_details()