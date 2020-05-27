'''class InvalidField(Exception):
    pass

class Student:
    def __init__(self,name,age,score):
        self.name=name
        self.student_id=None
        self.age=age
        self.score=score
    
    @classmethod
    def avg(cls, field, **kwargs):
        mem=["student_id","name","age","score"]
        
        if field in mem:
            if len(kwargs)==0:
                q=f"select avg({field}) from Student"
                res=read_data(q)
                
            else:
                for key,value in kwargs.items():
                    arg=key.split("__")
                    if arg[0]==key and arg[0] in mem:
                        q=f"select avg({field}) from Student where {arg[0]}={value}"
                    elif(arg[0] in  mem and arg[1]=="lt"):
                        q=f"select avg({field}) from Student where {arg[0]}<{value}"
                    elif(arg[0] in  mem and arg[1]=="lte"):
                        q=f"select avg({field}) from Student where {arg[0]}<={value}"
                    elif(arg[0] in  mem and arg[1]=="gt"):
                        q=f"select avg({field}) from Student where {arg[0]}>{value}"
                    elif(arg[0] in  mem and arg[1]=="gte"):
                        q=f"select avg({field}) from Student where {arg[0]}>={value}"
                    elif(arg[0] in  mem and arg[1]=="neq"):
                        q=f"select avg({field}) from Student where {arg[0]}!={value}"
                    elif(arg[0] in  mem and arg[1]=="in"):
                        q=f"select avg({field}) from Student where {arg[0]} in {tuple(value)}"
                    elif(arg[0] in  mem and arg[1]=="contains"):
                        q=f"select avg({field}) from Student where {arg[0]} LIKE '%{value}%'"
                    else:
                        raise InvalidField  
                    res=read_data(q)
                    if res[0][0]==None:
                        return 0.0
    
                #return res[0][0]     
            return res[0][0]
        else:
            raise InvalidField
    
    @classmethod
    def min(cls, field, **kwargs):
        mem=["student_id","name","age","score"]
        if field in mem:
            if len(kwargs)==0:
                q=f"select min({field}) from Student"
                res=read_data(q)
                
            else:
                for key,value in kwargs.items():
                    arg=key.split("__")
                    if arg[0]==key and arg[0] in mem:
                        if key=="name":
                            q=f"select min({field}) from Student where {arg[0]}='{value}'"
                        else:
                            q=f"select min({field}) from Student where {arg[0]}={value}"
                    elif(arg[0] in  mem and arg[1]=="lt"):
                        q=f"select min({field}) from Student where {arg[0]}<{value}"
                    elif(arg[0] in  mem and arg[1]=="lte"):
                        q=f"select min({field}) from Student where {arg[0]}<={value}"
                    elif(arg[0] in  mem and arg[1]=="gt"):
                        q=f"select min({field}) from Student where {arg[0]}>{value}"
                    elif(arg[0] in  mem and arg[1]=="gte"):
                        q=f"select min({field}) from Student where {arg[0]}>={value}"
                    elif(arg[0] in  mem and arg[1]=="neq"):
                        q=f"select min({field}) from Student where {arg[0]}!={value}"
                    elif(arg[0] in  mem and arg[1]=="in"):
                        q=f"select min({field}) from Student where {arg[0]} in {tuple(value)}"
                    elif(arg[0] in  mem and arg[1]=="contains"):
                        q=f"select min({field}) from Student where {arg[0]} LIKE '%{value}%'"
                    else:
                        raise InvalidField  
                    res=read_data(q)
                    if res[0][0]==None:
                        return None
    
                return res[0][0]     
            return res[0][0]
        else:
            raise InvalidField
        
    @classmethod
    def max(cls, field, **kwargs):
        mem=["student_id","name","age","score"]
        if field in mem:
            if len(kwargs)==0:
                q=f"select max({field}) from Student"
                res=read_data(q)
                
            else:
                for key,value in kwargs.items():
                    arg=key.split("__")
                    if arg[0]==key and arg[0] in mem:
                        if key=="name":
                            q=f"select max({field}) from Student where {arg[0]}='{value}'"
                        else:
                            q=f"select max({field}) from Student where {arg[0]}={value}"
                    elif(arg[0] in  mem and arg[1]=="lt"):
                        q=f"select max({field}) from Student where {arg[0]}<{value}"
                    elif(arg[0] in  mem and arg[1]=="lte"):
                        q=f"select max({field}) from Student where {arg[0]}<={value}"
                    elif(arg[0] in  mem and arg[1]=="gt"):
                        q=f"select max({field}) from Student where {arg[0]}>{value}"
                    elif(arg[0] in  mem and arg[1]=="gte"):
                        q=f"select max({field}) from Student where {arg[0]}>={value}"
                    elif(arg[0] in  mem and arg[1]=="neq"):
                        if key=="name":
                            q=f"select max({field}) from Student where {arg[0]}!='{value}'"
                        else:
                            q=f"select max({field}) from Student where {arg[0]}!={value}"
                    elif(arg[0] in  mem and arg[1]=="in"):
                        q=f"select max({field}) from Student where {arg[0]} in {tuple(value)}"
                    elif(arg[0] in  mem and arg[1]=="contains"):
                        q=f"select max({field}) from Student where {arg[0]} LIKE '%{value}%'"
                    else:
                        raise InvalidField  
                    res=read_data(q)
                    if res[0][0]==None:
                        return None
    
                return res[0][0]     
            return res[0][0]
        else:
            raise InvalidField
       
    @classmethod
    def sum(cls, field, **kwargs):
        mem=["student_id","name","age","score"]
        if field in mem:
            if len(kwargs)==0:
                q=f"select sum({field}) from Student"
                res=read_data(q)
                
            else:
                for key,value in kwargs.items():
                    arg=key.split("__")
                    if arg[0]==key and arg[0] in mem:
                        q=f"select sum({field}) from Student where {arg[0]}={value}"
                    elif(arg[0] in  mem and arg[1]=="lt"):
                        q=f"select sum({field}) from Student where {arg[0]}<{value}"
                    elif(arg[0] in  mem and arg[1]=="lte"):
                        q=f"select sum({field}) from Student where {arg[0]}<={value}"
                    elif(arg[0] in  mem and arg[1]=="gt"):
                        q=f"select sum({field}) from Student where {arg[0]}>{value}"
                    elif(arg[0] in  mem and arg[1]=="gte"):
                        q=f"select sum({field}) from Student where {arg[0]}>={value}"
                    elif(arg[0] in  mem and arg[1]=="neq"):
                        q=f"select sum({field}) from Student where {arg[0]}!={value}"
                    elif(arg[0] in  mem and arg[1]=="in"):
                        q=f"select sum({field}) from Student where {arg[0]} in {tuple(value)}"
                    elif(arg[0] in  mem and arg[1]=="contains"):
                        q=f"select sum({field}) from Student where {arg[0]} LIKE '%{value}%'"
                    else:
                        raise InvalidField  
                    res=read_data(q)
                    if res[0][0]==None:
                        return len(res)
    
                return res[0][0]     
            return res[0][0]
        else:
            raise InvalidField
       
    @classmethod
    def count(cls, field, **kwargs):
        mem=["student_id","name","age","score"]
        if field in mem:
            if len(kwargs)==0:
                q=f"select count({field}) from Student"
                res=read_data(q)
                
            else:
                for key,value in kwargs.items():
                    arg=key.split("__")
                    if arg[0]==key and arg[0] in mem:
                        if key=="name":
                            q=f"select count({field}) from Student where {arg[0]}='{value}'"
                        else:
                            q=f"select count({field}) from Student where {arg[0]}={value}"
                    elif(arg[0] in  mem and arg[1]=="lt"):
                        q=f"select count({field}) from Student where {arg[0]}<{value}"
                    elif(arg[0] in  mem and arg[1]=="lte"):
                        q=f"select count({field}) from Student where {arg[0]}<={value}"
                    elif(arg[0] in  mem and arg[1]=="gt"):
                        q=f"select count({field}) from Student where {arg[0]}>{value}"
                    elif(arg[0] in  mem and arg[1]=="gte"):
                        q=f"select count({field}) from Student where {arg[0]}>={value}"
                    elif(arg[0] in  mem and arg[1]=="neq"):
                        q=f"select count({field}) from Student where {arg[0]}!={value}"
                    elif(arg[0] in  mem and arg[1]=="in"):
                        q=f"select count({field}) from Student where {arg[0]} in {tuple(value)}"
                    elif(arg[0] in  mem and arg[1]=="contains"):
                        q=f"select count({field}) from Student where {arg[0]} LIKE '%{value}%'"
                    else:
                        raise InvalidField  
                    res=read_data(q)
                    if res[0][0]==None:
                        return 0
            return res[0][0]
        else:
            raise InvalidField
       
       
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans'''
	
