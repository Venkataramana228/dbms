Q1="SELECT AVG(AGE) FROM PLAYER;"

Q2="SELECT match_no,play_date from MATCH where audience>50000 order by match_no ASC;"

Q3='''SELECT t.team_id,count(win_lose) as won
from matchteamdetails mtd inner join team t on t.team_id=mtd.team_id 
where win_lose='W' group by t.team_id having match_no>=1 
order by won desc,t.team_id asc;'''

Q4='''SELECT match_no,play_date from match
where stop1_sec>(select avg(stop1_sec) from match) 
order by match_no desc;'''

Q5='''SELECT m.match_no,t.name,p.name 
from team t inner join player p inner join matchcaptain mc 
inner join match m inner join matchteamdetails mtd 
on p.team_id=mtd.team_id and m.match_no=mtd.match_no
and m.match_no=mc.match_no and t.team_id=mc.team_id 
and p.team_id=mc.team_id and p.player_id=mc.captain
group by m.match_no,t.name,p.name 
order by m.match_no asc,t.name asc;'''

Q6='''SELECT m.match_no,p.name,p.jersey_no 
from player p inner join match m inner join matchteamdetails mtd 
on mtd.team_id=p.team_id and mtd.match_no=m.match_no and m.player_of_match=p.player_id 
order by m.match_no;'''

Q7='''SELECT t.name,avg(age) as avg_age 
from team t inner join player p on t.team_id=p.team_id 
group by p.team_id having avg_age>26
order by t.name asc;'''

Q8='''SELECT p.name,p.jersey_no,p.age,count(goal_id) 
from player p inner join goaldetails gd on p.player_id=gd.player_id and p.team_id=gd.team_id 
group by p.player_id having p.age<=27 
order by count(goal_id) desc,p.name asc;'''

Q9='''SELECT gds.team_id,(COUNT(gds.goal_id)*100.0)/(select count(goal_id) from goaldetails gd) from goaldetails gds group by gds.team_id ;
'''

#Q9='''SELECT gds.team_id,((select count(goal_id) from goaldetails gd where gds.team_id=gd.team_id  group by  gd.team_id having count(goal_id)>=1) * 100.0)/(select count(goal_id) from goaldetails gd  ) from goaldetails gds group by gds.team_id;'''

Q10="SELECT avg(total_goal_score) from (select count(goal_id) as total_goal_score from goaldetails gd group by gd.team_id);"

Q11='''SELECT p.player_id,p.name,p.date_of_birth 
from player p where not exists(select gd.player_id from match m inner join goaldetails gd on gd.player_id=p.player_id and gd.match_no=m.match_no  
group by gd.player_id having count(goal_id)!=0) l
order by p.player_id;'''

Q12='''SELECT t.name,mtd.match_no,m.audience,
audience-(select avg(audience) from match m inner join matchteamdetails mtd on mtd.match_no=m.match_no and mtd.team_id=t.team_id group by mtd.team_id)  
from team t  inner join matchteamdetails mtd inner join match m
on m.match_no=mtd.match_no and t.team_id=mtd.team_id order by m.match_no;'''