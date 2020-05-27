class DoesNotExist(Exception):
    pass
class MultipleObjectsReturned(Exception):
    pass
class InvalidField(Exception):
    pass

class Student:
    def __init__(self,name,age,score):
        self.name=name
        self.student_id=None
        self.age=age
        self.score=score
        
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(self.student_id,self.name,self.age,self.score)
   
       
    @classmethod
    def get(cls,student_id=0,name="",age=0,score=-1,**kwargs):
        if student_id!=0:
            x=read_data("select * from Student where student_id={}".format(student_id))
        elif name!="":
            x=read_data("select * from Student where name='{}' ".format(name))
        elif age>0:
            x=read_data("select * from Student where age={}".format(age))
        elif score!=-1:
            x=read_data("select * from Student where score={}".format(score))
        else:
            raise InvalidField
        if len(x)==0:
            raise DoesNotExist
        elif len(x)>1:
            raise MultipleObjectsReturned
        else:
            res=Student(x[0][1],x[0][2],x[0][3])
            res.student_id=x[0][0]
            return res
            
    def delete(self):
        write_data("delete from Student where student_id={}".format(self.student_id))
    
    def save(self):
        import sqlite3
        connection = sqlite3.connect("selected_students.sqlite3")
        crsr = connection.cursor() 
        crsr.execute("PRAGMA foreign_keys=on;") 
        if self.student_id==None:
            inst="insert into Student(name,age,score) values('{}',{},{})".format(self.name,self.age,self.score)
            crsr.execute(inst)
            self.student_id=crsr.lastrowid
        elif ("select {} from Student where student_id not in (select student_id from Student)".format(self.student_id)):
            inst="insert  or replace into Student(student_id,name,age,score) values({},'{}',{},{}) ".format(self.student_id,self.name,self.age,self.score)
            crsr.execute(inst)
            self.student_id=crsr.lastrowid
        else:
            ram="update Student set name='{}',age={},score={} where student_id={}".format(self.name,self.age,self.score,self.student_id)
            crsr.execute(ram)
            
        connection.commit() 
        connection.close()
    
    @classmethod
    def filter(cls,**kwargs):
        l=[]
        mem=['student_id','name','age','score']
        for key,value in kwargs.items():
            att=key.split("__")
            l.append(tuple(att))
            
            
            if(att[0]==key and key in mem):
               
                if att[0]!='name':
                    q=f'select * from Student where {att[0]}={value}'
                else:
                    q=f"select * from Student where {att[0]}='{value}'"
                y=read_data(q)
            
            elif(att[0] in  mem and att[1]=="lt"):
                q=f'select * from Student where {att[0]}<{value}' 
                y=read_data(q)
                
            elif(att[0] in mem and att[1]=="lte"):
                q=f'select * from Student where {att[0]}<={value}'
                y=read_data(q)
                
            elif(att[0] in mem and att[1]=="gt"):
                q=f'select * from Student where {att[0]}>{value}'
                y=read_data(q)
    
            elif(att[0] in mem and att[1]=="gte"):
                q=f'select * from Student where {att[0]}>={value}'
                y=read_data(q)
                
            elif(att[0] in mem and att[1]=="neq"):
                if att[0]!='name':
                    q=f"select * from Student where {att[0]}!={value}"
                else:
                    q=f"select * from Student where {att[0]}!='{value}'"
                
                y=read_data(q)
                
            elif(att[0] in mem and att[1]=="in"):
                q=f'select * from Student where {att[0]} in {tuple(value)}'
                y=read_data(q)
                
            elif(att[0] in mem and att[1]=="contains"):
                q=f'select * from Student where {att[0]} LIKE "%{value}%"'
                y=read_data(q)
                
            else:
                raise InvalidField
        
            record=[]
            if len(y)==0:
                return y
            else:
                for i in range(len(y)):
                    res=Student(y[i][1],y[i][2],y[i][3])
                    res.student_id=y[i][0]
                    record.append(res)
        return record
                        
            
            
        
        
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()
    	
    
def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("selected_students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute(sql_query) 
    ans= crsr.fetchall()  
    connection.close() 
    return ans

'''s=Student.filter(age__lt=5,score__lt=40)'''
