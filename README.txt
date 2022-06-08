---------------------------------HAVE 3 MAIN CLASS---------------------------------------------
    + Staff: save info of Staff (code, name, age, gender, email, departmentID)
    + Department: save info of Department, one Department have many Staff
    + Attendance: save info of Attendance, it describe who attend or not attend in every date
------------------------------------------------------------------------------------------------


-------------------------------THERE ARE 2 HTTP REQUEST-----------------------------------------
    + GET: to get all data of Staff
    + POST: receive an info of any Staff, then check him/her in DB:
        . If he/she is exist, attend him/her and send a response with his/her info
        . If he/she isn't exist, do not thing and send a response with empty data
------------------------------------------------------------------------------------------------


--------------------------------HOW TO RUN THIS PROJECT-----------------------------------------
1, Create a super user, use command:            >python manage.py createsuperuser
2, Run server with command:                     >python manage.py runserver
3, Use this account to login in /admin url
3, Add Department, Staff normally
------------------------------------------------------------------------------------------------


------------------------------HOW TO SEND GET/POST REQUEST--------------------------------------
1, Use VSCode extension: REST CLIENT
2, Use PostMan app
(I will guide you later)
------------------------------------------------------------------------------------------------


----------------------------------------CONTACT-------------------------------------------------
                        If you have any question, contact to me:
- Email:    bloghuy2818@gmail.com
- Phone:    0934998527
- Facebook: https://www.facebook.com/meow.ihuka.2801/
------------------------------------------------------------------------------------------------
