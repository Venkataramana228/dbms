
Q1='''SELECT * from actor a where 
exists (select c.pid from cast c inner join movie m 
on m.id=c.mid and a.id=c.pid 
where m.name like 'Annie%');'''

Q2='''SELECT m.id,m.name,m.rank,m.year FROM MOVIE m where
exists(select md.mid from moviedirector md inner join director d 
on m.id=md.mid and d.id=md.did and m.id=md.mid 
where d.fname='Biff' and lname='Malibu' and 
m.year in (1999,1994,2003)) order by m.rank desc,m.year asc;'''

Q3='''SELECT year,count(id) from movie 
group by year having avg(rank)>(select avg(rank) from movie) order by year ;'''

Q4='''SELECT * FROM movie where year==2001 
and rank<(select avg(rank) from movie where year=2001 ) 
order by rank desc limit 10;'''


Q5='''Select m.id,female.count,male.count from movie m ,(select mid,count(a.id) as count from actor a inner join cast c on a.id=c.pid where gender ='F'  group by c.mid) as female,
(select mid,count(a.id) as count from actor a inner join cast c on a.id=c.pid where gender ='M' group by c.mid) as male where m.id=male.mid and  m.id=female.mid order by m.id asc limit 100;'''

Q6='''SELECT DISTINCT pid from cast c inner join movie m
on m.id=c.mid group by mid,pid having count(distinct c.role)>1
order by pid asc limit 100;'''

Q7='''SELECT fname,count(id) from director
group by fname having count(id)>1;'''

Q8='''select d.id,d.fname,d.lname from director d 
where exists(select md.did from moviedirector md inner join cast c 
on c.mid=md.mid and d.id=md.did group by c.mid having count(c.pid)>=100)
and not exists(select md.did from moviedirector md inner join cast c 
on c.mid=md.mid and d.id=md.did group by c.mid having count(c.pid)<100);'''




'''Q5=select id,(select count(gender) from actor a inner join cast c 
on a.id=c.pid  and m.id=c.mid where gender=='F'), 
(select count(gender) from actor a inner join cast c 
on a.id=c.pid  and m.id=c.mid where gender=='M') 
FROM MOVIE  m order by id limit 100;
'''
'''Q5=SELECT id,count(gender) from (select pid from actor a inner join cast c on a.id=c.pid and m.id=c.mid where gender='F'),count(gender) from (select pid from actor a inner join cast c on a.id=c.pid and m.id=c.mid where gender='M') FROM Movie
m order by id limit 100;'''
