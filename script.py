from user.models import CustomUser,Student,Teacher, FeeTable,Semester,Subject
from library.models import BookInstance,Books
c_list = []
 
# for i in range(10):
#     user = CustomUser(first_name='Student'+str(i), 
#                 last_name='Student'+str(i),
#                 username='student'+str(i),
#                 email='student@hero.com',
#                 password='pbkdf2_sha256$120000$rRpl59JV8Gbd$AneGpBBLUkfzCKDvMRWV1pstjvrKWOfOw3FN/6QYT2w=',
#                 is_active=True, 
#                 is_student = True)
#     users.append(user)
 
# CustomUser.objects.bulk_create(users)

# list_user = CustomUser.objects.filter(is_student = True)
# print(list_user)
# semester = Semester.objects.get(semester = 1)
# for x in list_user:
#     student = Student.objects.create(user = x,semester = semester)
#     student.phone_number = 78956
#     student.save()
#     fee_table = FeeTable.objects.create(student =  student)
#     fee_table.save()


# for i in range(5):
#     user = CustomUser(first_name='teacher'+str(i), 
#                 last_name='teacher'+str(i),
#                 username='teacher'+str(i),
#                 email='teacher@gmail.com',
#                 password='pbkdf2_sha256$120000$rRpl59JV8Gbd$AneGpBBLUkfzCKDvMRWV1pstjvrKWOfOw3FN/6QYT2w=',
#                 is_active=True, 
#                 is_teacher = True,
#                 is_student = False)
#     users.append(user)

# list_user = CustomUser.objects.filter(is_teacher = True)
# for x in list_user:
#     teacher = Teacher.objects.create(user= x)
#     teacher.save()

# subject_list = {
#     '1':["Introduction of Information Technology","Fundamentals of Computer Programming","Statistics","Calculus and Analytical Geometry","Static1"],
#     '2':["Digital Logic","Discrete Structure","Microprocessor","Data Structure And Algorithm","Linear Algebra","Statistic II"],
#     '3':[""]
# }
# teachers = Teacher.objects.all()
# for s in range(1,8):
#     semester = Semester.objects.get(semester = s)
#     for x in range(2):
#         book = Books.objects.create(name = 'Book '+str(s)+" of " + str(x),semester = semester,author = 'Some One',nou_registered = 3)
#         book.save()
#         for _ in range(int(book.nou_registered)):    
#             book_instance = BookInstance.objects.create(book =  book)
#             book_instance.save()
#         book.reset()
#passw0rd23
users = CustomUser.objects.all()
# pbkdf2_sha256$120000$nkT8BwmyBvJw$5RrSm00akXJz70JBXUf5aHOVc39hPZFMdAonV9dMrJg=
for user in users:
    user.password = 'pbkdf2_sha256$120000$nkT8BwmyBvJw$5RrSm00akXJz70JBXUf5aHOVc39hPZFMdAonV9dMrJg='
    user.save()

