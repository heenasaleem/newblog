import unittest
import Change_Password
import Download_Blog
import My_Blogs
import SignIn
import SignUp
import Validate_Profile
import Write_Blog
import os
import HTMLTestRunner

direct = os.getcwd()

class MyTestSuite(unittest.TestCase):



    def test_Issue(self):



        smoke_test = unittest.TestSuite()

        smoke_test.addTests([

            unittest.defaultTestLoader.loadTestsFromTestCase(SignIn.Blog),
            unittest.defaultTestLoader.loadTestsFromTestCase(SignUp.Blog_SignUp),
            unittest.defaultTestLoader.loadTestsFromTestCase(Write_Blog.Write_Blog_1),
            unittest.defaultTestLoader.loadTestsFromTestCase(My_Blogs.MyBlogs),
            unittest.defaultTestLoader.loadTestsFromTestCase(Validate_Profile.Profile_vaidate),
            unittest.defaultTestLoader.loadTestsFromTestCase(Change_Password.ChangePassword),
            unittest.defaultTestLoader.loadTestsFromTestCase(Download_Blog.Download_file),

        ])

        outfile = open(direct + "\SmokeTest_Blog_App.html", "w")



        runner1 = HTMLTestRunner.HTMLTestRunner(

            stream=outfile,

            title='Test Report',

            description='Smoke Tests'

        )

        runner1.run(smoke_test)

if __name__ == '__main__':

    unittest.main()