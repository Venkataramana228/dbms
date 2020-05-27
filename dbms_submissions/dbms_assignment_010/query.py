Q1='''SELECT p.player_id,p.team_id,
p.jersey_no,p.name,p.date_of_birth,
p.age FROM Player p INNER JOIN  
matchcaptain mc on p.player_id=mc.captain and p.team_id=mc.team_id left join goaldetails gd
on gd.player_id=p.player_id
where gd.goal_id is null;'''

Q2='''SELECT team_id,COUNT(match_no) from 
matchteamdetails group by team_id;'''

Q3='''SELECT team_id, ((select count(goal_id) from goaldetails gd 
where gd.team_id=t.team_id
group by gd.team_id)*1.0) /(select count(p.player_id) 
from player p where p.team_id=t.team_id  
group by p.team_id) as avg from team t Group by team_id having avg is not null ;'''

Q4='''SELECT captain,count(captain) from
matchcaptain  mc group by captain;'''

Q5='''SELECT count(captain) from (select mc.captain from 
matchcaptain mc inner join match m on m.match_no=mc.match_no 
where m.player_of_match=mc.captain group by captain);'''

Q6='''select distinct p.player_id from player p 
where exists (select mc.captain from matchcaptain mc 
where p.player_id=mc.captain group by captain) and 
not exists (select player_of_match from match m where p.player_id=m.player_of_match 
group by player_of_match having count(player_of_match)!=0);'''

Q7='''select strftime('%m',play_date) as month,count(match_no)
from match group by month;'''

Q8='''SELECT p.jersey_no,count(captain) from
player p inner join matchcaptain mc on p.player_id=mc.captain
group by p.jersey_no order by count(mc.captain) desc,jersey_no desc;'''

Q9='''SELECT p.player_id,avg(audience) as avg from
player p inner join match m inner join matchteamdetails mtd  
on m.match_no=mtd.match_no and p.team_id=mtd.team_id 
group by p.player_id order by avg desc,player_id desc;'''

Q10='''SELECT p.team_id,avg(age) from 
player p inner join team t on p.team_id=t.team_id
group by p.team_id;'''

Q11='''select avg(age) from player p inner join matchcaptain mc 
on p.player_id=mc.captain;'''

Q12='''select strftime('%m',date_of_birth) as month,count(player_id) as no_of_players from  player p 
group by month order by no_of_players desc,month desc;'''

Q13='''SELECT mc.captain,count(win_lose) as wins from 
matchteamdetails mtd inner join matchcaptain mc 
on mc.match_no=mtd.match_no and mc.team_id=mtd.team_id
where win_lose='W' group by captain order by wins desc;'''

Q13='''SELECT mc.captain,(select count(mtd.win_lose) from matchteamdetails mtd where mtd.win_lose="W" and mc.team_id=mtd.team_id) as wins from matchcaptain mc group by mc.captain having wins>=1 order by wins desc;'''

