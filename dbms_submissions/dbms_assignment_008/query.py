Q1='''SELECT d.id,d.fname from director d where  
not exists(select m.id from moviedirector md inner join movie m on m.id=md.mid where d.id=md.did and m.year<2000) and
exists (select m.id from moviedirector md inner join movie m on m.id=md.mid  where d.id=md.did and m.year>2000) group by d.id;'''
Q2='''select d.fname ,
(Select m.name from movie m 
inner join moviedirector md 
on md.mid=m.id where md.did=d.id
order by rank desc,m.name ASC limit 1 ) from director d  limit 100;
'''
Q3='''SELECT * from actor a where not exists (select distinct c.pid from cast c  inner join movie m on m.id=c.mid where a.id=c.pid and m.year between 1990 and 2000) order by a.id desc limit 100;
'''