'''s=Student.avg("age")
print(s)'''


class InvalidField(Exception):
    pass
class Student:
    def __init__(self,name,age,score):
        self.name=name
        self.student_id=None
        self.age=age
        self.score=score
    @staticmethod
    def filter(**kwargs):
        list=[]
        mem=["student_id","name","age","score"]
        operations={'lt':'<','lte':'<=','gt':'>','gte':'>=','eq':'=','neq':'!='}
        for key,value in kwargs.items():
            l=key.split("__")
            
            if l[0] not in mem:
                raise InvalidField
            if l[0] in mem and len(l)==1:
                if l[0]=='name':
                    query=f"{key}='{value}'"
                else:
                    query=f"{key}={value}"
            elif l[1]=='in':
                query=f"{l[0]} in {tuple(value)}"
            elif l[1]=='contains':
                query=f"{l[0]} Like '%{value}%'"
            else:
                query=f"{l[0]}{operations[l[1]]}{value}"
            list.append(query)
        return " and ".join(list)
    
    @classmethod
    def avg(cls,field,**kwargs):
        att=["student_id","name","age","score"]
        if field not in att:
            raise InvalidField
        if len(kwargs)==0:
            q=f"select avg({field}) from Student"
        else:
            cond=Student.filter(**kwargs)
            q=f"select avg({field}) from student where {cond}"
        res=read_data(q)
        return res[0][0]
        
    @classmethod
    def min(cls,field,**kwargs):
        att=["student_id","name","age","score"]
        if field not in att:
            raise InvalidField
        if len(kwargs)==0:
            q=f"select min({field}) from Student"
        else:
            cond=Student.filter(**kwargs)
            q=f"select min({field}) from student where {cond}"
        res=read_data(q)
        return res[0][0]
    
    @classmethod
    def max(cls,field,**kwargs):
        att=["student_id","name","age","score"]
        if field not in att:
            raise InvalidField
        if len(kwargs)==0:
            q=f"select max({field}) from Student"
        else:
            cond=Student.filter(**kwargs)
            q=f"select max({field}) from student where {cond}"
        res=read_data(q)
        return res[0][0]
    
    @classmethod
    def sum(cls,field,**kwargs):
        att=["student_id","name","age","score"]
        if field not in att:
            raise InvalidField
        if len(kwargs)==0:
            q=f"select sum({field}) from Student"
        else:
            cond=Student.filter(**kwargs)
            q=f"select sum({field}) from student where {cond}"
        res=read_data(q)
        return res[0][0]
    
    @classmethod
    def count(cls,field=None,**kwargs):
        att=["student_id","name","age","score"]
        if field==None:
            q=f"select count(*) from Student"
        elif field not in att:
            raise InvalidField
        elif len(kwargs)==0:
            q=f"select count({field}) from Student"
        else:
            cond=Student.filter(**kwargs)
            q=f"select count({field}) from student where {cond}"
        res=read_data(q)
        return res[0][0]
    
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans
	
'''s=Student.avg("age",age__lt=20)
print(s)'''