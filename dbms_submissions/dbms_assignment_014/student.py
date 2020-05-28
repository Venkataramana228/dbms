

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
    
    @staticmethod
    def aggregate(op,field,**kwargs):
        att=["student_id","name","age","score"]
        if field not in att:
            raise InvalidField
        if len(kwargs)==0:
            q=f"select {op}({field}) from Student"
        else:
            cond=Student.filter(**kwargs)
            q=f"select {op}({field}) from student where {cond}"
        res=read_data(q)
        return res[0][0]
        
    
    @classmethod
    def avg(cls,field,**kwargs):
        x=cls.aggregate("avg",field,**kwargs)
        return x
        
    @classmethod
    def min(cls,field,**kwargs):
        x=cls.aggregate("min",field,**kwargs)
        return x
    
    @classmethod
    def max(cls,field,**kwargs):
        x=cls.aggregate("max",field,**kwargs)
        return x
    
    @classmethod
    def sum(cls,field,**kwargs):
        x=cls.aggregate("sum",field,**kwargs)
        return x
        
    @classmethod
    def count(cls,field=None,**kwargs):
        x=cls.aggregate("count",field,**kwargs)
        return x
    
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
	
