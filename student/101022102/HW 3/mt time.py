# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 15:51:44 2014

@author: user
"""

+	class Time(object):
    
+	    def print_time(time):
+	        print '%.2d:%.2d:%.2d' % (time.hour,time.minute,time.second)
+	
+	    def time_to_int(time):
+	        return time.hour*3600+time.minute*60+time.second        
+	
+	    def is_after(self,other):
+	        return Time.time_to_int(self) > Time.time_to_int(other)
+	
+	    def increment_modifier(self,second):
+	        a = Time.time_to_int(self)
+	        a = a + second
+	        self.hour = a/3600
+	        self.minute = (a%3600)/60
+	        self.second = (a%3600)%60
+	        print Time.print_time(self)
+	
+	    def increment_pure(self,second):
+	        time3 = Time()
+	        a = Time.time_to_int(self)
+	        a = a + second
+	        time3.hour = a/3600
+	        time3.minute = (a%3600)/60
+	        time3.second = (a%3600)%60
+	        print Time.print_time(time3)
+	
+	    def mul_time(self,n):
+	        self.hour *= n
+	        self.minute *= n
+	        self.second *= n
+	        a = Time.time_to_int(self)
+	        self.hour = a/3600
+	        self.minute = (a%3600)/60
+	        self.second = (a%3600)%60
+	        print Time.print_time(self)
+	
+	
+	t1 = Time()
+	t1.hour = 2
+	t1.minute = 40
+	t1.second = 13
+	
+	t2 = Time()
+	t2.hour = 15
+	t2.minute = 36
+	t2.second = 9
+	
+	Time.mul_time(time1,2)
